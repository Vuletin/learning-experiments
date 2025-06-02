number = int(input("Number: "))

for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")