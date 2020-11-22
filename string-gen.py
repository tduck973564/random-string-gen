from string import ascii_letters; from random import randrange
chars = list(ascii_letters); chars.extend(list("1234567890!@#$%^&*()-=_+[];':,."))
returnlist = []

exclude = list(input("Type characters you would like to exclude > "))
iternum = int(input("Type the length of the random string. > "))
chars = [x for x in chars if x not in exclude]

for iterloop in range(iternum):
        returnlist.append(chars[randrange(len(chars))])
print("".join(returnlist))