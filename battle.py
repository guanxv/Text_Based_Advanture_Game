import random


print('WELCOME TO RPG SHOOTING GAME...')
print('PLEASE TYPE YOUR NAME BELOW')
print('\n')


p1_team_label = '''
 [<->]
<]<^>[>'''

p2_team_label = '''
  >--<
x[]__[]x'''

#knife list [ 'name', Damage, Damage per bullet , durability]
knife1 = ["Ninja", 1, 6]
knife2 = ['Blade', 3, 5]
knife3 = ['Saw', 2, 5]

#mech gun list [ 'name', shots, damage per bullet]
mech_gun1 = ['HellFire', 4, 1]
mech_gun2 = ['ButtCrap', 7, 0.5]
mech_gun3 = ['KillerCraspalis', 6, 0.45]

#flame list [ 'name',attack]
Flame1 = ['HeavyHualer', 4]
Flame2 = ['KillingHeavy', 3]



p1_name = input('Player 1 name: ')
p2_name = input('Player 2 name: ')

print('\n' + p1_name+"'s TEAM LABEL" + p1_team_label + '\n')
print('\n' + p2_name+"'s TEAM LABEL" + p2_team_label + '\n')

#p1_choose_weapon = input("press key 1,2 or 3 to generate you random weapon: ")
p1_weapon = []
p2_weapon = []

weapon_selection = []
weapon_selection.append(knife1)
weapon_selection.append(knife2)
weapon_selection.append(knife3)
weapon_selection.append(mech_gun1)
weapon_selection.append(mech_gun2)
weapon_selection.append(mech_gun3)
weapon_selection.append(Flame1)
weapon_selection.append(Flame2)


def gen_random_weapon():
    player_weapon = []
    for reps in range(3):
        i = random.randint(0, 2)
        j = random.randint(3, 5)
        k = random.randint(6, 7)

    player_weapon.append(weapon_selection[i])
    player_weapon.append(weapon_selection[j])
    player_weapon.append(weapon_selection[k])
    print(player_weapon)
    return player_weapon

print('THE WEAPONS ARES: ')
print(weapon_selection)

print ( '\n' + p1_name + " GOTS:")
p1_weapon = gen_random_weapon()
print ('\n' + p2_name + " GOTS:")
p2_weapon = gen_random_weapon()

# initial status

hp = 40

p1_hp = hp
p2_hp = hp

distance = 30

# end of initial status

def attack(player):

    attacker_name = ''
    attacker_name = p1_name if player == 'p1' else p2_name
    attacker_weapon = p1_weapon if player == 'p1' else p2_weapon

    print("please choose your weapon:")
    n = 1
    for weapon in attacker_weapon:
        print(str(n) + ": " + str(weapon))
        n += 1



    weapon_chosen = []
    while weapon_chosen == []:
        weapon_chosen_num = input('1, 2, or 3:')
        if weapon_chosen_num in ['1', '2', '3']:
            weapon_chosen = attacker_weapon[int(weapon_chosen_num)-1]

    print(weapon_chosen)



def select_action(player):

    player_name = ''
    player_name = p1_name if player == 'p1' else p2_name

    action = ""

    while not (action == 'a' or action == 'm'):
        action = input('\n' + player_name + ' PLEASE SELECT YOUR ACTION: a = Attack / m = Move  ')
        print(player_name + " has selected "+ action)
        if action != 'a' and action != 'm':
            print("please try again ")
        elif action == 'a':
            attack(player)
        elif action == 'm':
            move(player)


select_action('p1')