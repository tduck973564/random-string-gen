inputArray = list(input("Type in the password you want rated here. > "))
lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = lowerLetters.extend(upperLetters)
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '|', ';', "'", ':', ',', '.', '/', '<', '>', '?']
lowerLettersCount = upperLettersCount = lettersCount = numbersCount = symbolsCount = 0
points = 0
for i in inputArray:
    if i in lowerLetters:
        lowerLettersCount += 1
        lettersCount += 1
    elif i in upperLetters:
        upperLettersCount += 1
        lettersCount += 1
    elif i in numbers:
        numbersCount += 1
    elif i in symbols:
        symbolsCount += 1

if numbersCount:
    points += 2
if symbolsCount:
    points += 2
if upperLettersCount:
    points += 1
elif upperLettersCount == lowerLettersCount == numbersCount == symbolsCount:
    points += 10
elif lowerLettersCount > upperLettersCount:
    points -= 3
elif lettersCount > numbersCount:
    points -= 3
elif lettersCount > symbolsCount:
    points -= 2
elif upperLettersCount > lowerLettersCount:
    points += 1
elif symbolsCount > lettersCount:
    points += 1
elif numbersCount > lettersCount:
    points += 1
points += len(inputArray) / 4
print(f"The password score is {points}.")