import random


file = open("nouns.txt", "r")
if file.mode == "r":
    contents = file.readlines()

guess = contents[random.randint(0, len(contents))]
word_length = []
same_initial = []

def find_same_length_word(word):
    n = len(word)
    for x in range(len(contents)):
        if n == len(contents[x]):
            word_length.append(contents[x])

    return word_length

word_length = find_same_length_word(guess)

def find_same_initial(word):
    first = word[0]
    for x in range(len(word_length)):
        w = word_length[x]
        if first == w[0]:
            same_initial.append(word_length[x])
    
    return same_initial

same_initial = find_same_initial(guess)
same_initial.remove(guess)
print(guess)
print("words with the same length as:", guess,"\n", word_length)
print('\n\nwords with the same initial and length as: ', guess, "\n", same_initial)