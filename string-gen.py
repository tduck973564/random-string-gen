from random import randrange
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '|', ';', ':', ',', '.', '<', '>', '/', '?', '`', '~']
returnlist = []

exclude = list(input("Type characters you would like to exclude > "))
iternum = int(input("Type the length of the random string. > "))
chars = [x for x in chars if x not in exclude]

for iterloop in range(iternum):
        returnlist.append(chars[randrange(len(chars))])
print("".join(returnlist))