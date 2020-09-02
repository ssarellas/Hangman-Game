#hangman game

import random

userGuessList = []
userGuesses = []
playGame = True
category = ''
continueGame = 'Y'

print('Hello there and welcome to hangman! What is your name?')
name = input()
print('Hello', name,'! Let\'s get started. The objective of the game is to guess the word the computer is \
thinking of and you can only guess one letter at a time. What category do you want? Put B for breakfast \
foods, D for desserts or X to exit.')
category = input()
while True:
    while True:
        if category.upper() == 'B':
            option = ['OMLETTE','FRENCHTOAST', 'CEREAL', 'WAFFLES', 'PANCAKES']
            secretWord = option[random.randint(0,4)]
            break
        elif category.upper() == 'D':
            option = ['PASTRIES', 'CUPCAKES', 'PUDDING', 'ICECREAM', 'BROWNIES']
            secretWord = option[random.randint(0,4)]
            break
        else:
            category = input('Please select a valid category of B for Breakfast foods or D for dessert.\n')

        if category.upper() == 'X':
            print('Goodbye!')
            playGame = False
            break
    if playGame:
        attempts = len(secretWord) + 2
        def printGuessedLetter():
            print('Your secret word is:' + ''.join(userGuessList))
        for n in secretWord:
            userGuessList.append('_ ')
        printGuessedLetter()
        print('the number of guesses you have for this word is', attempts)
        while True:
            print('Guess a letter:')
            letter = input()
            if letter.upper() in userGuesses:
                print('You have alreasy guessed this letter, try again.')
            else:
                attempts -= 1
                userGuesses.append(letter.upper())
                if letter.upper() in secretWord:
                    print('Good guess!')
                    if attempts > 0:
                        print('You have', attempts,'guesses remaining!')
                    for i in range(len(secretWord)):
                        if letter.upper() == secretWord[i]:
                            letterIndex = i
                            userGuessList[letterIndex] = letter.upper()
                    printGuessedLetter()
                else:
                    print('Try again.')
                    if attempts > 0:
                        print('You have', attempts,'guesses remaining!')
                        printGuessedLetter()
            joinedList = ''.join(userGuessList)
            if joinedList.upper() == secretWord.upper():
                print('Congrats! You won!')
                break
            elif attempts == 0:
                print('You ran out of guesses! Better luck next time.')
                print('The word was:', secretWord.upper())
                break
        continueGame = input('Do you want to play again? Hit Y to continue, or any other key to quit.   ')
        if continueGame.upper() == 'Y':
            category = input('Please select a valid categary: B for breakfast foods or D for desserts.\n')
            userGuessList = []
            userGuesses = []
            playGame = True
        else:
            print('Thanks for playing!')
            break
    else:
        break
    


    

