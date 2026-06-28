# patient_breathing = input("is the patient breathing? (yes/no) ").strip().lower()

# patient_bleeding = input("is the patient bleeding heavily? (yes/no) ").strip().lower()

# patient_fever = input("does the patient has fever? (yes/no) ").strip().lower()

# # My addition and It's worth

# fever_temp = int(input("fever temperature? "))

# if patient_breathing == "yes":

#     if patient_bleeding == "yes":

#         print("Emergency Surgery")

#     else:

#         if patient_fever == "yes":

#             if fever_temp >= 102:

#                 print("Emergency appointment")

#             else: 
#                 print("General Physician")

#         else:

#             print("Wait in Normal Queue")

# else:

#     print("Immediate CPR")


patient_breathing = input("Is the patient breathing? (yes/no): ").strip().lower()

if patient_breathing == "no":
    print("Immediate CPR")

else:
    patient_bleeding = input("Is the patient bleeding heavily? (yes/no): ").strip().lower()

    if patient_bleeding == "yes":
        print("Emergency Surgery")

    else:
        patient_fever = input("Does the patient have a fever? (yes/no): ").strip().lower()

        if patient_fever == "yes":
            fever_temp = int(input("What is the temperature? "))

            if fever_temp >= 102:
                print("Emergency Appointment")
            else:
                print("General Physician")

        else:
            print("Wait in Normal Queue")