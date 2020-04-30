name = input("Please, enter your name: ")
age = int(input("Now your age: "))

if 18 <= age < 31:
    print("Welcome aboard, {}!!".format(name))
else:
    print("Nice try smart-ass! You're not in the range")
