from enum import Enum
from random import randint

from prettytable import PrettyTable


class Options(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3


class Result(Enum):
    Lose = 0
    Win = 1
    Draw = 2


def com_int(player_decision):
    print(f"Computer decision: {Options(com_choice).name}")

    option = int(player_decision)

    if option > 3:
        return -1

    if (option == Options.Rock.value and com_choice == Options.Scissor.value
            or option > com_choice):
        return Result.Win
    elif option < com_choice:
        return Result.Lose
    else:
        return Result.Draw


def com_string(player_decision):
    if player_decision.lower() == Options.Rock.name.lower():
        return com_int(Options.Rock.value)
    elif player_decision.lower() == Options.Paper.name.lower():
        return com_int(Options.Paper.value)
    elif player_decision.lower() == Options.Scissor.name.lower():
        return com_int(Options.Scissor.value)
    else:
        return -1


def init_gameboard():
    table = PrettyTable(["Actions", "Number"])
    for choice in Options:
        table.add_row([choice.name, choice.value])
    print(table)
    print("__________________")


def main():
    global com_choice
    round_counter = 0

    init_gameboard()

    while True:
        decision = input("Enter your choice: ")

        com_choice = randint(1, 3)

        if decision.isdecimal():
            evaluation = com_int(decision)
        else:
            evaluation = com_string(decision)

        if evaluation == -1:
            print(f"Invalid Input: {decision}")
            continue

        if evaluation == Result.Win:
            print("You Won!")
            break
        elif evaluation == Result.Lose:
            print("You Lose!")
        elif evaluation == Result.Draw:
            print("Draw!")

    round_counter += 1
    print(f"Round: {round_counter}")
    print("_" * 15)


main()
