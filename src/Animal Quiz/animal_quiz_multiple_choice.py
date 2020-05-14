# Declare variables
score = 0


# Declare functions
def check_guess(guess, answer):
    global score
    if guess.lower() == answer.lower():
        score = score + 1


# Application
print('Geography!')
print('----------\n')
guess1 = input('Which of these countries has the largest population?\n \
A) Brazil\n B) Iran\n C) Russia\n D) Germany\n Input A, B, C, D\n')
check_guess(guess1, 'A')
print('\n')

guess2 = input('Which of these mountain ranges has the higest maximum elevation?\n \
A) Rockies\n B) Alps\n C) Andes\n D) Urals\n Input A, B, C, D\n')
check_guess(guess2, 'C')

guess3 = input('Which of these rivers flows past the most countries?\n \
A) Euphrates\n B) Amazon\n C) Danube\n D) Mississippi\n Input A, B, C, D\n')
check_guess(guess3, 'C')

guess4 = input('Which of these cities has the highest population?\n \
A) Singapore\n B) Shanghai\n C) San Francisco\n D) Santiago\n Input A, B, C, D\n')
check_guess(guess4, 'B')

guess5 = input('Which of these islands has the largest area?\n \
A) Cuba\n B) Madagascar\n C) Iceland\n D) Great Britain\n Input A, B, C, D\n')
check_guess(guess5, 'B')

guess6 = input('Which of these capital cities gets the most rain?\n \
A) Kuala Lumpur\n B) Wellington\n C) Washington DC\n D) Mexico City\n Input A, B, C, D\n')
check_guess(guess6, 'A')

guess7 = input('Which of these US states has the largest area?\n \
A) Florida\n B) Nebraska\n C) New York\n D) California\n Input A, B, C, D\n')
check_guess(guess7, 'D')

guess8 = input('Which of these cities is at the highest altitude?\n \
 A) New York\n B) London\n C) Beijing\n D) Paris\n Input A, B, C, D\n')
check_guess(guess8, 'B')

guess9 = input('Which of these bodies of water has the largest surface area?\n \
A) Red Sea\n B) Black Sea\n C) Persian Gulf\n D) Gulf of Mexico\n Input A, B, C, D\n')
check_guess(guess9, 'D')

guess10 = input('Which of these cities has the most air pollution?\n \
 A) Delhi\n B) Tokyo\n C) Los Angeles\n D) Rome\n Input A, B, C, D\n')
check_guess(guess10, 'A')

guess11 = input('Which of these countries borders the most other countries?\n \
A) Vietnam\n B) Germany\n C) Egypt\n D) United States\n Input A, B, C, D\n')
check_guess(guess11, 'B')

guess12 = input('Which of these countries has the highest percentage of Catholics?\n \
A) Poland\n B) Germany\n C) Cuba\n D) South Korea\n Input A, B, C, D\n')
check_guess(guess12, 'A')

guess13 = input('Which of these countries has the highest GDP per capita?\n \
A) China\n B) Switzerland\n C) Egypt\n D) Spain\n Input A, B, C, D\n')
check_guess(guess13, 'B')

guess14 = input('Which of these countries has the highest fertility rate?\n \
 A) India\n B) Mexico\n C) Tanzania\n D) Canada\n Input A, B, C, D\n')
check_guess(guess14, 'C')

guess15 = input('Which of these countries has the highest life expectancy?\n \
A) Argentina\n B) United Kingdom\n C) Philippines\n D) Japan\n Input A, B, C, D\n')
check_guess(guess15, 'D')


print('Your score is ' + str(score))


