







player_alive = input("does the player alive? (yes/no) ").strip().lower()

if player_alive == "no":
    print("Game over ")

else:
    castle_key = input("did you have castle key? (yes/no) ").strip().lower()
    
    if castle_key == "no":
        print("find castle key")
    else:
        defeat_forestBoss = input("do you have defeat the forest boss? (yes/no) ").strip().lower()

    if defeat_forestBoss == "no":
        print("Defeat the Forest Boss First")
    else:
        print("Welcome to the Dragon Castle!")





