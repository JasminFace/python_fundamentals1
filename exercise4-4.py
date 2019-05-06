secret_number = 143

print("Let's play a game. Pick ANY number.")
number = int(input())

if number == secret_number:
    print("YOU WIN!")
elif number == 142 or number == 144:
    print("So close!")
else:
    print("Try again.")