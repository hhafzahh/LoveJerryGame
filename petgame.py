# Game Purpose to increase Cognitive skills - Math Mental Sum + Type Writing Fast
from random import choice, randint
import random
import time

color_red = "\033[91m"
color_default = "\033[0m"

def convertHealthToBar(pethealth):
    maxhealth = 100
    currenthealth = pethealth
    remaining_health_symbol = "X"
    lost_health_symbol = "_"
    bars = 20
    

    remaining_health_bars = round(currenthealth/maxhealth * bars)
    lost_health_bars = bars - remaining_health_bars

    print('==================================================================')
    print(f"Health of Pet: {currenthealth}/{maxhealth}")
    print(f"|{color_red}{remaining_health_bars * remaining_health_symbol}"
          f"{color_default}{lost_health_bars * lost_health_symbol}|")
    print('==================================================================')

    if currenthealth < 50:
        print("Please take care of the pet. The health of pet is decreasing as it is not being fed and take care of!")
    print('----------------------------------------------------------------------------------------------------------')

# for now we can have math quiz to only include product..
def mathquiz():
    
    print('Enjoy a math quiz, and respond with nothing to stop.')
    num_right = 0
    num_wrong = 0
    total_right_answer_seconds = 0.0

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
        try:  # `int` may fail
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


# type fast
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

#Riddle Game





def earnMoreCredits():
    user_input = ''
    while True:
        user_input = input('Do you want to earn more credits? yes/no: ')

        if user_input.lower() == 'yes':
            game_type = input('Cognitive Math or Cognitive Typing? (math/tying):' )
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
            else:
                print("invalid")
        elif user_input.lower() == 'no':
            print('User typed no')
            break
        else:
            print('Type yes/no')


def startgame():
    credits = random.randint(1, 20)
    health = random.randint(1, 90)
    while health > 0:
        convertHealthToBar(health)
        #please enter to see the options
        print("Press enter to see the options availabe")
        print(" 1. Show Credits \n 2. Earn more Credits \n 3. See Pet Health \n 4. Feed the Cat \n 5. Quit")
        menuSelectedOption = int(input("Pick an option (1-5):      "))
        if menuSelectedOption == 1:
            print("Credits Attained: " , credits)
        elif menuSelectedOption == 2:
            earningNew = earnMoreCredits()
            print("testing", earningNew)
            credits = credits + earningNew
            print("Total Credits", credits)

        elif menuSelectedOption == 3:
            print("Health of Pet:" , health )

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
