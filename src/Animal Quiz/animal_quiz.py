# Declare variables
score = 0


# Declare functions
def check_guess(guess, answer):
    global score
    if guess.lower() == answer.lower():
        print('Correct Answer')
        score = score + 1


# Application
print('Guess The Animal!')
guess1 = input('Which bear lives at the North Pole? ')
check_guess(guess1, 'polar bear')
guess2 = input('Which is the fastest land animal? ')
check_guess(guess2, 'cheetah')
guess3 = input('Which is the largest animal? ')
check_guess(guess3, 'blue whale')

print('Your score is ' + str(score))


