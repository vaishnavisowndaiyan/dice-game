import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

count = 0
while True:
    user_choice = input('Roll the dice? (y/n): ').lower().strip()
    if user_choice == 'y':
        count += 1
        print(roll_dice())
    elif user_choice == 'n':
        print(f'\nYou have rolled the dice {count} times in this session.')
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')