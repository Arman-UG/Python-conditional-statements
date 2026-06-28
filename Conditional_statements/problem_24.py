identity = input("who are you? (developer/tester/devops) ").strip().lower()



if identity == "developer" :
    test_cases_pass = input("Did all tests pass? (yes/no) ").strip().lower()
    code_review = input("Is the code reviewed? (yes/no) ").strip().lower()

    if test_cases_pass == "yes" and code_review == "yes":
        print("Merge into `Main`")
    else:
        print("Fix pending issues.") 
elif identity == "tester":
    regression_testing = input("Regression Testing completed? (yes/no) ").strip().lower()
    bugs = input("Critical Bugs found? (yes/no) ").strip().lower()

    if regression_testing == "yes" and bugs == "no":
        print("Test passed")
    else:
        print("Return build to Developers")
elif identity == "devops":
    approval_received = input("Production approval received? (yes/no) ").strip().lower()
    backup = input("Backup completed? (yes/no) ").strip().lower()

    if approval_received == "yes" and backup == "yes":
        print("Deploy to Production")
    else:
        print("Deployment Blocked")
else:
    print("Invalid input")