import random
import os

def num_die():
    while True:
        try:
            num_dice = input('Number of dice (1 or 2): ')
            if num_dice in ['1', 'one']:
                return 1
            elif num_dice in ['2', 'two']:
                return 2
            else:
                raise ValueError('Please enter 1 or 2 only')
        except ValueError as err:
            print(err)

def roll_dice():
    min_val = 1
    max_val = 6
    roll_again = 'y'

    while roll_again.lower() in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = num_die()

        if amount == 2:
            print('Rolling the dice...')
            dice_1 = random.randint(min_val, max_val)
            dice_2 = random.randint(min_val, max_val)

            print('The values are:')
            print('Dice One:', dice_1)
            print('Dice Two:', dice_2)
            print('Total:', dice_1 + dice_2)
        else:
            print('Rolling the die...')
            dice_1 = random.randint(min_val, max_val)
            print('The value is:', dice_1)

        roll_again = input('Roll Again? (yes/y to continue): ')

if __name__ == '__main__':
    roll_dice()
