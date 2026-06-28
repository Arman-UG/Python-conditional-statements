participants_registration = int(input("How many participants are registering today? "))

for participant in range(participants_registration):
    welcome_massage = "Welcome to the Tech conference."
    name = input("enter your name: ").strip().lower()
    if name == "":
        print("enter your name first.")
    else:
        email = input("enter your email: ").strip().lower()
        identity = input("Are you student or professional? (student/professional) ").strip().lower()
        if email == "":
            print("Enter email first.")
        else:
            if identity == "student" or identity == "professional":
                print("congratulation, registration successful. \n here is your shared details-- \n name: ", name,"\n email: ", email,"\n identity: ", identity)
            else:
                print("unauthorized person")


