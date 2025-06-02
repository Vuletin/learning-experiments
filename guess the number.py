import random

secret_number = random.randint(1, 10)


guess = None
guesscounter = 0
print("I'm thinking of a number from 1 - 10, can you guess what: ")

while guess != secret_number:

    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("too low")
        guesscounter += 1
    elif guess > secret_number:
        print("too high")
        guesscounter += 1
    else:
        print("correct number")
        guesscounter += 1

print("tried:", guesscounter, end=" times")