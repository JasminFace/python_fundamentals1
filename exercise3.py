#Part 1
print("What is your name?")
user_name = input()
print("Hello, {}".format(user_name))


#Part 2
secret_password = "please"

print("What's the password?")
password_attempt = input()

correct_or_not = (password_attempt == secret_password)

print("That's {}!".format(correct_or_not))


#Part 3
print("How many cookies have been eaten?")
eaten = input()

remaining_cookies = 12 - int(eaten)

print("There are {} cookies left.".format(remaining_cookies))


#Part 4
print("How old will you be this year?")
age = input()
birth_year = 2019 - int(age)
print("You were born in {}.".format(birth_year))