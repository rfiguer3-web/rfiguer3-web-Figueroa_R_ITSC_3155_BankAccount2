import CheckingAccount
import SavingsAccount

# Creation of 2 savings accounts
savings1 = SavingsAccount.SavingsAccount("Robert", 100, 10, .05, 1234, 10001)
savings2 = SavingsAccount.SavingsAccount("Gabby", 150, 20, .04, 5678, 10002)

# Creation of 2 checking accounts
checking1 = CheckingAccount.CheckingAccount("Robert", 50, 10, 40, 1278, 10003)
checking2 = CheckingAccount.CheckingAccount("Gabby", 80, 12, 50, 3456, 10004)

# Ensuring that Savings accounts work like Bank Accounts
savings1.print_customer_information()
savings2.print_customer_information()

# This should not work
savings1.withdraw(95)
savings2.withdraw(140)

# There should be no change by here
savings1.print_customer_information()
savings2.print_customer_information()

# This should work
savings1.withdraw(20)
savings2.withdraw(10)

# Should display 80 and 140 as balances
savings1.print_customer_information()
savings2.print_customer_information()

# Adding money into accounts
savings1.deposit(100)
savings2.deposit(100)

# Should display 180 and 240 as balances
savings1.print_customer_information()
savings2.print_customer_information()

# Ensuring that Checking accounts work like Bank Accounts

checking1.print_customer_information()
checking2.print_customer_information()

# This should not work
checking1.withdraw(45)
checking2.withdraw(70)

# There should be no change by here
checking1.print_customer_information()
checking2.print_customer_information()

# This should work
checking1.withdraw(20)
checking2.withdraw(10)

# Should display 30 and 70 as balances
checking1.print_customer_information()
checking2.print_customer_information()

# Adding money into accounts
checking1.deposit(100)
checking2.deposit(100)

# Should display 130 and 170 as balances
checking1.print_customer_information()
checking2.print_customer_information()

# Testing that the interest tick work
savings1.print_customer_information()
savings2.print_customer_information()

# Tick the interest
savings1.interest_tick()
savings2.interest_tick()

# Should display previous balances with interest added
savings1.print_customer_information()
savings2.print_customer_information()

# Testing that transferring works on checking accounts
checking1.print_customer_information()
checking2.print_customer_information()

# Try to go past limits
checking1.transfer(50, savings1)
checking2.transfer(60, savings2)

# Ensure nothing changed
checking1.print_customer_information()
checking2.print_customer_information()
savings1.print_customer_information()
savings2.print_customer_information()

# Transfer correctly
checking1.transfer(20, savings1)
checking2.transfer(30, savings2)

# Ensure balances are as follows: 110, 140, 200, 270
checking1.print_customer_information()
checking2.print_customer_information()
savings1.print_customer_information()
savings2.print_customer_information()

# FAKE SCENARIO
print("Robert opens a savings account and put's $500 in with a 10% annual interest rate.")
scenario_savings = SavingsAccount.SavingsAccount(
    "Robert", 500, 50, .1, 100, 200)
scenario_savings.print_customer_information()

print("There is a minimum of $50 needed to be kept in the account at all times.")
print("To test this, Robert tries to take out all $500.")
scenario_savings.withdraw(500)
scenario_savings.print_customer_information()

print("After this, Robert adds $100 every month for 10 months.")
# For the sake of keeping the code somewhat clean, I made this one $1000 deposit
scenario_savings.deposit(1000)
scenario_savings.print_customer_information()

print("After another 2 months pass, the interest kicks in")
scenario_savings.interest_tick()
scenario_savings.print_customer_information()

print("Robert now withdraws $500 for an emergency expense.")
scenario_savings.withdraw(500)
scenario_savings.print_customer_information()

print("Robert values the importance of a savings account.")
print("He continues to put money in every month for the rest of his life until he retires early.")