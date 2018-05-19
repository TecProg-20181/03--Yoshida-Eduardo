import random
import string
import os
from types import *

WORDLIST_FILENAME = "words.txt"
guesses = 8


def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of stripython letter digitngs
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."

    return wordlist


def isFileTxt():
    if WORDLIST_FILENAME.endswith(".txt"):
        return True
    print "Invalid file extension"
    return False


def isFileEmpty():
    return os.stat(WORDLIST_FILENAME).st_size == 0


def isFileValid():
    if(isFileTxt() and isFileEmpty() is False):
        return True
    return False


def isWordList(wordList):
    if(isinstance(wordList, list)):
        return True
    return False


def checkInput(letter):
    if(len(letter) == 1):
        if(letter.isalpha()):
            return True
    return False


def chooseWord(wordlist, guesses):
    chosenWord = random.choice(wordlist)
    if isWordValid(chosenWord, guesses):
        return chosenWord
    chooseWord(wordlist, guesses)


def isWordValid(word, guesses):
    letter = string.ascii_lowercase
    diffLetters = []
    if(word.isalpha()):
        for letter in word:
            if letter not in diffLetters:
                diffLetters.append(letter)
        if len(diffLetters) > guesses:
            return False
        print 'There are', len(diffLetters), 'different letters'
        return True
    return false


def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    return True


def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    return available


def updateAvailableLetters(availableLetters, lettersGuessed):
    for letter in lettersGuessed:
        availableLetters = availableLetters.replace(letter, '')
    return availableLetters


def checkAvailableLetters(availableLetters):
    if(availableLetters.isalpha()):
        return True
    return False


def isLetterNew(letter, lettersGuessed):
    if(len(letter) == 1):
        if letter in lettersGuessed:
            return False
        return True


def isLetterValid(letter):
    if(letter in string.ascii_lowercase and len(letter) == 1):
        return True
    print "Invalid letter"
    return False


def updateHiddenWord(lettersGuessed, secretWord):
    hiddenWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            hiddenWord += letter
        else:
            hiddenWord += '_'
    return hiddenWord


def start(secretWord):
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'


def hangman(secretWord, guesses):
    start(secretWord)

    lettersGuessed = []
    hiddenWord = updateHiddenWord(lettersGuessed, secretWord)
    availableLetters = getAvailableLetters()

    while isWordGuessed(secretWord, lettersGuessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        print 'Available letters', availableLetters
        letter = raw_input('Please guess a letter: ')
        letter = letter.lower()

        if isLetterValid(letter):
            if isLetterNew(letter, lettersGuessed):
                if letter in secretWord:
                    print 'Good Guess: ',
                    lettersGuessed.append(letter)
                    hiddenWord = updateHiddenWord(lettersGuessed, secretWord)
                    print hiddenWord
                else:
                    guesses -= 1
                    lettersGuessed.append(letter)
                    print 'Oops! That letter is not in my word: ', hiddenWord
            else:
                print 'Oops! You have already guessed that letter:', hiddenWord

        if(checkAvailableLetters(updateAvailableLetters(availableLetters,
                                                        lettersGuessed))):
            availableLetters = updateAvailableLetters(availableLetters,
                                                      lettersGuessed)
        print '------------'

    if isWordGuessed(secretWord, lettersGuessed) is True:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


if(isFileValid()):
    wordlist = loadWords()
else:
    print("Wordlist could not be loaded")
    exit()

secretWord = chooseWord(wordlist, guesses).lower()

hangman(secretWord, guesses)
