from re import A
import random
from tkinter import W
from tokenize import Name

def coinFlip():
    if random.randrange(2)==0:
      return 'HEAD'
    return 'TAILS'

check = 0 

while check == 0:
    protaganist = input('Welcome to Aether World, here you will live a story in a skin of our protagonist: \nBALDUN or MAYA: ')
    protaganist = protaganist.upper()    
    if protaganist == 'MAYA':
            print('\nMaya Welcome to Aether World, now you will be introduced to a story')
            check =+ 1
    elif protaganist == 'BALDUN':
            print('\nBaldun Welcome to Aether World, now you will be introduced to a story')  
            check =+ 1
    else:
            print(f'\nenter the name of one of the protagonists above the protagonist {protaganist} is not valid')
            check =+ 0
check2 = 0
while check2 == 0:
    firstOption = input(f'\n{protaganist} You are relaxing in a tavern thinking when will appear a new job to a mercenary like you \nWhen a known from a local guild calls you he talk to you about two jobs \nA quest to rescue a chest sent to the king And A quest to deliver a sealed letter from a local thane to the king of the kingdom of regnar \nChoose your quest KING or THANE: ')
    firstOption = firstOption.upper()
    if firstOption == 'KING':
                print('\nknown says:Ok, I will give to you instructions about the local that the chest was robbed \nis near a Real road around Dragon Mountain, here is your your half of the advance payment 1500 goldcoins when you return with the real gift  I pay to you the other half.')
                check2 =+ 1
    elif firstOption == 'THANE':
                 print('\nknown says:Ok, here is the letter, you mustn’t open  this letter \nI will pay to you 500 goldcoins now and more 500 goldcoins when you return with the real label,\nthe thane will also lend you a horse to get there faster')
                 check2 =+ 1
    else:
            print(f'\nenter with a option valid, {firstOption} is not a valid option')
            check =+ 0
check3 = 0
while check3 == 0:
       if firstOption == 'KING': 
          second_option = input('\nThe king has selected the best horse to be at his disposal The Faster Night but \nThe king is very superstitious he asked you to flip a coin, your luck will decide if you go with the horse or go walking, you want HEAD or TAILS? ')           
          second_option = second_option.upper()
          if second_option == 'HEAD ' or 'TAILS':
                    print("\nOk, Let's go")
                    
                    luck = coinFlip()
                    luck1 = luck
                    check3 += 1
          else:
                    print(f'\nenter with a option valid, {second_option} is not a valid option! ')
       elif firstOption == 'THANE':
          second_option = input('\nWhich one do you want: CROOKED TAIL or BROWN LAME? ')
          second_option = second_option.upper()
          if second_option == 'CROOKED TAIL':
                     print('good choice')
                     check3 += 1
          elif second_option == 'BROWN LAME':
                     print('good choice')
                     check3 += 1
          else:
                     print(f'\nenter with a option valid, {second_option} is not a valid option! ')
check4 = 0
while check4 == 0:
        if second_option == 'CROOKED TAIL':
          print(f'\n{second_option} is a very good horse you will take 1 day to reach your destination')
          check4 += 1
        elif second_option == 'BROWN LAME':
                print(f'{second_option} is a very good horse but it is lame you will take 2 day to reach your destination')
                check4 += 1
        elif second_option == 'HEAD' or 'TAILS':
             print(f'{protaganist} roll: {luck}')
             check4 += 1
             if luck1 == second_option:
               print('Faster Night is a very good horse do you will spend 8 hours to arrive at your destination')
               check4 += 1
             elif luck != second_option:
               print('Ops, walking probaly you will spend 3 days to arrive in your destination, good luck')
               check4 += 1
         
check5 = 0
while check5 == 0:
       third_option = input(f'\n{protaganist} goes to your house to get your equipment you choose a SWORD or a SPEAR? ')
       third_option = third_option.upper()
       if third_option == 'SWORD':
         print('\nGood choice, with this sword you will have advantage in short battles')
         check5 += 1
       elif third_option == 'SPEAR':
         print('\nGood choice, with this Spear you will have advantage in long battles')
         check5 += 1
         
       else:
         print(f'\nenter with a option valid, {third_option} is not a valid option! ')
         check =+ 0
         
