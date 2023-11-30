# Game Purpose to increase Cognitive skills - Math Mental Sum + Type Writing Fast
# Text Based Game
from random import choice, randint
import random
import time

color_red = "\033[91m"
color_default = "\033[0m"

#To show the health of the pet in progress bar visual
#Total Health = 100%
#The parameter is based on the value in the startgame()
def convertHealthToBar(pethealth):
    maxhealth = 100
    currenthealth = pethealth

    #I cant find the shaded symbol
    remaining_health_symbol = "X"
    lost_health_symbol = "_"
    bars = 20
    
    #no of remaining health bars = currenthealth/100 * 20
    remaining_health_bars = round(currenthealth/maxhealth * bars)
    lost_health_bars = bars - remaining_health_bars

    print('==================================================================')
    print(f"Health of Pet: {currenthealth}/{maxhealth}")
    print(f"|{color_red}{remaining_health_bars * remaining_health_symbol}"
          f"{color_default}{lost_health_bars * lost_health_symbol}|")
    print('==================================================================')

    #give warning reminder if pet health is lower than 50
    if currenthealth < 50:
        print("Please take care of the pet. The health of pet is decreasing as it is not being fed and take care of!")
    print('----------------------------------------------------------------------------------------------------------')

# Game Option 1 : Math Quiz
def mathquiz():
    
    print('Enjoy a math quiz, and respond with nothing to stop.')
    num_right = 0
    num_wrong = 0
    total_right_answer_seconds = 0.0

    # A simple math quiz with numbers with small numbers
    # 1. Take 2 random numbers & 1 random operator
    # 2. Set the correct value as result
    # 3. Condition : If input by user != correct value, then print according
    # 4. It notes the time taken too <- ask group mates if we want to condition time interval such that longer time -> considered decrease of 1 credit etc.
    while True:
        num1 = randint(2, 9)
        num2 = randint(2, 11)
        operator = choice(['+','-','x'])
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        else:
            result = num1 * num2

        start_time = time.time()
        response = input(f'What is {num1} {operator} {num2}? ')
        if not response:
            break
        elapsed = time.time() - start_time
        try: 
            if int(response) == result:
                print(f'Right, in {elapsed:.2f} seconds')
                num_right += 1
                total_right_answer_seconds += elapsed
            else:
                print(f'Wrong, the answer was {result}')
                num_wrong += 1
        except ValueError:
            print('You entered something other than an integer')

    print(f'You got {num_right} right and {num_wrong} wrong.')
    difference  = num_right - num_wrong
    print("difference", difference)
    return difference

##########################################################################
# Game Option 2 : Color Text Game Quiz
colours = [
    'GREY','RED','GREEN', 'BROWN','BLUE','PURPLE','CYAN','BLACK'
]
score = 0

# ANSI escape codes for colored text
color_codes = {
  'GREY': "\033[0;30m",
  'RED': "\033[0;31m",
  'GREEN': "\033[0;32m",
  'BROWN': "\033[0;33m",
  'BLUE': "\033[0;34m",
  'PURPLE': "\033[0;35m",
  'CYAN': "\033[0;36m",
  'BLACK': "\033[0;37m",
}

def startColorGame():

  time_limit = 15
  start_time = time.time()
  
  global score
  while True:

    #check if time limit is reached 
    elapsed_time = time.time() - start_time
    remaining_time = max(0, time_limit - elapsed_time)

    if remaining_time <= 0:
        print("Time's up! Game over.")
        break
    # Your game logic goes here
    print(f"Remaining Time: {int(remaining_time)} seconds")

    # Simulate some game actions
    print("Type in the color of the words, not the word text!")
    print(f"Current Score: {score}")

    random.shuffle(colours)
    color = colours[0]
    word = colours[1]

    print(f"The color is: {color_codes[color]}{word}\033[0m")

    user_input = input("Type the color: ").lower()

    if user_input.lower() == color.lower():
      score += 1
    print(f"Current Score: {score}")
    print(f"CORRECT COLOR: {color}")
    print("\n")

    c = int(input("press 1 to continue and 0 to quit :"))

    #once user quits, score will be returned as credits earned
    if c == 0:
      print(score)
      return score
      break

