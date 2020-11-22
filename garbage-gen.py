from string import ascii_letters; from random import randrange
chars = list(ascii_letters); chars.extend(list("1234567890!@#$%^&*()-=_+[];':,."))
returnlist = []

while True:
    for iterloop in range(1000):
        returnlist.append(chars[randrange(len(chars))])
    print("".join(returnlist))