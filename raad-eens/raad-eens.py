#Alwin Wezenbeek 99060433
#guessing numbers
#20 rounds
#you can guess 10 times each round
#keep score 1 point for each guessed number to a max of 20 points
#say the score after each round
#ask the user to keep playing after each round
#if the guessed number is closer than 50 numbers say: 'you're getting warmer' 
#if the number is closer than 20 say:'you're almost burning alive'
#if the guessed number is further than 50 numbers say: 'you're on room temperature'
#if the guessed number is further than 100 numbers say: 'you're cold'
#if the guessed number is further than 200 numbers say: 'you're freezing'
#after 20 rounds announce the score

#-------Imports-------
import random

#-------Variables-------
rounds = 20
random_number = random.randint(0, 10)
guesses = 10
score = 0

#-------Start-Message------
print('''you're about to guess a number between 1 and 1000
there are 20 rounds and you can guess a number 10 times each round
for every guessed number you get 1 point to a max of 20 points
Good Luck...''')

while guesses != random_number:
    guesses = 10
    guess = int(input('guess a number between 1 and 1000: '))
    guesses -= 1
    if guess <= random_number:
        print('number is higher')
    if guess >= random_number:
        print('number is lower')
    if guess == random_number:
        score += 1
        print('you guessed it')
        print ('you have'' ' + str(score) + ' ''points')
    if guesses >= 0:
        print('you did not guess it')

