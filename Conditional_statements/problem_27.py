identity = input("who are you? (doctor/nurse/patient/visitor) ").strip().lower()



if identity == "doctor":
    id_card = input("Do you have your ID card? (yes/no) ").strip().lower()
    med_license = input("Is your medical license active? (yes/no) ").strip().lower()

    if id_card == "yes" and med_license == "yes":
        print("Access to ICU")
    else:
        print("Access denied")
elif identity == "nurse":
    id_card = input("Do you have your ID card? (yes/no) ").strip().lower()
    shift = input("Are you assigned to today's shift? (yes/no) ").str().lower()

    if id_card == "yes" and shift == "yes":
        print("Access to ward")
    else:
        print("Access denied")
elif identity == "patient":
    appointment = input("Do you have an appointment? (yes/no) ").strip().lower()
    emergency = input("Is it an emergency? (yes/no) ").strip().lower()

    if emergency == "yes":
        print("emergency ward")
    elif appointment == "yes":
        print("wait in the normal queue") 
    else:
        print("please make an appointment first")
elif identity == "visitor":
    visitor_hours = input("Visiting hours? (yes/no) ").strip().lower()
    visitor_pass = input("Visitor pass? (yes/no) ").strip().lower()

    if visitor_hours == "yes" and visitor_pass == "yes":
        print("Visitors entry granted") 
    else:
        print("Access denied")
else:
    print("Invalid input")       
    
