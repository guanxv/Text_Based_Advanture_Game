import time
import random
import keyboard
from dnd_data import race_desc, race_short


class Charactor:

    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0

    race = ""
    clas = ""
    level = ""
    exp = 0

    def __init__(
        self, name
    ):  # , strength, dexterity, constitution, intelligence, wisdom, charisma, race, clas, level):
        
        # time.sleep(100)
        self.name = self.get_char_name()
        self.get_char_ability_score()
        self.choose_race()
        # self.strength = strength
        # self.dexterity = dexterity
        # self.constitution = constitution
        # self.intelligence = intelligence
        # self.wisdom = wisdom
        # self.charisma = charisma
        # self.race = race
        # self.clas = clas
        # self.level = level

    @staticmethod
    def get_char_name():
        clear_screen()
        name = ""
        while name == "":
            name = input("Brave warrior, What's your name?   :")
        return name

    def get_char_ability_score(self):
        clear_screen()
        thinking(6)

        print("Hi {}, Now let's see what is your ability!".format(self.name))
        time.sleep(2)
        roll_screen(3)

        print("You need to roll the dice for following abilitys")
        nl(1)
        self.prt_ability_band()
        print("Are you ready?")
        print("Press Space Bar for roll the dice:")

        while True:

            if keyboard.press_and_release("space"):
                self.roll_dice_for_ability()
                print("Do you want to re-roll the dice ? (Space / N)")

            if keyboard.press_and_release("n"):
                break

            # else:
            #     print("Press (Space) for rolling the dice!, (N) for stopping !")

    def roll_dice_for_ability(self):
        time.sleep(0.8)

        self.strength = sum_roll_dice_remove_lowest(4, 6)
        self.dexterity = sum_roll_dice_remove_lowest(4, 6)
        self.constitution = sum_roll_dice_remove_lowest(4, 6)
        self.intelligence = sum_roll_dice_remove_lowest(4, 6)
        self.wisdom = sum_roll_dice_remove_lowest(4, 6)
        self.charisma = sum_roll_dice_remove_lowest(4, 6)

        clear_screen()
        self.prt_ability_band()
        print(
            "   {}           {}             {}               {}               {}            {}".format(
                self.strength,
                self.dexterity,
                self.constitution,
                self.intelligence,
                self.wisdom,
                self.charisma,
            )
        )

    def choose_race(self):
        clear_screen()
        print("Dear Warrior, What is your race:")
        nl(1)

        index = self.chooser(race_desc)
        race_select = race_short[index]
        print("Oh, you are a " + race_select "!")
        self.race = race_select

    @staticmethod
    def chooser(list_to_choose):
        print("Please Choose from following:")
        nl(1)
        for item in list_to_choose:
            print(item)
            time.sleep(0.2)

        nl(1)

        while True:

            selected = input("Please Choose One: ")
            selected = ("(" + selected + ")").upper()

            for idx, item in enumerate(list_to_choose):
                if selected in item:
                    print("You selected: \n {}".format(list_to_choose[idx]))
                    nl(1)
                    confirm =  input("Do you confirm ? (Yes / No)")

                    if "y" in confirm.lower():
                        return idx
                    if "n" in confirm.lower():
                        pass

            



    @staticmethod
    def prt_ability_band():
        print(
            """
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#                                                                                   #
#  STRENGTH  #  DEXTERITY  #  CONSTITUTION  #  INTELLIGENT  #  WISDOM  #  CHARISMA  #
#                                                                                   #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
            """
        )


def clear_screen():
    for i in range(100):
        print("\n")


def nl(n):
    for i in range(n):
        print("\n")


def roll_screen(n):
    for i in range(n):
        nl(1)
        time.sleep(1)


def thinking(n):
    print(".")
    for i in range(n):
        time.sleep(0.5)
        print(".")


def roll_dice(n_dice, dice_rank):
    result = []

    for i in range(n_dice):
        result.append(random.randint(1, dice_rank))
    return result


def remove_lowest(num_list):
    if len(num_list) == 1:
        return num_list
    else:
        lowest = min(num_list)
        num_list.remove(lowest)
        return num_list


def sum_roll_dice_remove_lowest(n_dice, dice_rank):
    dice_list = roll_dice(n_dice, dice_rank)
    dice_list.sort()
    dice_list.pop()
    return sum(dice_list)


print(sum_roll_dice_remove_lowest(4, 6))


# time.sleep(10)
b = Charactor("aa")
