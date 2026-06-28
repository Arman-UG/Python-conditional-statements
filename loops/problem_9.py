cafe_open = "yes"

while cafe_open == "yes":
    customer_name = input("What is your name: ").strip().lower()
    play_hours = int(input("How many hours you wants to play? "))

    print("Welcome", customer_name, "Your playing hours is:", play_hours, "Your time start now")
    cafe_open = input("Is the cafe still open? (yes/no) ").strip().lower()

    if cafe_open == "no":
        print("Cafe closed")