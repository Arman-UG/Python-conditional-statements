employee = input("Are you an employee? (yes/no) ").strip().lower()
id_card = input("Do you have an ID card? (yes/no) ").strip().lower()
security_training = input("Have you completed Security Training? (yes/no) ").strip().lower()

if employee == "yes" and id_card == "yes" and security_training == "yes":
    print("Access Granted.")
else:
    print("Access Denied.")
