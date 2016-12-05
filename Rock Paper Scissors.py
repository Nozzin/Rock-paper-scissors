import random
import sys
import time

def main():
    yes = 0
    computerW = 0
    playerW = 0
    
    while yes == 0:
        
        yes_no = input('Do you want to play? yes or no? ')
        
        if yes_no == ('yes' or 'Yes'):
            player = player_choice()
            computer = computer_choice()
            print('Rock!')
            time.sleep(.5)
            
            print('Paper!')
            time.sleep(.5)
            
            print('Scissors!')
            time.sleep(.5)
            
            print('Shoot!')
            time.sleep(.5)
            
            print('I have chosen',computer,'!')
            time.sleep(.5)
            
            print('You chose',player,'.')
            time.sleep(.5)
            
            if player == ("rock" or "Rock"):
                if computer == ('rock'):
                    print('Damn. A tie! Your good.')
                    time.sleep(1)
                if computer == ('paper'):
                    print('MUHAHAHA. None can beat a computer you fool.')
                    time.sleep(1)
                    computerW += 1
                if computer == ('scissors'):
                    print('Pft. I let you win that one.')
                    time.sleep(1)
                    playerW += 1
                    
            if player == ("paper" or "Paper"):
                if computer == ('paper'):
                    print('Damn. A tie! Your good.')
                    time.sleep(1)
                if computer == ('scissors'):
                    print('MUHAHAHA. None can beat a computer you fool.')
                    time.sleep(1)
                    computerW += 1
                if computer == ('rock'):
                    print('Pft. I let you win that one.')
                    time.sleep(1)
                    playerW += 1
                    
            if player == ("scissors" or "Scissors"):
                if computer == ('scissors'):
                    print('Damn. A tie! Your good.')
                    time.sleep(1)
                if computer == ('rock'):
                    print('MUHAHAHA. None can beat a computer you fool.')
                    time.sleep(1)
                    computerW += 1
                if computer == ('paper'):
                    print('Pft. I let you win that one.')
                    time.sleep(1)
                    playerW += 1
                    
            print('Computer:',computerW)
            print('Player:',playerW)
                    
            
        elif yes_no == ('no' or 'No'):
            sys.exit()
            
        else:
            print('That wasnt a yes or no.')
            sys.exit()
        
        

def player_choice():
    choice = str(input("Would you like to pick rock? paper? or scissors? "))
    if choice == ('rock'):
        return choice
    if choice == ('Rock'):
        return choice
    if choice == ('paper'):
        return choice
    if choice == ('Paper'):
        return choice
    if choice == ('scissors'):
        return choice
    if choice == ('Scissors'):
        return choice
    else:
        print('Thats not a choice')
        player_choice()

def computer_choice():
    choice = random.randint(0,2)
    if choice == 0:
        choice = 'rock'
    elif choice == 1:
        choice = 'paper'
    elif choice == 2:
        choice = 'scissors'
    return choice
    

main()
