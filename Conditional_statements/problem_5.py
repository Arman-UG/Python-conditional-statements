is_live_product = input("Company has live product? Yes or No: ").strip().lower()
monthly_budget = float(input("Monthly budget of company: "))
num_of_employee = int(input("How many employees in the company: "))


min_employees = 5
min_budget = float(50000.0)

gift = "If you join us we make free live product for your company"

if is_live_product == "yes":
    if (monthly_budget >= min_budget):
        if (num_of_employee >= min_employees):
            print("Hot Deal - Schedule a Call")
    if monthly_budget < min_budget:
        print("Warm Deal - Send an email. 🎁", gift)

elif is_live_product == "no":
    if (monthly_budget >= min_budget):
        if (num_of_employee >= min_employees):
            print("Warm Deal - Send an email. 🎁", gift)

elif monthly_budget < min_budget:
        if num_of_employee > min_employees:
            if is_live_product == "yes" or "no":
                print("Warm Deal - Send an email. 🎁", gift)

else:
    print("We respect your Ideas. However unfortunately we can't go further\n If any possibility in future we will.")