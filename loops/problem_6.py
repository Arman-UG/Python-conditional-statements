for inventory in range(5):
    item = input("What is your Item? (potion/sword/shield) ").strip().lower()
    if item == "potion":
        print("You have Potion")
    elif item == "sword":
        print("you have sword")
    elif item == "shield":
        print("you have shield")
    else:
        print("Unknown Item")