import random

# Gets random line from text file

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

# Shuffles the positions of letters in a word

def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled

# Sets up the game and starts it

def initiate_game():

    word_length = int(input ('How many letters do you want? '))
    infile = open("Word_list.txt","r")
    # Gets the random word of the input length and strips the new line
    word = random_line(x for x in infile if len(x) == word_length + 1).strip("\n")
    infile.close()
    # For test purposes
    print(word)
    question = shuffle_word(word)
    print("Solve:", question)
    guess_word(word)

# Takes the players guesses and checks them 

def guess_word(word):
    guess = input('Make a guess: ').lower()
           
    if guess == word:

        print("Correct!")
        # Player has guessed correctly so calls funtion to play again
        keep_playing()
        return 

    print ("Incorrect - try again")
    guess_word(word)

# Asks user if they want to play again
        
def keep_playing():
    choice = input("\nContinue? [y/n]: ")
    print('-'*50)
    if choice == 'n':
        print("\nThank you for playing!")
        return
    if choice == 'y':
        initiate_game()
        return
    print ("Enter y or n")
    keep_playing()

initiate_game()
