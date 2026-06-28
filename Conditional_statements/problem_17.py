



employee = input("Are you an employee? (yes/no) ").strip().lower()

if employee == "no":
    print("Visitor Entry")
else:
    id_card = input("Do you have your ID Card? (yes/no) ").strip().lower()
    if id_card == "no":
        print("Access Denied")
    else:
        department = input("Choose your department? (IT/HR/Finance)").strip().lower()
        if department == "it":
            serverRoom_access = input("Do you need Server Room access? (yes/no) ").strip().lower()
            if serverRoom_access == "yes":
                print("Opening Server Room...")
            else:
                print("Opening IT dashboard...")
        else:
            if department == "hr":
                Payroll_access = input("Do you need Payroll access? (yes/no) ").strip().lower()
                if Payroll_access == "yes":
                    print("Opening Payroll dashboard...")
                else:
                    print("Opening HR dashboard...")
            else:
                if department == "finance":
                    authorization_letter = input("Are you carrying today's authorization letter? (yes/no) ").strip().lower()
                    if authorization_letter == "yes":
                        print("Opening Finance Vault...")
                    else:
                        print("Opening Finance dashboard...")
                else:
                    print("Invalid department.")