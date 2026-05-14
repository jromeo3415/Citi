from services.customer_service import  CustomerService
from repo.repo import CustomerRepo
from fastapi import Depends
from database.database import db

def get_customer_repo():
    return CustomerRepo(db)

def get_customer_service(repo: CustomerRepo = Depends(get_customer_repo)):
    return CustomerService(repo)