print("Color Fast Text Game in 15s")
print("Press enter to start")
def colorTextGame():
  while True:
    user_start = int(input("press 1 to start and 0 to quit :"))
    if user_start == 1:
      startColorGame()
    else:
      break


###### Game Option 3: Word Scramble Game
#1. Choose a random word from the words list
#2. Jumble the characters of that word
#3. Ask user for input of the unscrambled word
#4. If userinput = random word selected, then credit added 1 

# function for choosing random word.
def choose():
  # list of word
  words = [
      'coding', 'laptop', 'physics', 'programming', 'mathematics', 'player',
      'game', 'reverse', 'water', 'board', 'smart'
  ]

  #pick is a random word from the list
  pick = random.choice(words)


  return pick


#function to jumble/shuffle the letters of the word
def jumble(word):
  # sample() method shuffling the characters of the word
  random_word = random.sample(word, len(word))

  # join() method join the elements of the iterator(e.g. list) with particular character .
  jumbled = ''.join(random_word)
  return jumbled


# Function for playing the game.
def wordScrambleGame():

  # set initial score as 0
  score = 0

  # keep looping
  while True:

    #choose a random word
    picked_word = choose()

    #jumble the word
    jumble_word = jumble(picked_word)
    print("jumbled word is :", jumble_word)

    #ask user for input
    ans = input("what is in your mind? ")

    # checking ans is equal to picked_word or not
    if ans == picked_word:

      # score increment by 1 when user answer correctly
      score += 1
      print("Correct Answer")
    else:
      print("Better luck next time...correct word is :", picked_word)

    c = int(input("press 1 to continue and 0 to quit :"))

    #once user quits, score will be returned as credits earned
    if c == 0:
      print(score)
      return score
      break

###### Game Option 4: Number Guessing Game
#Bagel Game, guess 2 numbers and see if you are right
NUM_DIGITS = 2
MAX_GUESS = 10
# 1. Get a list of 1-9
# 2. Shuffle the numbers
# 3. Set secretNumber as string and add each digit into the string
# 4. Return Secret Number
def getSecretNum():
  #Returns  a string of unique random digits that is NUM_DIGITS long.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(NUM_DIGITS):
    secretNum += str(numbers[i])
  return secretNum


#Get Clues based on the input of the user and the secretNumber generated by the computer
#If input number by user equals to the secretNum then, return 'You got it'
#Else if first number of the user is  equal to firstnumber of secretNum but not equal for secondNum or vies versa, then return 'Fermi'
#Else if first number of the user is in the correct position and correct value or the second is in the correct, then return 'Pico'
#Else return 'Bagels'

#Can have more clues here

def getClues(guess, secretNum):
  if guess == secretNum:
    return 'You got it, boo!'
  if guess[0] == secretNum[0] or guess[1] == secretNum[1]:
    return 'Fermi'
  elif guess[0] == secretNum[1] or guess[1] == secretNum[0]:
    return 'Pico'
  else:
    return 'Bagels'
  

# Returns True if num is a string of only digits,
# otherwise returns False
def isOnlyDigits(num):
  num_str = str(num)
  if num_str == '':
    return False
  else:
    for i in num_str:
      if i not in '0123456789':
        return False
    return True

#Define GuessingGame:
# 1. Set Score = 0 
# 2. Set the rules and questions
# 3. Get a Secret Number first
# 4. While no.of guesses taken is less than maximum number of guesses, then set guess to empty string
# 5. While input is not equal to the length of numbers required or value is not digits, then set guess to input again
# 6. Call the Clues function to check if it matches entirely or slightly and return the necessary clues to help the user, Increase GuessTaken by 1 
# 7.  If it matches, score increment by 4, and break the game
# 8. Ask user if he/she wishes to play again

