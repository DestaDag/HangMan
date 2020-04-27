import random
life = 8
nouns = open("nouns.txt", "r")

if nouns.mode == 'r':
    contents = nouns.readlines()

guess = contents[random.randint(0, len(contents))]
print(guess)
for x in range(len(guess)-1):
    print("_")

y = input("enter letter ")
for let in range(len(guess)-1):
    if y == guess[let]:
        print(y)
    else:
        print("_")
