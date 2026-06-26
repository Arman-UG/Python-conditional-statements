passed_12th = input("Have you passed 12th grade? (yes/no) ").strip().lower()


if passed_12th == "no":
    print("Admission Rejected")
else:
    stream = input("choose your stream? (Engineering/Medical/Commerce) ").strip().lower()
    if stream == "engineering":
        maths = input("Do you know Mathematics? (yes/no) ").strip().lower()
        if maths == "yes":
            print("Engineering Admission Approved")
        else:
            print("Mathematics Required")
    elif stream == "medical":
        biology = input("Do you know Biology? (yes/no) ").strip().lower()
        if biology == "yes":
            print("Medical Admission Approved")
        else:
            print("Biology Required")
    elif stream == "commerce":
        accounts = input("Do you know Accounting? (yes/no) ").strip().lower()
        if accounts == "yes":
            print("Commerce Admission Approved")
        else:
            print("Accounting Required")
    else:
        print("Invalid Stream")