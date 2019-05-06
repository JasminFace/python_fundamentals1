distance = 0
energy = 40

while True:
    print("Would you like to walk or run?")
    motion = input() #either walk or run

    if motion == "walk":
        if energy - 1 < 0:
            print("You're too tired to walk. Take a break or get some food!")
        else:
            distance += 1
            energy -= 1  
    elif motion == "run":
        if energy -4 < 0:
            print("You're too tired to run. Take a break or get some food!")
        else:
            distance += 4
            energy -= 4
    elif motion == "eat":
        energy += 6
        print("Nom, nom. Delicious!")
    elif motion == "rest":
        energy += 8
        print("Relax! Stay a while!")
    elif motion == "go home":
        break
    else:
        print("What do you want to do?")

    print("Distance from home is {} km.".format(distance))
    print("Your energy level is {}.".format(energy))