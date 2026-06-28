for inspection in range(8):
    passenger_name = input("Name: ").strip().lower()
    boarding_pass = input("did you have boarding pass? (yes/no) ").strip().lower()
    prohibited_items = input("Are you carrying prohibited items? (yes/no) ").strip().lower()

    if boarding_pass == "yes" and prohibited_items == "no":
        print("Security cleared.")
    else:
        print("Send to Secondary Inspection")