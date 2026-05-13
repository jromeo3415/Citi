from repo.repo import db
from services.customer_service import CustomerService
from models.models import Customer
import copy

def test_get_customer_by_id_service_equal():
    account = db[1]
    expected = Customer(id=1, name="John", account=[account[0]])

    actual = CustomerService.get_customer_by_id_service(db, 1)

    assert expected == actual

def test_get_customer_by_id_service_not_equal():
    account = db[1]
    expected = Customer(id=1, name="Alex", account=[account[0]]) #  name is mutant

    actual = CustomerService.get_customer_by_id_service(db, 1)

    assert expected != actual # expression changed to reflect expected outcome

def test_get_all_customers_service_equal():
    accounts = db[0]
    expected = accounts

    actual = CustomerService.get_all_customers_service(db)

    assert expected == actual

def test_get_all_customers_service_not_equal():
    customers = copy.deepcopy(db[0]) #  required to ensure original list is not modified
    expected = customers
    accounts = db[1] #  required to give an account to this mutant customer
    expected.append(Customer(id=7, name="asdf", account=[accounts[0]])) # mutant (new customer)

    actual = CustomerService.get_all_customers_service(db)

    assert expected != actual # expression changed to reflect expected outcome