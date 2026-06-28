


identity = input("who are you? (operator/supervisor/mteengineer/visitors) ").strip().lower()

if identity == "operator":
    under_maintenance = input("does the machine under maintenance? (yes/no) ").strip().lower()
    if under_maintenance == "yes":
         print("Machine is under maintenance")
    else:
        machine = input("You want to start the machine? (yes/no) ").strip().lower()
        permission = input("Do you have permission from the supervisor? (yes/no) ").strip().lower()
        if machine == "yes" and permission == "yes":            
            authorized = input("Are you authorized? (yes/no) ").strip().lower()
            if authorized == "no":
                print("Access denied.")
            else:
                gloves = input("Have you wear gloves? (yes/no) ").strip().lower()
                helmet = input("Have you wear helmet? (yes/no) ").strip().lower()
                glasses = input("Have you wear glasses? (yes/no) ").strip().lower()
                if gloves == "yes" and helmet == "yes" and glasses == "yes":
                    print("You can start the machine")
                else:
                    print("Access denied. first please carefully wear all the required protective elements")
        else:
            print("Access denied.")

elif identity == "supervisor":
    inspect_production = input("Do you want to inspect the production? (yes/no) ").strip().lower()
    if inspect_production == "no":
        print("Sorry sir, Only if you want to inspect the production your access can granted.")
    else:
        production_emg = input("Sir, production runs in emergency mode. Are you willing to inspect the production? (yes/no) ").strip().lower()
        if production_emg == "yes":
            gloves = input("Have you wear gloves? (yes/no) ").strip().lower()
            helmet = input("Have you wear helmet? (yes/no) ").strip().lower()
            glasses = input("Have you wear glasses? (yes/no) ").strip().lower()

            if gloves == "yes" and helmet == "yes" and glasses == "yes":
                print("Sure sir you can inspect the production")
            else:
                print("Please sir, carefully wear all the required protective elements")
        else:
            print("Good decision, sir")

elif identity == "mtengineer":
    emergency_stop = input("Does the emergency stop is pressed? (yes/no) ").strip().lower()
    if emergency_stop == "no":
        print("Quickly press the emergency stop button")
    else:
        safety_gate = input("does the safety gates are open? (yes/no) ").strip().lower()
        protective_element = input("Have you wear all protective elements carefully? (yes/no) ").strip().lower()
        if safety_gate == "yes" and protective_element == "yes":
            print("Access granted")
        else:
            print("Access denied")
elif identity == "visitors":
    spl_card = input("Did you have the visitors card? (yes/no) ").strip().lower()
    if spl_card == "yes":
        glasses = input("Did you wear special visitors glasses? (yes/no) ").strip().lower()
        mask = input("did you wear special visitors mask? (yes/no) ").strip().lower()
        if glasses == "yes" and mask == "yes":
            machine_running = input("is machine is running? (yes/no) ").strip().lower()
            if machine_running == "yes":
                print("Access denied")
            else:
                print("Access granted. Enjoy your visit.")
        else:
            print("access denied: please wear all the required protective elements first")
    else:
        print("access denied: Please collect the card first. It's for visitors security")

