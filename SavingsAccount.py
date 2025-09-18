import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current, minimum, interest, routing_num, account_num):
        super().__init__(customer_name, current, minimum, routing_num, account_num)
        self.interest = interest

    def interest_tick(self):
        self.current_balance *= (1 + self.interest)
    