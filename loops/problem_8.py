

identity = input("Are you manager (yes/no) ").strip().lower()

if identity == "no":
    print("Access denied, Only manager can allow to open the Bill software")
    
else:
    today_customer_orders = int(input("How many customers are ordering today? "))
    for customer in range(today_customer_orders):
        customer_name = input("what's your name? ").strip().lower()
        if customer_name == "":
            print("Enter you name first.")
        else:
            table_number = int(input("What is your table number? "))
            if table_number <= 0:
                print("Invalid table number.")
            else:
                meal_type = input("What is your meal type? (veg/nonVeg/drinks/desert) ").strip().lower()
                bill_amount = float(input("enter your bill amount: "))
                if bill_amount >= 1000:
                    final_bill_amount = bill_amount - bill_amount * 10 / 100
                    print("Customer name: ", customer_name, "\n Table number: ", table_number, "\n Meal type: ", meal_type, "\n Original bill: ", bill_amount, "\n Discount : 10%", "\n Final bill: ", final_bill_amount)
                else:
                    print("Customer name: ", customer_name, "\n Table number: ", table_number, "\n Meal type: ", meal_type, "\n bill: ", bill_amount, "Sorry your bill amount is under 1000, No discounts are allowed in this amount")
            
