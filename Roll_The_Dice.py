#The Dice Game
#Roll the Dice

import random
        
#Created a function called rollDie   
def rollDice():
    
#Created a variable for the repeat game loop
    cRepeat = False
    
#Repeat game while loop
    while cRepeat != True:
        
#Variables' for the while loop which generates the random numbers
        i = 0
        nOutput = 0
        totalDie = 0

#User input is put into 2 variables 
        nDie = input('Number of die? ')     #User input for number of die
        nSide = input('Numbrt of sides? ')  #User input for number of sides the die will have

#While loop to insure that the die does not have improbable sides
        while int(nSide) < 3:
            if int(nSide) < 3:
                nSide = input('Sides cannat be less than 3. Please insert a new number of sides :')
            else:
                break                       #It stops the loop from repeating once the input has met the requirements

#A while loop that generates random integers for the amount of die chosen and also calculates the collective amount
        while i < int(nDie):
            nOutput = random.randint(1,int(nSide))
            print('Die ',i+1,': ',nOutput)
            totalDie += nOutput
            i += 1

#Unnecessary text outputs to make the layout look nice
#Aswell as asks user whether the program should be repeated        
        print('')
        print('You rolled a: ',totalDie)
        print('')
        userReplay = input('''Do you wish to repeat?
Y/y or N/n: ''')
        print('')

#Validation of the yes and the no on repeating the simulation or not
        if userReplay.upper() == 'Y':
            break
        elif userReplay.upper() == 'N':
            continue
        else:
            print('Error...')
            print('')
            break
    input('press ENTER...')

rollDice()
