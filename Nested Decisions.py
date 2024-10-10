place = input("Choose a place: forest or cave? ")



if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
         print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You found a hidden treasure!")
    if place == "cave":   
        option = input("light a torch/proceed in the dark? ")       # Task 2: Setting the Scene
    if option == "light a torch":
         print("You found a treasure!")
    elif option == ("proceed in the dark"):
         print("Good luck!")
    else:
        print("Please select again adventurer!")
else:                       
    print("Please select again adventurer!")
