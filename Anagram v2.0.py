import random
import collections

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

# Asks the player for number of letters in the anagram

def get_word_length():
    
    word_length = input ('How many letters do you want? (3-8) ')
    if not word_length.isdigit():
        print ("Please enter a number from 3-8 " )
        return get_word_length()
    word_length = int(word_length)
    if not 2 < word_length < 9 :
        print ("Invalid number")
        return get_word_length()
    
    return word_length

# Finds all anagrams of the word in the text file

def get_anagrams(word, word_list):
    return [i for i in word_list if collections.Counter(word) == collections.Counter(i)]
   
# Main game function    

def initiate_game():
    word_length = get_word_length()
    infile = open("Word_list.txt","r")
    # Gets the random word of the input length and strips the new line
    word = random_line(x for x in infile if len(x) == word_length + 1).strip("\n")
    infile.close()
    question = shuffle_word(word)
    print ("The word to unscramble is: ", question)
    # Calls the get_anagrams function to make a list of all the anagrams
    with open("Word_list.txt", "r") as word_list:
        anagrams = get_anagrams(word, (word.strip("\n") for word in word_list if len(word) == word_length + 1))
        
        # Prints the list of anagrams for testing purposes
        print (anagrams)
    print (f"There are {len(anagrams)} anagrams to guess")

#Keeps going while anagrams still remain in the list of anagrams made above. Also provides a count of the anagrams remaining

    while anagrams:
        guess = input("Enter a guess: ")
        if guess in anagrams:
            anagrams.remove(guess)
            print(f"Correct, {len(anagrams)} anagrams remain")
            continue
        print("Incorrect - try again")
    keep_playing()
    return
    
        

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
