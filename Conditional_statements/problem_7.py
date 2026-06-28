




user_experience = int(input("How many years of experience do you have: "))
knows_python = input("Did you know Python language? (yes/no) ").strip().lower()
knows_selenium = input("Did you know Selenium (yes/no) ")


if user_experience >= 2:
    if knows_python == "yes":
        if knows_selenium == "yes":
            print("Technical Interview + Automation Team")
        else:
            print("Technical Interview + Development Team")
    else:
        print("Eligible for HR round only")
        
else:
    print("Rejected: Insufficient experience")