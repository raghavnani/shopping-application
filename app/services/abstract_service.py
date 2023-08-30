class AbstractService():
    

    def find_all(self):
        return self.repository().find_all()

    def find_by_id(self, id):
        return self.repository().find_by_id(id)

    def repository(self):
        raise NotImplementedError("Inherited Service should implement repository()")

    def delete_by_id(self, id):
        self.repository().delete_by_id(id)
