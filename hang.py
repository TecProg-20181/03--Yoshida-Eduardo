import random
import string

WORDLIST_FILENAME = "words.txt"
GUESSES = 8


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print 'Loading word list from file...'
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    # secretLetters = []
    # for letter in secretWord:
    #    if letter in secretLetters:
    #        secretLetters.append(letter)
    #    else:
    #        pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True


def getGuessedWord():

    guessed = ''
    return guessed


def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    return available


def updateAvailableLetters(available, lettersGuessed):
    for letter in lettersGuessed:
        available = available.replace(letter, '')
    return available


def isLetterValid(letter, lettersGuessed):
    if letter in lettersGuessed:
        return False
    return True


def printHiddenWord(lettersGuessed, secretWord):
    hiddenWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            hiddenWord += letter
        else:
            hiddenWord += '_'
    print hiddenWord


def hangman(secretWord):

    lettersGuessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    while isWordGuessed(secretWord, lettersGuessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        available = getAvailableLetters()

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')

        if isLetterValid(letter, lettersGuessed) is True:
            if letter in secretWord:
                print 'Good Guess: ',
                lettersGuessed.append(letter)
            else:
                guesses -= 1
                lettersGuessed.append(letter)
                print 'Oops! That letter is not in my word: ',
        else:
            print 'Oops! You have already guessed that letter: ',

        available = updateAvailableLetters(available, lettersGuessed)
        printHiddenWord(lettersGuessed, secretWord)
        print '------------'

    if isWordGuessed(secretWord, lettersGuessed) is True:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


secretWord = loadWords().lower()
hangman(secretWord)
