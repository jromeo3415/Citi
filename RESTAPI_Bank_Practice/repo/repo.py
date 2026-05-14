from bson import ObjectId


class CustomerRepo:
    def __init__(self, db):
        self.collection = db["customers"]

    def get_customer_by_id_repo(self, id: str):
        return self.collection.find_one(({"id": ObjectId(id)}))