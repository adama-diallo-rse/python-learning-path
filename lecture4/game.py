import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

answer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < answer:
                print("Too small!")
            elif guess > answer:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass