import random

def game():
    # Generate a random number between 1 and 10
    secret_num = random.randint(1, 10)

    while True:
        # get a number guess from player
        guess = int(input("Guess a number between 1 and 10: "))

        # compare guess to secret number
        if guess == secret_num:
            print("You got it! My number was {}".format(secret_num))
            break
        else:
        # print hit/miss
            print("That's not my number noob")

game()

