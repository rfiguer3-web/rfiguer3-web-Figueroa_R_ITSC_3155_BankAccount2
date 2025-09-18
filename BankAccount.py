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
    def __init__(self, customer_name, current, minimum):
        self.customer_name = customer_name
        self.current_balance = current
        self.minimum_balance = minimum

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
        print("Minimum Balance:", self.minimum_balance, "\n")
