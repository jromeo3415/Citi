import customer_service
from fastapi import FastAPI

app = FastAPI()

#   localhost:8080/api/customers : return all customers as JSON response
@app.get("/api/customers")
def CustomerController:
    def __init__(customerService):
        customerService = service.getAllCustomers()

    def getAllCustomers(self):
        return self.customerService

#   localhost:8080/api/accounts
class AccountController:
    def __init__(accountService):
        accountService = service.getAllServices()

    def getAllAccounts(self):
        return self.acccountService