def guessingGame():
  score = 0
  print('I am thinking of a %s-digit number. Try to guess what it is!' %
        (NUM_DIGITS))
  print('''
      The clues I give are...
      ------------------------------------------------------------
      When I say:  |That means:
      ------------------------------------------------------------
      Bagels       |None of the digits is correct.
      ------------------------------------------------------------
      Pico         |One digit is correct but in the wrong position.
      ------------------------------------------------------------
      Fermi        |One digit is correct and in the right position
      ------------------------------------------------------------
    ''')
  
  while True:
    secretNum = getSecretNum()

    print('I have thought up a number. You have %s guesses to get it' %
          (MAX_GUESS))
    guessesTaken = 1

    while guessesTaken <= MAX_GUESS:
      guess = ''

      while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
        print('Guess %s: ' % (guessesTaken))
        guess = input()

      print(getClues(guess, secretNum))
      guessesTaken += 1

      if guess == secretNum:
        score = score + 4
        return score
        break
      
      if guessesTaken > MAX_GUESS:
        print('You ran out of guesses. The number was %s' % (secretNum))

    print('Do you want to play again?(yes or no)')
    if not input().lower().startswith('y'):
      break


###### Game Option 5: Color Mental Game


#If user wants to earn more credits, this function will run
#1. Ask for user input to confirm yes
#2. Ask for Game Type - math or colorText or word or guess
#3. Based on the Game Type, call function, and store the credits into the credits variable
def earnMoreCredits():
    user_input = ''
    while True:
        user_input = input('Do you want to earn more credits? yes/no: ')

        if user_input.lower() == 'yes':
            game_type = input('Math or ColorText or Word or Guess Game? (math/colortext/word/guess):')
            if game_type.lower() == 'math':
                credits = mathquiz()
                print("played", credits)
                return credits
                break
            elif game_type.lower() == 'colortext':
                print("Color Text")
                credits = colorTextGame()
                print("typed & earned: ", credits)
                return credits
                break
            elif game_type.lower() == 'word':
               print("Word Scramble Game")
               credits = wordScrambleGame()
               print("Earned Credits:" , credits)
               return credits 
               break
            elif game_type.lower() == 'guess':
                print("Guessing Game")
                credits = guessingGame()
                print("Earned Credits:", credits)
                return credits
                break
            else:
                print("invalid")
        elif user_input.lower() == 'no':
            print('User typed no')
            break
        else:
            print('Type yes/no')


#Main Function to start game
#Have a random value of credits and health of pet
def startgame():
    credits = random.randint(1, 20)
    health = random.randint(1, 90)
    while health > 0:

        #Show pet health bar
        convertHealthToBar(health)

        #Ask user for input of which options they want to enter
        print("Press enter to see the options availabe")
        print('''  
                    1. Show Credits \n 
                    2. Earn more Credits \n
                    3. See Pet Health \n 
                    4. Feed the Cat \n 
                    5. Quit
              ''')
        
        menuSelectedOption = int(input("Pick an option (1-5):      "))
        #If Option 1, print the value of credits variable
        if menuSelectedOption == 1:
            print("Credits Attained: " , credits)
        
        #If Option 2, Add credits to initial credits variable and print the final credits
        elif menuSelectedOption == 2:
            earningNew = earnMoreCredits()
            print("testing", earningNew)
            credits = credits + earningNew
            print("Total Credits", credits)

        #If Option 3, Show health of pet <-- might want to remove
        elif menuSelectedOption == 3:
            print("Health of Pet:" , health )

        #If Option 4, Feed the Pet
        #Choice of food : Fish (4 credits to buy) , Water (2 credits to buy)
        #If enough credits, immediately deduct,else prompt to choose option 2 to earn more credits
        # Once pet is fed, health increases based on the choice of food [fish - increase by 10 , water - increase by 2 ]
        elif menuSelectedOption == 4: 
            totalCred_fish = 4
            totalCred_water = 2
            user_input = input('Do you want to buy fish or water? (fish/water):')
            if user_input.lower() == 'fish':
                if credits >= totalCred_fish:
                    credits -= totalCred_fish
                    health += 10 # increase petheath by 10 when fed
                    print('You fed the cat. Pet health increased by 10.')
                else:
                    print('Not enough credits to feed the cat')
            elif user_input.lower() == 'water':
                if credits >= totalCred_water: 
                    credits -= totalCred_water
                    health += 2 #increase pethealth by 2 when fed

            else:
                print("invalid input")
        elif(menuSelectedOption == 5):
            print('Quit Program')
            break
        else: 
            print('Invalid choice. Please enter 1-5')



startgame()


# convert the above into tkinter.
