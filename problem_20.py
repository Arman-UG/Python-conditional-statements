user_loggedIn = input("Are you logged in? (yes/no) ").strip().lower()


if user_loggedIn == "no":
    print("please log in")
else:
    food_category = input("Choose your food category?(Pizza/Burger/Biryani) ").strip().lower()

    if food_category == "pizza":
        extra_cheese = input("Do you want extra cheese? (yes/no) ").strip().lower()
        if extra_cheese == "yes":
            print("Large Cheese Pizza")
        else:
            print("Regular Pizza")
    elif food_category == "burger":
        want_fries = input("Do you want fries? (yes/no) ").strip().lower()
        if want_fries == "yes":
            print("Burger Combo")
        else:
            print("Classic Burger")
    elif food_category == "biryani":
        cold_drink = input("Do you want a cold drink? (yes/no) ").strip().lower()
        if cold_drink == "yes":
            print("Biryani Combo")
        else:
            print("Regular Biryani")
    else:
        print("Not available.")