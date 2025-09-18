from BankAccount import BankAccount


class CheckingAccount(BankAccount):
    # Instantiation
    def __init__(self, customer_name, current, minimum, transfer_limit, routing_num, account_num):
        super().__init__(customer_name, current, minimum, routing_num, account_num)
        self.limit = transfer_limit
        self.transferred = 0

    def transfer(self, amount, account):
        if amount < 0 or amount > self.current_balance - self.minimum_balance:
            print("Not enough funds.")
            return
        elif self.transferred + amount > self.limit:
            print("Transfer would exceed limit.  Only $" + str(self.limit - self.transferred)
                  + " more may be moved until the limit resets.")
            return
        else:
            self.withdraw(amount)
            account.deposit(amount)
            self.transferred += amount

    def reset_transfer_limit(self):
        self.transferred = 0
