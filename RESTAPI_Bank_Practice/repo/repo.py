from models import models

customers = []
accounts = []

john_saving = models.Account(id = 1, type = "Savings", balance = 129.23)
accounts.append(john_saving)
bob_checking = models.Account(id = 2, type =  "Checking", balance = 234.33)
accounts.append(bob_checking)
jane_checking = models.Account(id = 3, type = "Checking", balance = 3444.53)
accounts.append(jane_checking)
jane_saving = models.Account(id = 4, type = "Saving", balance = 234244.35)
accounts.append(jane_saving)


customers.append(models.Customer(id = 1, name = "John", account = [john_saving]))
customers.append(models.Customer(id = 2, name = "Bob", account = [bob_checking]))
customers.append(models.Customer(id = 3, name = "Jane", account = [jane_checking, jane_saving]))

#    maybe fix this using dictionary or something
db = [customers, accounts]