import random
import json
import argparse
import csv
import sqlite3
import random
import name_generator
import time

parser = argparse.ArgumentParser(description='This allows you to quickly command line create characters.')
# parser.add_argument('menuOptions', type=int)
                    # help='an integer for the accumulator')
# parser.add_argument('--foo', help='foo help')

parser.add_argument('-M', '--Menu', type=int, choices=xrange(1,5),default=0)
parser.add_argument('-d', '--dice', type=int, choices=xrange(3,7),default=3)
parser.add_argument('-g', '--gender', type=str, choices=['random','female','male'],default='random')
parser.add_argument('-fn', '--first_name', type=str, default='')
parser.add_argument('-ln', '--last_name', type=str, default='')

characterClasses = ['Strong','Fast','Tough','Smart','Dedicated','Charismatic']
classOptions =  list(characterClasses)
classOptions.append("random")
parser.add_argument('-c', '--character_class', type=str, choices=classOptions,default='random')

args = parser.parse_args()

maxRolls = args.dice

print args

print args.Menu
# parser.add_argument('--Menu', dest='option', action='store_const',
                    # const=sum, default=max,
                    # help='command line option')
# args = parser.parse_args()

# parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('foo', type=int, choices=xrange(5, 10) )
# parser.parse_args(['7'])

# parser.print_help()

# quit()
# Namespace(foo=7)
# >>> parser.parse_args(['11'])
# usage: PROG [-h] {5,6,7,8,9}
# PROG: error: argument foo: invalid choice: 11 (choose from 5, 6, 7, 8, 9)





# print args.option(args.menuOptions)

# all_rulebooks = ["Modern 3e","Fantasy 2e","Fantasy 3e","Fantasy 4e","Fantasy 5e"]
all_rulebooks = ["Modern 3e"]



def attributeModifier(number):
    try:
        return int((number[0]  - 10) / 2)
    except:
        try:
            return int((number  - 10) / 2)
        except:
            pass

