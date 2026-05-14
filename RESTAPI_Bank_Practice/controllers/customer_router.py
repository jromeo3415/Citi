from fastapi import APIRouter, HTTPException, Depends
from services.customer_service import CustomerService
from database.database import db
from models.models import Customer, CustomerCreate
from dependency import get_customer_service
from util import clean_mongo_doc
router = APIRouter()

@router.get("/")
def get_all_customers_route(service: CustomerService = Depends(get_customer_service)):
    response = service.get_all_customers_service()
    return [clean_mongo_doc(item) for item in response]

@router.get("/{customer_id}")
def get_customer_route(customer_id: int, db):
    customer = CustomerService.get_customer_by_id_service(db, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer

@router.post("/")
def create_user_route(customer: CustomerCreate, db):
    return CustomerService.create_user_service(db, customer)