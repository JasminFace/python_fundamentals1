distance = 0
energy = 10

while True:
    print("Would you like to walk or run?")
    motion = input() #either walk or run

    if motion == "walk":
        if energy - 1 < 0:
            print("You're too tired to walk. Rest or get some food!")
        else:
            distance += 1
            energy -= 1  
    elif motion == "run":
        if energy - 5 < 0:
            print("You're too tired to run. Rest or get some food!")
        else:
            distance += 5
            energy -= 5
    elif motion == "go home":
        break
    else:
        print("What do you want to do?")

    print("Distance from home is {} km.".format(distance))
    print("Your energy level is {}.".format(energy))