def main():
    selecting_menu_option = True
    rulebook_type = 0
    while selecting_menu_option == True:
        print "Welcome to the character generation program, default is 2."
        print "You are currently creating a ",all_rulebooks[rulebook_type]," character."
        print ""
        print "/----------------------------------------------------------------"
        print "| 1.  manually create a new character"
        print "|[2]. auto create a character with random values and display JSON."
        print "| 3.  auto create a character with random values and save JSON to text."
        print "| 4.  auto create a character with random values and save to database."
        print "|"
        print "| 9.  Change character rule book type."
        print "/------------------attributeValues-------------------------------"
        print ""
        if args.Menu==0:
            menu_option = str(raw_input('Enter your selection:') )
            if menu_option == "9":
                # print "Sorry. That option is still in development."
                rulebook_type += 1
                if rulebook_type >= len(all_rulebooks):
                    rulebook_type = 0
                time.sleep(1)
                print ""
            else:
                pass
                selecting_menu_option = False

        else:
            menu_option = str(args.Menu)
    if (menu_option == ''):
        menu_option = '2'
        # quit()
    # print "You selected"
    if (menu_option == '1'):
        working_details = True
        while working_details:
            if args.gender == 'random':
                time.sleep(1)
                print ""
                option = str(raw_input('If you want specify a gender, enter "Female" or "Male" without quotes:') )
                if option in ["F",'f',"female","Female"]:
                    args.gender = "female"
                elif option in ["M",'m',"male","Male"]:
                    args.gender = "male"
                else:
                    print "Ok, we're going with a random gender."
                    args.gender = random.choice(('male', 'female'))
            else:
                args.gender = args.gender
            print "Great! Your character is", args.gender,"."

            if args.last_name == "":
                time.sleep(1)
                print ""
                option = str(raw_input('Enter a last name or press enter to get a random one: '))
                if option == "":
                    args.last_name = name_generator.get_last_name()
                else:
                    args.last_name = option
            if args.first_name == "":
                time.sleep(1)
                print ""
                option = str(raw_input('Enter a first name or press enter to get a random one: '))
                if option == "":
                    args.first_name = name_generator.get_first_name(args.gender)
                else:
                    args.first_name = option
            print ""
            print "Hello,", args.first_name , args.last_name, "and welcome to the game."
            if args.character_class == "random":
                time.sleep(1)
                print ""
                print "What kind of character are you?"
                print "Enter 'Strong', 'Fast', 'Tough', 'Smart', 'Dedicated', 'Charismatic',"
                option = str(raw_input("or just press enter to get a random character class assignment: "))
                if option in characterClasses:
                    args.character_class = option
                else:
                    args.character_class = random.choice(characterClasses)

            time.sleep(1)
            print ""
            print "ok we are going with the following details:"
            print ""
            print args.first_name + " " + args.last_name
            print args.gender
            print args.character_class
            print ""
            print "Does this look good?"
            option = str(raw_input("Just press enter if it does, otherwise type 'No' and enter: "))
            print ""
            time.sleep(1)
            if option == "":
                working_details = False
            else:
                args.gender = "random"
                args.first_name = ""
                args.last_name = ""
                args.character_class = "random"

        print "Let's get rolling"
        time.sleep(1)
        print ""
        print "For each of the six stats, you get", maxRolls, "rolls of a 6 sided die."
        option = str(raw_input("Do you want to automatically roll stats:"))


        print "All done!"
        time.sleep(1)
        print ""

    if (menu_option == '1' or menu_option == '2' or menu_option == '3' or menu_option == '4'):
        if args.gender == 'random':
            character_gender = random.choice(('male', 'female'))
        else:
            character_gender = args.gender

        attributeRoles = []
        attributeValues = []
        print 'Dice rolls'
        for num in range (0,6):
            roll = []
            for diceRolls in range (0,maxRolls):
                roll.append(random.randint(1,6))
                print roll[-1],
            print
            roll.sort()
            top_three = roll[-1]+roll[-2]+roll[-3]
            print top_three,": Top 3 rolls (",roll[-1] , roll[-2], roll[-3],")"
            attributeValues.append ((top_three,roll))
        attributeValues.sort()

        print
        print 'Totals'
        for each in attributeValues:
            print each,
        print
        for each in attributeRoles:
            print each,
        print

        print args.character_class
        if (args.character_class == 'random'):
            newCharacter = random.choice(characterClasses)
        else:
            newCharacter = args.character_class
        print newCharacter, "Character"
        attributes = ['STR','DEX','CON','INT','WIS','CHA']
        characterAttributes = {'STR':0,'DEX':0,'CON':0,'INT':0,'WIS':0,'CHA':0}
        # print attributes
        # print value
        if (newCharacter == characterClasses[0]):
            # Assign Strength
            characterAttributes['STR'] = attributeValues[-1]
            attributes.remove('STR')
            del attributeValues[-1]
            nextGroup = ['DEX','CON']
            while (nextGroup <> []):
                next = random.choice(nextGroup)
                nextGroup.remove(next)
                attributes.remove(next)
                characterAttributes[next] = attributeValues[-1]
                del attributeValues[-1]
        if (newCharacter == characterClasses[1]):
            # Assign Dexterity
            characterAttributes['DEX'] = attributeValues[-1]
            attributes.remove('DEX')
            del attributeValues[-1]
            nextGroup = ['CHA','WIS','INT']
            while (nextGroup <> []):
                next = random.choice(nextGroup)
                nextGroup.remove(next)
                attributes.remove(next)
                characterAttributes[next] = attributeValues[-1]
                del attributeValues[-1]
        if (newCharacter == characterClasses[2]):
            # Assign Dexterity
            characterAttributes['CON'] = attributeValues[-1]
            attributes.remove('CON')
            del attributeValues[-1]
            nextGroup = [random.choice(['STR','DEX']),'WIS','INT']
            while (nextGroup <> []):
                next = random.choice(nextGroup)
                nextGroup.remove(next)
                attributes.remove(next)
                characterAttributes[next] = attributeValues[-1]
                del attributeValues[-1]
        if (newCharacter == characterClasses[3]):
            # Assign Dexterity
            characterAttributes['INT'] = attributeValues[-1]
            attributes.remove('INT')
            del attributeValues[-1]
            nextGroup = [random.choice(['STR','DEX','CON']),random.choice(['WIS','CHA'])]
            while (nextGroup <> []):
                next = random.choice(nextGroup)
                nextGroup.remove(next)
                attributes.remove(next)
                characterAttributes[next] = attributeValues[-1]
                del attributeValues[-1]
        if (newCharacter == characterClasses[4]):
            # Assign Dexterity
            characterAttributes['WIS'] = attributeValues[-1]
            attributes.remove('WIS')
            del attributeValues[-1]
            nextGroup = ['INT']
            for each in random.sample(['STR','DEX','CON'],random.choice([1,2,3])):
                nextGroup.append(each)
            # print nextGroup
            while (nextGroup <> []):
                next = random.choice(nextGroup)
                # print next,
                nextGroup.remove(next)
                attributes.remove(next)
                characterAttributes[next] = attributeValues[-1]
                del attributeValues[-1]
        if (newCharacter == characterClasses[5]):
            # Assign Dexterity
            characterAttributes['CHA'] = attributeValues[-1]
            attributes.remove('CHA')
            del attributeValues[-1]
            nextGroup = random.sample(['STR','DEX','CON'],random.choice([1,2,3]))
            while (nextGroup <> []):
                next = random.choice(nextGroup)
                nextGroup.remove(next)
                attributes.remove(next)
                characterAttributes[next] = attributeValues[-1]
                del attributeValues[-1]
        while (attributes <> []):
            # print attributes
            # print value
            next = random.choice(attributes)
            attributes.remove(next)
            characterAttributes[next] = attributeValues[-1]
            del attributeValues[-1]
        print 'STR:',characterAttributes['STR'], 'Strength Modifier:', attributeModifier(characterAttributes['STR'])
        print 'DEX:',characterAttributes['DEX'], 'Dexterity Modifier:', attributeModifier(characterAttributes['DEX'])
        print 'CON:',characterAttributes['CON'], 'Constitution Modifier:', attributeModifier(characterAttributes['CON'])
        print 'INT:',characterAttributes['INT'], 'Intelligence Modifier:', attributeModifier(characterAttributes['INT'])
        print 'WIS:',characterAttributes['WIS'], 'Wisdom Modifier:', attributeModifier(characterAttributes['WIS'])
        print 'CHA:',characterAttributes['CHA'], 'Charisma Modifier:', attributeModifier(characterAttributes['CHA'])
        print
        print "Hit Point Time"
        hitPoints = {}
        if (newCharacter == 'Tough'):
            hitPoints['MaxHP'] = 10 + attributeModifier(characterAttributes['CON'])
            hitPoints['CurHP'] = hitPoints['MaxHP']
        elif (newCharacter == 'Fast' or newCharacter == 'Strong'):
            hitPoints['MaxHP'] = 8 + attributeModifier(characterAttributes['CON'])
            hitPoints['CurHP'] = hitPoints['MaxHP']
        else:
            hitPoints['MaxHP'] = 6 + attributeModifier(characterAttributes['CON'])
            hitPoints['CurHP'] = hitPoints['MaxHP']
        print
        characterLevelAbilities = {}

        #Base Attack Calculations
        if (newCharacter == 'Strong'):
            characterLevelAbilities['BaseAttackBonus'] = 1
        else:
            characterLevelAbilities['BaseAttackBonus'] = 0

        #Fortitude Save Calculations
        if (newCharacter == 'Strong' or newCharacter == 'Tough' or newCharacter == 'Dedicated' or newCharacter == 'Charismatic'):
            characterLevelAbilities['FortSave'] = 1
        else:
            characterLevelAbilities['FortSave'] = 0

        #Reflex Save Calculations
        if (newCharacter == 'Fast' or newCharacter == 'Charismatic'):
            characterLevelAbilities['RefSave'] = 1
        else:

        #Will Save Calculations
            characterLevelAbilities['RefSave'] = 0
        if (newCharacter == 'Smart' or newCharacter == 'Dedicated'):
            characterLevelAbilities['WillSave'] = 1
        else:
            characterLevelAbilities['WillSave'] = 0

        #Defense Bonus Calculations
        if (newCharacter == 'Fast'):
            characterLevelAbilities['DefenseBonus'] = 3
        elif (newCharacter == 'Strong' or newCharacter == 'Tough' or newCharacter == 'Dedicated'):
            characterLevelAbilities['DefenseBonus'] = 1
        else:
            characterLevelAbilities['DefenseBonus'] = 0

        #Reputation Bonus Calculations
        if (newCharacter == 'Charismatic'):
            characterLevelAbilities['Reputation Bonus'] = 2
        elif (newCharacter == 'Smart' or newCharacter == 'Dedicated'):
            characterLevelAbilities['Reputation Bonus'] = 1
        else:
            characterLevelAbilities['Reputation Bonus'] = 0
        # print characterLevelAbilities
        characterAbilities = {}
        characterAbilities['InitiativeModifier'] = attributeModifier(characterAttributes['DEX'])
        characterAbilities['Defense'] = 10 + attributeModifier(characterAttributes['DEX']) + characterLevelAbilities['DefenseBonus']
        if args.last_name == "":
            last_name = name_generator.get_last_name()
        else:
            last_name = args.last_name
        if args.first_name == "":
            first_name = name_generator.get_first_name(character_gender)
        else:
            first_name = args.first_name
        character = {   "class":newCharacter,
                        "attributes":characterAttributes,
                        "hitpoints":hitPoints,
                        "level_abilities":characterLevelAbilities,
                        "gender":character_gender,
                        "name":{
                            "last":last_name,
                            "first":first_name},
                        "abilities":characterAbilities,
                        "equipment":None,
                        "equiped":{
                            "armor":None,
                            "right_hand":None,
                            "left_hand":None},
                        "attack_details":
                            {"weapon_name": "unarmed", "complexity": "simple", "type": "melee", "damage_die": "1d3", "damage_type": "non-leathal", "weight": "0"}
                            # {"unarmed":"1d4"}
                        }
    json_data = json.dumps(character)
    print json.dumps(character,sort_keys=True, indent=4)
    if (menu_option == '4'):
        conn = sqlite3.connect('dnd_game.sqlite')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS characters
                     (
                     character_name text UNIQUE,
                     character_data text
                     )''')
        c.execute('INSERT INTO characters VALUES (?,?)', (last_name+"_"+first_name,json_data),)
        conn.commit()
        conn.close()


    # print json.dumps([newCharacter,characterAttributes,hitPoints,characterLevelAbilities,characterAbilities], sort_keys=True, indent=4)
    # print json.dumps([newCharacter,characterAttributes,hitPoints,characterLevelAbilities,characterAbilities], sort_keys=True, indent=1)

if __name__ == "__main__":
    main()
