from http.client import HTTPException

from fastapi import APIRouter, Depends, HTTPException
from customer_service import getAllCustomers
from repo import CustomerRepo, getDB

router = APIRouter()

@router.get("/")
def getAllCustomersService(db: CustomerRepo = Depends(getDB) ):
    try:
        return getAllCustomers(db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))