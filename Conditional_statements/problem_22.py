logged_in = input("Are you logged in? ").strip().lower()



if logged_in == "no":
    print("Access Denied")
else:
    identity = input("who are you? (employee/manager/hr) ").strip().lower()
    if identity == "employee":
        leave_type = input("Leave Type? (sick/casual/emergency) ").strip().lower()
        if leave_type == "sick":
            has_medical_certificate = input("Do you have medical certificate? (yes/no) ").strip().lower()
            if has_medical_certificate == "no":
                print("bring medical certificate")
            else:
                medical_certificate_submit = input("Medical Certificate Submitted? (yes/no) ").strip().lower()
                if medical_certificate_submit == "yes":
                    print("Leave Approved")
                else:
                    print("Medical Certificate Required")
        elif leave_type == "casual":
            leave_days = int(input("How many leave days? "))
            if leave_days <= 2:
                print("Auto Approved")
            elif leave_days <= 5:
                married = input("are you married? (yes/no) ").strip().lower()
                if married == "no":
                    print("Manager Approval Required")
                else:
                    reason = input("Enter the leave reason? (sick/drappointment/family problem) ").strip().lower()
                    if reason == "sick":
                        print("Manager Approval Required")
                    elif reason == "drappointment":
                        print("Valid reason. Leave approved")
                    elif reason == "familyproblem":
                        print("Valid reason. Leave approved")
                    else:
                        print("Invalid reason")
            elif leave_days > 5:
                reason = input("Explain the reason")
                if reason:
                    print("wait for the HR Approval.")
        elif leave_type == "emergency":
            informed = input("Has Manager been informed? (yes/no) ").strip().lower()
            if informed == "yes":
                print("Emergency Leave Approved")
            else:
                #my opinion and it's worth only in emergency situation
                print("Emergency leave approved. don't forgot to mail the manager later")
    elif identity == "manager":
        action = input("Choose Action? (Approve Leave/View Team)").strip().lower()
        if action == "approveleave":
            print("Leaves dashboard is opening....")
        elif action == "viewteam":
            print("Team dashboard is opening....")   
        else:
            print("You don't have permissions")
    elif identity == "hr":
        action = input("Choose Action? (payroll/recruitment/leaves)").strip().lower()
        if action == "payroll":
            print("Payroll dashboard is opening....")
        elif action == "recruitment":
            print("Recruitment dashboard is opening....")
        elif action == "leaves":
            print("Leaves dashboard is opening....")
        else:
            print("Invalid action")
    else:
        print("You don't have permission to enter")
