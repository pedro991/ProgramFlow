import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

while guess != 0:
    if guess == answer:
        print("Well done!")
        break
    elif guess < answer:
        print("Please guess higher")
        guess = int(input())
    else:
        print("Please guess lower")
        guess = int(input())

# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
