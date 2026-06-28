







defeat_dungeonBoss = input("Did you defeat the Dungeon Boss? (yes/no) ").strip().lower()

if defeat_dungeonBoss == "no":
    print("Defeat the Dungeon Boss First")
else:
    collect_treasureChest = input("Did you collect the Treasure Chest? (yes/no) ").strip().lower()
    if collect_treasureChest == "no":
        print("Go collect the Treasure Chest")
    else:
        users_class = input("choose your class? (warrior/mage/archer) ").strip().lower()
        if users_class == "warrior":
            prefer_attacks = input("Do you prefer Attack? (yes/no) ").strip().lower()
            if prefer_attacks == "yes":
                print("Reward: Legendary Sword")
            else:
                print("Reward: Legendary Shield")
        else:
            if users_class == "mage":
                prefer_fireMagic_attacks = input("Do you prefer Fire Magic attacks? (yes/no) ").strip().lower()
                if prefer_fireMagic_attacks == "yes":
                    print("Reward: Phoenix Staff")
                else:
                    print("Reward: Ice Staff")
            else:
                if users_class == "archer":
                    prefer_longRange_attacks = input("Do you prefer Long Range attacks? (yes/no) ").strip().lower()
                    if prefer_longRange_attacks == "yes":
                        print("Reward: Eagle Bow")
                    else:
                        print("Reward: Twin Daggers")
