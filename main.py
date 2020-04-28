import random

life = 8
file = open("nouns.txt", "r")
if file.mode == "r":
    contents = file.readlines()

guess = contents[random.randint(0, len(contents))]
guess1 = []


def scan(word, letter):
    s = 0
    for let in range(len(word) - 1):
        if letter == word[let]:
            s += 1

    if s == 0:
        return True

    return False


def ins(word, letter, word1):
    for let in range(len(word)-1):
        if letter == word[let]:
            word1[let] = letter
    print(word1)


def final(word1):
    s = 0
    for x in word1:
        if x == '_':
            s += 1

    if s > 0:
        return False
    else:
        return True

for x in range(len(guess)-1):
    guess1.append('_')
print(guess1)

while life > 0:
    print("life", life)
    inputs = ""
    y = input("enter letter ")
    if scan(guess, y):
        print("Wrong letter")
        print(guess1)
        life -= 1
    else:
        ins(guess, y, guess1)

    if life == 0:
        print("You lost word was", guess)
    if final(guess1):
        print("You won")
        break
