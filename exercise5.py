distance = 0

while distance >= 0:
    print("Would you like to walk or run?")
    motion = input() #either walk or run

    if motion == "walk":
        distance += 1
        print("Distance from home is {} km.".format(distance))
    elif motion == "run":
        distance += 5
        print("Distance from home is {} km.".format(distance))
    else:
        print("I said walk or run.")