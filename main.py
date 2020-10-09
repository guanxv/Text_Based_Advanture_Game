import time
import random
import keyboard
from dnd_data import race_desc, race_short, Race, races


class Charactor:

    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0

    race = None

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

        # race mod

        # choose class

        # class mod

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

            if keyboard.is_pressed("space"):
                self.roll_dice_for_ability()
                print("Do you want to re-roll the dice ? (Space / N)")

            if keyboard.is_pressed("n"):
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
        self.race = races[index]
        print("Oh, you are a " + self.race.name + "!")
        print('You have got following Ability adjustment:')
        
        
        for ability , value in self.race.ability_mod.items():
            if value == 0:
                pass
            else:
                print(ability + ":   +" + str(value))
        
        self.ability_race_mod()

        self.print_current_ability()
                
        

        #print the key and value for ability mod
        #modify the ability

        

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
                    confirm = input("Do you confirm ? (Yes / No)")

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

    def ability_race_mod(self):
        self.strength += self.race.ability_mod['Strength']
        self.dexterity += self.race.ability_mod['Dexterity']
        self.constitution += self.race.ability_mod['Constitution']
        self.intelligence += self.race.ability_mod['Intelligence']
        self.wisdom += self.race.ability_mod['Wisdom']
        self.charisma += self.race.ability_mod['Charisma']

    def print_current_ability(self):
    
        
        print('Your current ability are:')
        nl(2)
        print('Strength:' + str(self.strength) )
        print('Dexterity:' + str(self.dexterity) )
        print('Constitution:' + str(self.constitution) )
        print('Intelligence:' + str(self.intelligence) )
        print('Wisdom:' + str(self.wisdom) )
        print('Charisma:' + str(self.charisma) )



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



b = Charactor("aa")
