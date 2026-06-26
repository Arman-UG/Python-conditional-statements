


rocket_ready = input("is rocket ready for the final test? (yes/no) ").strip().lower()

if rocket_ready == "no":
    print("make it ready first")
else:
    weather = input("what's the condition of weather? (clear/cloudy/storm) ").strip().lower()

    if weather == "storm":
        print("Launch cancel")
    elif weather == "cloudy":
        rocket_engineers = input("rocket engineers are you all agree with the launch? (yes/no) ").strip().lower()
        rocket_dept_head = input("RDH Sir, are you agree with the launch? (yes/no) ").strip().lower()
        space_engineers = input("Space engineers are you all agree with the launch? (yes/no) ").strip().lower()
        if rocket_dept_head == "yes" and rocket_engineers == "yes" and space_engineers == "yes": 
            fuel_loaded = input("fuel loaded? (yes/no) ").strip().lower()
            navigation = input("navigation system ready? (yes/no) ").strip().lower()
            communication = input("communication system is ready? (yes/no) ").strip().lower()
            if fuel_loaded == "yes" and navigation == "yes" and communication == "yes":
                print("Launch approved")
            else:
                print("Launch cancel")
        else:
            print("launch cancel")
    elif weather == "clear":
        fuel_loaded = input("fuel loaded? (yes/no) ").strip().lower()
        navigation = input("navigation system ready? (yes/no) ").strip().lower()
        communication = input("communication system is ready? (yes/no) ").strip().lower()
        if fuel_loaded == "yes":
            if navigation == "yes" and communication == "yes":
                print("Launch approved")
            else:
                print("Launch cancel")
    else:
        print("Invalid question")


