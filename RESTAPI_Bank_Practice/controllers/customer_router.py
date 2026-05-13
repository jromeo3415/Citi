from fastapi import APIRouter, HTTPException
from services.customer_service import CustomerService
from repo.repo import db
from models.models import Customer, CustomerCreate

router = APIRouter()

@router.get("/")
def get_all_customers_route(database = db):
    return CustomerService.get_all_customers_service(database)

@router.get("/{customer_id}")
def get_customer_route(customer_id: int, database = db):
    customer = CustomerService.get_customer_by_id_service(database, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer

@router.post("/")
def create_user_route(customer: CustomerCreate, database = db):
    return CustomerService.create_user_service(database, customer)