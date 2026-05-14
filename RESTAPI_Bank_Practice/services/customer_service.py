from models import models
from repo.repo import CustomerRepo

class CustomerService:
    def __init__(self, repo):
        self.repo = repo

    def get_all_customers_service(self):
        collection = self.repo.collection
        print(collection)
        customers = []
        for customer in collection.find():
            print(customer)
            customers.append(customer)

        return customers

    @staticmethod
    def get_customer_by_id_service(database, id):
        customers = database[0]
        for customer in customers:
            if customer.id == id:
                return customer

        return None

    @staticmethod
    def create_user_service(database, customer):
        new_user = models.Customer(
            id = len(database),
            name = customer.name,
            account =  [])

        database[0].append(new_user)
        return {"message": f"Successfully added customer {customer.name}"}