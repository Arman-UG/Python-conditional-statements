















player_alive = input("does the player alive? (yes/no) ").strip().lower()

if player_alive == "no":
    print("Game over ")

else:
    have_sword = input("Do you have a Sword? (yes/no) ").strip().lower()
    
    if have_sword == "no":
        print("Find a Sword First")
    else:
        temple_key = input("Do you have the Temple Key? (yes/no) ").strip().lower()

        if temple_key == "no":
            print("Find the Temple Key")
        else:
            level_10 = input("Have you reached Level 10? (yes/no) ")
            if level_10 == "no":
                print("Reach Level 10 First")
            else:
                print("Welcome to the Ancient Temple!")






