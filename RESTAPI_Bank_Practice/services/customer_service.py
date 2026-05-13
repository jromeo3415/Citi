from models import models

class CustomerService:
    @staticmethod
    def get_all_customers_service(database):
        return database[0]

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