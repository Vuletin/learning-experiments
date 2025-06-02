import random

power = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

you = input("pick: rock, paper, scissors ").lower()
cpu = random.choice(power)

print ("you chose", you)
print ("cpu chose", cpu)

if power[cpu] == you:
    print("cpu wins")
elif power[you] == cpu:
    print("you win")
elif cpu == you:
    print("It's draw")