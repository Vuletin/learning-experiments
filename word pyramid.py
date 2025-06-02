def pyramid():   
    word= input("word: ")
    number = int(input("number: "))

    for _ in range(number):
        for _ in range(number + (_ - number + 1)):
            print(word, end="")
        print()

pyramid()