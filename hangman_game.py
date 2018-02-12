# Hangman Game
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    """
    res = False
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            res = True
        else:
            res =False
            break
    return res  

def getGuessedWord(secretWord, lettersGuessed):
    """
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    """
    res = []
    for i in secretWord:
        if i in lettersGuessed:
            res.append(i)
        else:
            res.append('_ ')
    return ''.join(res)  
            
def getAvailableLetters(lettersGuessed):
    '''
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str1='abcdefghijklmnopqrstuvwxyz'
    str1 = list(str1)
    for i in lettersGuessed:
        if i in str1:
            str1.remove(i)
    return ''.join(str1)

def hangman(secretWord):
    '''
    Starts up an interactive game of Hangman.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord) ,"letters long")
    print("-----------")
    l=[]
    mistakesMade = 6
    while mistakesMade > 0 :
        print("You have" , mistakesMade , "guesses left.")
        print("Available letters: " ,end='')
        print(getAvailableLetters(l))
        guess = input("Please guess a letter: ")
        guessinlower = guess.lower()
        if guessinlower in l:
            print("Oops! You've already guessed that letter:" , getGuessedWord(secretWord,l))
        else:
            l.append(guessinlower)
            if guess in secretWord:
                print("Good Guess: " , getGuessedWord(secretWord,l))
                if getGuessedWord(secretWord,l) == secretWord:
                    print("-----------")
                    break
            else:
                mistakesMade -= 1
                print("Oops! That letter is not in my word : " ,getGuessedWord(secretWord,l))
        print("-----------")
    ans = isWordGuessed(secretWord , l)
    if ans == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, You ran out of guesses. The word is ",secretWord)
    return
secretWord = chooseWord(wordlist).lower()
ans = hangman(secretWord)
