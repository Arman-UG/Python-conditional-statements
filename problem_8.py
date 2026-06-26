
account_balance = int(input("How much balance you have left: "))
withdraw_amount = int(input("enter withdrawal amount: "))

if account_balance >= withdraw_amount:
    if withdraw_amount > 20000:
        print("Cash dispensed: Require manager approval")
    else:
        new_account_balance = account_balance - withdraw_amount
        print("Cash withdrawal successfully: ", withdraw_amount, "Left balance: ", new_account_balance)
else:
    print("Insufficient funds")
