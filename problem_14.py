


user_loggedIn = input("are you logged in? (yes/no) ").strip().lower()

if user_loggedIn == "no":
    print("Access Denied")
else:

    identity = input("who are you? (Admin/HR/Employee) ").strip().lower()
    if identity == "admin":
        manage_users = input("do you want to manage users? (yes/no) ").strip().lower()
        if manage_users == "yes":
            print("Opening User Management Panel...")
        else:
            print("Opening Admin Dashboard...")
    else:
        if identity == "hr":
            process_payrolls = input("Do you want to process payroll? (yes/no) ").strip().lower()
            if process_payrolls == "yes":
                print("Opening Payroll Module...")
            else:
                print("Opening Employee Records...")
        else:
            if identity == "employee":
                apply_leave = input("Do you want to apply for leave? (yes/no) ")
                if apply_leave == "yes":
                    print("Opening Leave Portal...")
                else:
                    print("Opening Employee Dashboard...")
