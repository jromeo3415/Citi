from fastapi import FastAPI
from controllers import customer_router
from controllers import account_router

app = FastAPI()

#   /api/customers router
app.include_router(customer_router.router, prefix="/api/customers")

#   /api/accounts router
app.include_router(account_router.router, prefix="/api/accounts")