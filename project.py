import random
"""
Bem vindos ao meu projeto
"""


def main():
    print("Welcome to The Roller Dice Simulator")
    print("we have 6 types of dice with different faces being dice of 4 (d4),\n8(d8), 10(d10), 12(d12) and 20 faces (d20)")
    print("choose what dice you want roll \nex: to roll d4 type: d4, to roll d6 type: d6, etc.")
    print("\nto exit the simulator type: quit")
    option = ''

    while option != 'quit':

        choose = input('\ntype your option: ')
        choose = choose.lower()
        if choose == 'quit':
            print('\nthank you for use the roller dice simulator')
            quit()
        else:
            num_dice = int(input("how many dices you want roll ? "))

        if choose == 'd4':
            result = dice_4_faces(num_dice)
            print("D4 roll results:")
            times = 1
            for _ in result:
                print(f"{times}º D4: {_}")
                times += 1
            total(result)

        elif choose == 'd6':
            result = dice_6_faces(num_dice)
            print("D6 roll results:")
            times = 1
            for _ in result:
                print(f"{times}º D6: {_}")
                times += 1
            total(result)
        elif choose == 'd8':
            result = dice_8_faces(num_dice)
            print("D8 roll results:")
            times = 1
            for _ in result:
                print(f"{times}º D8: {_}")
                times += 1
            total(result)
        elif choose == 'd10':
            result = dice_10_faces(num_dice)
            print("D10 roll results:")
            times = 1
            for _ in result:
                print(f"{times}º D10: {_}")
                times += 1
            total(result)
        elif choose == 'd12':
            result = dice_12_faces(num_dice)
            print("D12 roll results:")
            times = 1
            for _ in result:
                print(f"{times}º D12: {_}")
                times += 1
            total(result)
        elif choose == 'd20':
            result = dice_20_faces(num_dice)
            print("D20 roll results:")
            times = 1
            for _ in result:
                print(f"{times}º D20: {_}")
                times += 1
            total(result)
        elif choose == 'quit':
            option = 'quit'
            break
        else:
            print("invalid option try again")
            pass


def total(roll_result):
    # sum the total value of your rolls
    number = roll_result
    total = sum(number)
    return print(f"The total value of your roll is: {total}")


def dice_4_faces(num_dice):
    # rolls 4-sided dice
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 4)
        roll_results.append(roll)
    return roll_results


def dice_6_faces(num_dice):
    # rolls 6-sided dice
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


def dice_8_faces(num_dice):
    # rolls 8-sided dice
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 8)
        roll_results.append(roll)
    return roll_results


def dice_10_faces(num_dice):
    # rolls 10-sided dice
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 10)
        roll_results.append(roll)
    return roll_results


def dice_12_faces(num_dice):
    # rolls 12-sided dice
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 12)
        roll_results.append(roll)
    return roll_results


def dice_20_faces(num_dice):
    # rolls 20-sided dice
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 20)
        roll_results.append(roll)
    return roll_results


if __name__ == "__main__":
    main()
