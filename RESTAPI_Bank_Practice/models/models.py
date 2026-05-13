from pydantic import BaseModel

class Account(BaseModel):
    id: int
    type: str
    balance: float

class Customer(BaseModel):
    id: int
    name: str
    account: list[Account]

class CustomerCreate(BaseModel):
    name: str