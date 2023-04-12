import random   #library used for random number generation
max_value_string = input('choose your limit: you want to guess a number between 1 and ')
max_value = 0
while True:
    if max_value_string.isnumeric():
        max_value = int(max_value_string)
        break
    else:
        print('thats not a number')
        max_value_string = input('choose your limit: you want to guess a number between 1 and ')
while True:  #custom workaround for 'do while' because there is no 'do while' in python
    if max_value <= 1:
        print('you must choose a number greater than 1')
        max_value = int(input('you want to guess a number between 1 and '))  #re-asks the question
    if 1 < max_value:
        break  #stops the loop when a value greater than 1 is chosen
print('answer "0" to change your limits (this can be used anytime, but will reset your stats)')
x = random.randint(0,max_value)  #program generates number between 0 and 100
wins = 0
guesses = 0  #baseline needs to be set to later add to
totGuesses = 0
avgGuesses = 0

while True:  #loop keeps playing until the correct number has been guessed
    y_string = input('try to guess the number ')  #taking a number from the user as a string
    while not y_string.isnumeric():
        print('thats not a number')
        y_string = input('try to guess the number ')
    y = int(y_string)
    guesses = guesses + 1  #each guess, the guess counter goes up by 1
    difference = abs(x-y)  #measuring how far the users input was from the wanted number
    if y == -0:
        print('debug mode activated, the number was ' + str(x))  #activates debug mode
        keep_limit = int(input('your current limit is ' + str(max_value) + ': press 1 to keep, press 0 to change '))  # asks if the user wants to change the limit
        while True:  # custom workaround for 'do while' because there is no 'do while' in python
            if keep_limit == 1:
                break
            elif keep_limit == 0:
                max_value = int(input('choose your new limit: you want to guess a number between 1 and '))
                break
            else:
                print('you can only answer 0 or 1')
                keep_limit = int(
                    input('your current limit is ' + str(max_value) + ': press 1 to keep, press 0 to change '))
        wins = 0  #resets win counter
        totGuesses = 0
        avgGuesses = 0
        print('win counter has been reset')
        x = random.randint(1, max_value)  #a new number is generated
        print('a new number has been chosen')
    elif y < 0:
        print('you cannot choose a number that is less than zero')
    elif max_value < y: #message if the user goes over their chosen limit
        print('you cannot choose any number greater than ' + str(max_value))  #informs user that they exceeded their chosen limit
    elif difference == 0:
        print('you guessed it, the number was ' + str(x))  #inserting the value of x as a string
        x = random.randint(1, max_value)
        wins = wins + 1
        totGuesses = totGuesses + guesses
        avgGuesses = totGuesses / wins
        print('amount of guesses: ' + str(guesses))
        print('win counter: ' + str(wins))  #displays the amount of times you guessed right
        print('average guesses per game: ' + str(avgGuesses))
        guesses = 0  #guess counter resets
        print('a new number has been chosen')  #because the previous number has been found, a new number is generated

    elif 0 < difference <= 2:
        print('extremely close')
    elif 2 < difference <= (max_value/20):
        print('pretty close')
    elif (max_value/20) < difference <= (max_value/5):
        print('kinda close')
    elif (max_value/5) < difference <= (max_value/2):  #checks if you are between 1/5th and half the max amount of numbers away from the right answer
        print('not very close')
    elif (max_value/2) < difference <= max_value:
        print('way off')
    else:  #this shouldn't be able to happen, only here for debug purposes
        print('if you see this that means something went wrong') 
        print(x)  #shows the number you were looking for
