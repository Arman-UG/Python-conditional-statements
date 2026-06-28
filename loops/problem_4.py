for hospital in range(15):
    name = input("Enter your name: ").strip().lower()
    if name == "":
        print("Please enter your name first")
        break
    else:
        emergency = input("Do you have an emergency? (yes/no )").strip().lower()

        if emergency == "yes":
            print("Emergency ward")
        else:
            print("Normal queue")