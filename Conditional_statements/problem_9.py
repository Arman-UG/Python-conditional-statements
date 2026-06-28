valid_passport = input("Do you have valid passport? (yes/no)").strip().lower()
valid_visa = input("Do you have valid Visa? (yes/no)").strip().lower()
prohibited_items = input("Are you carrying 'prohibited items?' (yes/no)").strip().lower()

if valid_passport == "yes":
    if valid_visa == "yes":
        if prohibited_items == "yes":
            print("Security Inspection")
        else:
            print("boarding allowed")
    else:
        print("entry denied")
else:
    print("entry denied")              