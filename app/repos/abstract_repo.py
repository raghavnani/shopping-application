from app import db


class AbstractRepository():


    def entity(self):
        raise NotImplementedError("Inherited repository should implement entity()")

    def find_all(self):
        result = db.session.query(self.entity()).order_by(self.entity().id.desc()).all()
        return result

    def find_by_id(self, id):
        result = db.session.query(self.entity()).filter_by(id=id).first()
        return result
    
    def find_by_name(self, name):
        result = db.session.query(self.entity()).filter_by(name=name).first()
        return result

    def get(self, id):
        return db.session.query(self.entity()).get(id)
    
    def delete(self, entity):
        db.session.delete(entity)
        db.session.commit()
        return entity

    def delete_by_id(self, id):
        entity = self.find_by_id(id)
        if entity is not None:
            return self.delete(entity)
        else:
            return {"error": "Entity not found"}
    
    def update(self, entity):        
        db.session.merge(entity)
        db.session.commit()
        return entity
        
    def insert(self, entity):
        db.session.add(entity)
        db.session.commit()
        result = entity
        return result
    
    def save(self, entity):
        if entity.id is None:
            return self.insert(entity)
        else:
            return self.update(entity)