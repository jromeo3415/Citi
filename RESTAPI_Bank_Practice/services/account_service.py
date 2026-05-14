'''
class AccountService:
    @staticmethod
    def get_all_accounts_service(db):
        return db[1]

    @staticmethod
    def get_account_by_user_id_service(db, user_id):
        customers = db[0]
        for customer in customers:
            if customer.id == user_id:
                return customer.account

        return None

    @staticmethod
    def get_premium_accounts_service(db):
        accounts = db[1]
        premium_accounts = []
        for account in accounts:
            if account.balance > 10000:
                premium_accounts.append(account)

        if len(premium_accounts) > 0:
            return premium_accounts

        else:
            return {"message": "No premium accounts at this time"}
'''