import collections

def get_anagrams(word, word_list):
    return [i for i in word_list if collections.Counter(word) == collections.Counter(i)]

with open("Word_list.txt", "r") as word_list:
    anagrams = get_anagrams("retinas", (word.strip("\n") for word in word_list if len(word) == 8))

print("The word to unscramble is: sntiaer")
print(f"There are {len(anagrams)} anagrams to guess")

while anagrams:
    guess = input("Enter a guess: ")
    if guess in anagrams:
        anagrams.remove(guess)
        print(f"Correct, {len(anagrams)} anagrams remain")
        continue
    print("Incorrect")