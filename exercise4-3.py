name = "Jasmin"

print("Hi! What's your name?")
their_name = input()

if their_name == name:
    print("Whoa! We have the SAME NAME!")
else:
    print("Hello {}! Nice to meet you!".format(their_name))