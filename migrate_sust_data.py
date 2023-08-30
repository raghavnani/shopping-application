# sql credentials

sql_env = "dev"
sql_server = f"{sql_env}bmclsqldbserver.database.windows.net"
sql_username = "bmcladmin"
sql_password = "pwVTd#n2+LLrh"
sql_database = "8abcd972-549c-49ab-a8c7-a00ad6fe5a53"



# postgres credentials

# sql credentials

postgres_env = "dev"
md_postgres_server = f"bmcl{postgres_env}weumaster-data.postgres.database.azure.com"
postgres_username = "bmcladmin"
postgres_password = "J&GVmwYz64"
sust_database = "sust_8abcd972-549c-49ab-a8c7-a00ad6fe5a53"

sust_server = f"bmcl{postgres_env}weusustainability.postgres.database.azure.com"

master_data_db = "md_8abcd972-549c-49ab-a8c7-a00ad6fe5a53"



mysql_con_str = f'mssql+pyodbc://{sql_username}:{sql_password}@{sql_server}:1433/{sql_database}?driver=ODBC+Driver+18+for+SQL+Server'

sust_con_str = f'postgresql://{postgres_username}:{postgres_password}@{sust_server}:5432/{sust_database}'

md_con_str =  f'postgresql://{postgres_username}:{postgres_password}@{postgres_server}:5432/{master_data_db}'


!pip install sqlalchemy psycopg2 pyodbc

from sqlalchemy import create_engine  

sust_engine = create_engine(sust_con_str)  

mssql_engine = create_engine(mysql_con_str)  

md_engine =  create_engine(md_con_str)  


from sqlalchemy import Table, Column, Integer, String, MetaData, select  
  
metadata = MetaData()  
  
# Define the table schema with the schema name and correct case  
src_table_name = Table(  
    'EnergyRatingBuilding', metadata,  
     autoload=True, autoload_with=mssql_engine,
    schema='dbo'  # Replace with your schema name in the correct case  
) 

dst_table_name = Table(  
    'EnergyRatingBuilding', metadata,  
     autoload=True, autoload_with=sust_engine,  
    schema='eu_taxonomy'  # Replace with your schema name in the correct case  
)  


from sqlalchemy.orm import sessionmaker  

# Create sessions for source and destination databases  
source_Session = sessionmaker(bind=mssql_engine)  
destination_Session = sessionmaker(bind=sust_engine)  
  
source_session = source_Session()  
destination_session = destination_Session()  

data = source_session.query(src_table_name).all()

from sqlalchemy.exc import SQLAlchemyError  


for row in data[1:]:  
    
    try :
        
        energy_rating_id = row.EnergyRatingId 

        
        row_dict = {column.key: getattr(row, column.key, None) for column in dst_table_name.columns if hasattr(row, column.key)}

        row_dict['EnergyRatingId'] = energy_ratings_dict[energy_rating_id]
#         print(row_dict)

#         row_dict['CreatedBy'] = "00000000-0000-0000-0000-000000000000"
#         row_dict['UpdatedBy'] = "00000000-0000-0000-0000-000000000000"
#         row_dict['InternalIdentifier'] = 


        new_row = dst_table_name.insert().values(**row_dict)  


        destination_session.execute(new_row) 
        
#         break
    except SQLAlchemyError as e:  
        # Log the error  
        print(f"Error inserting row {row}: {e}")
        destination_session.rollback()  
        
#         break
destination_session.commit()  

# destination_session.close()




energy_ratings_dict = {}

for row in data:
    new_energy_rating_id = row.energyratingid_generation_source  
    
    energy_ratings_dict[row.EnergyRatingId] = row.energyratingid_generation_source



source_session.close()  
destination_session.close()
