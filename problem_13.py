


user_loggedIn = input("are you logged in? (yes/no) ")

if user_loggedIn == "no":
    print("Please log in.")
else:
    premium_subscription = input("have you a Premium subscription? (yes/no) ")

    if premium_subscription == "no":
        print("Upgrade to Premium.")
    else:
        movie_available = input("Is the movie available in your region? (yes/no) ")

        if movie_available == "no":
            print("Movie unavailable in your region.")
        else:
            need_popcorn = input("do you need popcorn to enjoy your movie? (yes/no) ")

            if need_popcorn == "no":
                print("Enjoy your movie!")
            else:
                print("please proceed the payment. you will get in 5-10 min from Zomato. Enjoy your movie")