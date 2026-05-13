import model

class CustomerRepo:
    def __init__(self):
        self.customers = []
        self.accounts = []
        A1 = model.Account(1, "Checking", 99.99)
        self.accounts.append(A1)

        self.customers.append(model.Customer(1, "John", A1))
        self.customers.append(model.Customer(2, "Tom", A1))
        self.customers.append(model.Customer(3, "Bob", A1))

    def getAllCustomers(self):
        return self.customers

def getDB():
    db = CustomerRepo
    return db