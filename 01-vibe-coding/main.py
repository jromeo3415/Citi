from fastapi import FastAPI
import customer_router

app = FastAPI()

app.include_router(customer_router.router, prefix="/api/customers")