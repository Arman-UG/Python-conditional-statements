


has_job = input("Do you have job? (yes/no) ").strip().lower()

if has_job == "no":
    print("Loan Rejected")
else:
    worked_years = int(input("How many years have you worked?"))

    if worked_years < 2:
        print("Work Experience Too Low")
    else:
        existing_loan = input("Do you have any existing loan? (yes/no) ").strip().lower()
        if existing_loan == "yes":
            emi = input("Have you paid all EMIs on time? (yes/no) ").strip().lower()
            if emi == "yes":
                print("Loan Approved")
            else:
                print("Loan Rejected")
        elif existing_loan == "no":
            print("Loan Approved")