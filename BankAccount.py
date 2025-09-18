"""
File: BankAccount.py
Author: Robert Figueroa, rfiguer3@charlotte.edu
Date: 2025-09-04
Description: This class simulates a basic BankAccount.
"""


class BankAccount:
    # Class variables
    name = "Happy Bank"

    # instantiation
    def __init__(self, customer_name, current, minimum, routing_num, account_num):
        self.customer_name = customer_name
        self.current_balance = current
        self.minimum_balance = minimum
        self._routing_number = routing_num
        self.__account_number = account_num

    # Protected getter for routing number
    def _get_routing_number(self):
        return self._routing_number

    # Deposit method
    def deposit(self, amount):
        self.current_balance += amount

    # Withdraw Method
    def withdraw(self, amount):
        # Check that balance does not go under the minimum amount
        if self.current_balance - amount < self.minimum_balance:
            print("Insufficient balance. " + self.customer_name +
                  "'s Minimum balance is", self.minimum_balance, "\n")
        else:
            self.current_balance -= amount

    # Print method
    def print_customer_information(self):
        print("Bank:", self.name)
        print("Name:", self.customer_name)
        print("Current Balance:", self.current_balance)
        print("Minimum Balance:", self.minimum_balance)
        print("Routing Number:", self._routing_number)
        print("Account Number:", self.__account_number, "\n")
