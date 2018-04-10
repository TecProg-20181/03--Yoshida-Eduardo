import random
import string

WORDLIST_FILENAME = "words.txt"


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
    return wordlist


def chooseWord(wordlist, guesses):
    chosenWord = random.choice(wordlist)
    if isWordValid(chosenWord, guesses):
        return chosenWord
    chooseWord(wordlist, guesses)


def isWordValid(word, guesses):
    letter = string.ascii_lowercase
    diffLetters = []
    for letter in word:
        if letter not in diffLetters:
            diffLetters.append(letter)
    if len(diffLetters) > guesses:
        return False
    print 'There are', len(diffLetters), 'different letters'
    return True


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


def isLetterValid(letter, lettersGuessed):
    if letter in lettersGuessed:
        return False
    return True


def updateHiddenWord(lettersGuessed, secretWord):
    hiddenWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            hiddenWord += letter
        else:
            hiddenWord += '_'
    return hiddenWord


def hangman(secretWord):
    guesses = 8
    lettersGuessed = []

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    hiddenWord = updateHiddenWord(lettersGuessed, secretWord)
    availableLetters = getAvailableLetters()

    while isWordGuessed(secretWord, lettersGuessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        print 'Available letters', availableLetters
        letter = raw_input('Please guess a letter: ')

        if isLetterValid(letter, lettersGuessed) is True:
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
            print 'Oops! You have already guessed that letter: ', hiddenWord

        availableLetters = updateAvailableLetters(availableLetters, lettersGuessed)
        print '------------'

    if isWordGuessed(secretWord, lettersGuessed) is True:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


wordlist = loadWords()
secretWord = chooseWord(wordlist, 8).lower()
hangman(secretWord)
