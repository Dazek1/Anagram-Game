import random

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

def generate_the_word(word_list):
    return random.choice(word_list)

def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled

word_length = 4
infile = open("Word_list.txt","r")
word = random_line(x for x in infile if len(x) == word_length + 1).strip("\n")
infile.close()
print(word)
print(shuffle_word(word))