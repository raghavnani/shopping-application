class AbstractService():
    

    def find_all(self):
        return self.repository().find_all()

    def find_by_id(self, id):
        return self.repository().find_by_id(id)

    def repository(self):
        raise NotImplementedError("Inherited Service should implement repository()")

    def delete_by_id(self, id):
        self.repository().delete_by_id(id)

    def update_by_id(self, id, price, quantity):
        entity =  self.repository().find_by_id(id)
        entity.price = price
        entity.quantity = quantity
        self.repository().update(entity)
        return entity

    