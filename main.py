# Investment Accounts Assignment

import random

def create_investments():
  n = 0
  money = []
  for i in range(20):
    money.append(random.randrange(1, 5000))
    i = i + 1
  return money

investments = create_investments()
print(investments)

# HELPER FUNCTIONS
def print_accounts():
    print("\nACCOUNT BALANCES")
    n = 0
    while n < len(investments):
      print(f"Account {n + 1}: ${investments[n]}")
      n = n + 1

def deposit():
    print("\nDEPOSIT")
    account = input("Enter account #")

# Python Menu Loop

# Main Program Loop 
loop = True
while loop:
  # Print Main Menu
  print("\nINVESTMENTS ACCOUNTS MAIN MENU")
  print("1: Print Accounts")
  print("2: Deposit")
  print("3: Withdrawl")
  print("4: Count Under $2000")
  print("5: Generous Donor")
  print("6: Hacker Attack")
  print("7: EXIT")

  # Get Menu Selection from User
  selection = input("Enter Selection (1-7): ")

  # Take Action Based on Menu Selection  
  if selection == "1":
    print_accounts()
  elif selection == "2":
    deposit()
  elif selection == "3":
    print("Option 3")
  elif selection == "4":
    print("Option 4")
  elif selection == "5":
    print("Option 5")
  elif selection == "6":
    print("Option 6")
  elif selection == "7":
    print("EXIT")
    loop = False