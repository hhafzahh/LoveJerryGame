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
        operator = choice(['+','-','x','÷'])
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == 'x':
            result = num1 * num2
        else:
            result = num1 / num2
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

# Game Option 2 : Typing Game 
def typingGame():
   credits = 0
   #for now we can have hardcoded string, later create random generated string..
   String = 'I am exponentionally getting tired day by day and workload is directly proportional to tiredness'

   print('Press Enter to start typing or to break a new line')
   print('Please Enter twice to break typing')
   print('=========================================================')
   wordcount = len(String.split())
   print('Enter the sentence:', String)
   print('=========================================================')

   #still working on this part <- need to condition more..
   while True:
       initialTime = time.time()
       inputText = str(input('Enter the sentence:'))
       finaltime = time.time()
       accuracy = len(set(inputText.split()) & set(String.split()))
       #accuracy seems SUS
       accuracy = accuracy/wordcount
       timetaken = finaltime - initialTime
       wpm =(wordcount/timetaken) * 100
       print('-----------------------------------------------------')
       print("WPM",wpm, "Accuracy", accuracy, "Time Taken", timetaken)
       print('-----------------------------------------------------')
       #not conditioned properly, need to include accuracy and time
       if wpm <= 10: 
        print("Your typing is very slow, Learn the proper typing technique and keep practicing")
        print("You have earned an extra 1 credit for trying")
        credits = credits + 1
        return credits
        break
       elif wpm <= 20:
        print("Your typing is slow. Focus on your technique and keep practicing")
        print("You have earned an extra 2 credit for trying")
        credits = credits + 2
        return credits
        break
       elif wpm <= 30:
        print("Better but still below average. Keep practicing to improve you speed and accuracy")
        print("You have earned an extra 3 credit")
        credits = credits + 3
        return credits
        break
       elif wpm <= 40:
        print("You are now an average typist. You still have significant room for improvement")
        print("You have earned an extra 4 credit")
        credits = credits + 4
        return credits
        break  
       elif wpm > 40 and accuracy > 90:
        print("You are doing well")
        print("You have earned an extra 6 credit")
        credits = credits + 6
        return credits
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
      'coding', 'laptop', 'physcics', 'programming', 'mathematics', 'player',
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

#Riddle Game
###### Game Option 4: Number Guessing Game
#Bagel Game, guess 3 numbers and see if you are right

NUM_DIGITS = 2
MAX_GUESS = 10


def getSecretNum():
  #Returns  a string of unique random digits that is NUM_DIGITS long.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(NUM_DIGITS):
    secretNum += str(numbers[i])
  return secretNum



def getClues(guess, secretNum):
#Returns a string with the Pico, \
#Fermi, & Bagels clues to the user.
  if guess == secretNum:
    return 'You got it, boo!'
  
  if guess[0] == secretNum[0] or guess[1] == secretNum[1]:
    return 'Fermi'
  elif guess[0] == secretNum[1] or guess[1] == secretNum[0]:
    return 'Pico'
  else:
    return 'Bagels'
    


def isOnlyDigits(num):
  # Returns True if num is a string of only digits,
  # otherwise returns False
  num_str = str(num)
  if num_str == '':
    return False
  else:
    for i in num_str:
      if i not in '0123456789':
        return False
    return True


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
    print("for troubleshooting", secretNum)
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
        score = score + 1
        return score
        break
      if guessesTaken > MAX_GUESS:
        print('You ran out of guesses. The number was %s' % (secretNum))

    print('Do you want to play again?(yes or no)')
    if not input().lower().startswith('y'):
      break

#If user wants to earn more credits, this function will run
#1. Ask for user input to confirm yes
#2. Ask for Game Type - math or typing
#3. Based on the Game Type, call function, and store the credits into the credits variable
def earnMoreCredits():
    user_input = ''
    while True:
        user_input = input('Do you want to earn more credits? yes/no: ')

        if user_input.lower() == 'yes':
            game_type = input('Cognitive Math or Cognitive Typing? or Word Game? or Guessing Game (math/typing/word/guess):')
            if game_type.lower() == 'math':
                credits = mathquiz()
                print("played", credits)
                return credits
                break
            elif game_type.lower() == 'typing':
                #create function for typing fast
                print("type fast")
                credits = typingGame()
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
