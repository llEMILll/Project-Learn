#random module
from random import randint
#menu
print('=================================')
print('Rock Paper Scissors Lizard Spock')
print('=================================')
print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')
#options List
options=['✊', '✋','✌️','🦎','🖖']
#Loop
while True:
    #Loop
    while True:
        #handle user input errors
        try:
            player=int(input('Pick a number: '))
            if 1 <= player <= 5:
                break  
            else:
                print('¡Invalid number! Please choose between 1, 2, 3, 4 or 5.')
        except ValueError:
            print('Invalid entry! Please enter a number.')
    #randint() function of the "random" module
    computer=randint(0,4)
    #variables
    player = options[player-1]
    computer = options[computer]
    #Print variables
    print('You chose: ', player)
    print('CPU chose: ', computer)
    #if-else control flow
    if player == computer:
        print('It is a tie!')
    elif (player == '✌️' and computer == '✋'):
        print('The player won!')
    elif (player == '✋' and computer == '✊'):
        print('The player won!')
    elif (player == '✊' and computer == '🦎'):
        print('The player won!')
    elif (player == '🦎' and computer == '🖖'):
        print('The player won!')
    elif (player == '🖖' and computer == '✌️'):
        print('The player won!')
    elif (player == '✌️' and computer == '🦎'):
        print('The player won!')
    elif (player == '🦎' and computer == '✋'):
        print('The player won!')
    elif (player == '✋' and computer == '🖖'):
        print('The player won!')
    elif (player == '🖖' and computer == '✊'):
        print('The player won!')
    elif (player == '✊' and computer == '✌️'): 
        print('The player won!')
    else:
        print('The cpu won!')
    #loop control
    quest=input('Pres *Y* to continue or *N* for exit: ') 
    quest= quest.upper()
    if quest == 'N':
        break




