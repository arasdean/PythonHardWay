import random
secretNumber = random.randint(1,20) #random integer between 1 and 20
print('I am thinking of a number between 1 and 20')# this literally prints some random ish

#ask the player to guess in six times

for guessesTaken in range(1,7): #var guessesTaken up to 6
    print ('Take a guess.')
    guess = int(input()) #user raw input becomes integer

    if guess < secretNumber: # following flow controls where secretNumber = randint
        print("Your guess is too low")
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break
if guess == secretNumber: #secretNumber is the randomint
    print('Good job! You guessed my number in %s guesses') % (str(guessesTaken))
else:
    print("Nope. The number I was thinking of was %s") % (str(secretNumber))
