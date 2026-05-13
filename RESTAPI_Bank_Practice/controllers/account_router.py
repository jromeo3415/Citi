from fastapi import APIRouter, HTTPException
from repo.repo import db
from services.account_service import AccountService

router = APIRouter()

@router.get("/")
def get_all_accounts_route(database = db):
    return  AccountService.get_all_accounts_service(database)

@router.get("/premium")
def get_premium_accounts_route(database = db):
    return AccountService.get_premium_accounts_service(database)

@router.get("/{customer_id}")
def get_account_route(customer_id: int, database = db):
    account = AccountService.get_account_by_user_id_service(database, customer_id)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return account