my_age = 27
print("Now tell me, how old are you?")
age = int(input())

difference = my_age - age

if age < 105:
    print("We are {} years apart!".format(abs(difference)))
elif age > 105:
    print("I'm not sure I believe you.")
else:
    print("That's okay, you don't have to say.")