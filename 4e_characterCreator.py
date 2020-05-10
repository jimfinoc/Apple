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


all_rulebooks = ["Fantasy 4e"]
characterClasses = ['Commoner','Cleric','Fighter', 'Paladin', 'Ranger', 'Rogue', 'Warlock', 'Warlord','Wizard',]
characterClasses.extend( ['Sorcerer','Barbarian'] )
# characterClasses.extend( ['Avenger', 'Barbarian', 'Bard', 'Druid', 'Invoker', 'Shaman', 'Sorcerer', 'Warden'] )
characterClasses.extend( ['Monk'] )
# characterClasses.extend( ['Ardent', 'Battlemind', 'Monk', 'Psion', 'Runepriest', 'Seeker'] )
characterRaces = ['Dragonborn','Dwarf','Eladrin','Elf','Half-Elf','Halfling','Human','Tiefling']
# characterRaces.extend( ['Deva','Gnome','Golaith','Half-Orc','Shifter'] )
# characterRaces.extend( ['Deva','Gnome','Golaith','Half-Orc','Shifter'] )



parser.add_argument('-M', '--Menu', type=int, choices=xrange(1,5),default=0)
parser.add_argument('-d', '--dice', type=int, choices=xrange(3,7),default=3)
parser.add_argument('-g', '--gender', type=str, choices=['female','male'],default='random')
parser.add_argument('-fn', '--first_name', type=str, default='')
parser.add_argument('-ln', '--last_name', type=str, default='')
parser.add_argument('-pn', '--player_name', type=str, default='')


# classOptions =  list(characterClasses)
# classOptions.append("random")
parser.add_argument('-c', '--character_class', type=str, choices=characterClasses,default='random')
parser.add_argument('-r', '--character_race', type=str, choices=characterRaces,default='random')

args = parser.parse_args()

maxRolls = args.dice
print args




# print args.option(args.menuOptions)
def updateAttributes(characterAttributes = {'STR':[0,[0,0,0]],'DEX':[0,[0,0,0]],'CON':[0,[0,0,0]],'INT':[0,[0,0,0]],'WIS':[0,[0,0,0]],'CHA':[0,[0,0,0]]}):
    # for each in characterAttributes.items():
    for each in characterAttributes.keys():
        # print each, len(characterAttributes[each])
        # if len(characterAttributes[each]) > 2:
        try:
            characterAttributes[each][0] = characterAttributes[each][1][-3] + characterAttributes[each][1][-2] + characterAttributes[each][1][-1]
        except:
            print "check the characterAttributes value, I cannot add the high three and store them as the the first element of the list"
            print characterAttributes[each]
        try:
            for i in range (2,len(characterAttributes[each]) ):
                characterAttributes[each][0] += characterAttributes[each][i]
        except:
            print "something else may be wrong with characterAttributes"
            print characterAttributes[each]

def updateSkills(characterSkills = {}, characterAttributes = {}):
    for each in characterSkills.keys():
        try:
            characterSkills[each][0] = attributeModifier(characterAttributes[characterSkills[each][1]][0])
        except:
            print "check the characterSkills & characterAttributes values"
            print characterSkills[each]
            print characterSkills[each][0]
            print characterSkills[each][1]
            print characterAttributes[characterSkills[each][1]][0]
            print "mod",attributeModifier(characterAttributes[characterSkills[each][1]][0])
            print "len",len(characterSkills[each])
            # print characterAttributes[ [characterSkills[each][1]] ]
            # print characterAttributes[each]
        try:
            for i in range (2,len(characterSkills[each]) ):
                print "i",i
                characterSkills[each][0] += characterSkills[each][i]
        except:
            print "something else may be wrong with characterskills"
            print characterSkills[each]
            # print characterAttributes[each]

def attributeModifier(number):
    try:
        return int((number[0]  - 10) / 2)
    except:
        try:
            return int((number  - 10) / 2)
        except:
            pass

def statPicker(characterAttributes = {'STR':0,'DEX':0,'CON':0,'INT':0,'WIS':0,'CHA':0},attributeValues=[16,14,13,12,11,10],stat1=[],stat2=[],stat3=[],stat4=[],stat5=[],stat6=[],attributes=['STR','DEX','CON','INT','WIS','CHA']):
    stats = [stat1,stat2,stat3,stat4,stat5,stat6]
    for number in range(0,len(stats)):
        # print number
        while (stats[number] <> []):
            # print stats[number]
            next = random.choice(stats[number])
            try:
                stats[number].remove(next)
                attributes.remove(next)
                characterAttributes[next] = attributeValues[-1]
                del attributeValues[-1]
            except:
                pass
            finally:
                pass
    while (attributes <> []):
        # print attributes
        # print value
        next = random.choice(attributes)
        attributes.remove(next)
        # print attributeValues[0]
        characterAttributes[next] = attributeValues[-1]
        del attributeValues[-1]

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
        # print "| 3.  auto create a character with random values and save JSON to text."
        # print "| 4.  auto create a character with random values and save to database."
        print "|"
        # print "/------------------attributeValues-------------------------------"
        print "/----------------------------------------------------------------"
        print ""
        if args.Menu==4:
            menu_option = '4'
            selecting_menu_option = False


        if args.Menu==0:
            menu_option = str(raw_input('Enter your selection:') )
            if menu_option == "9":
                # print "Sorry. That option is still in development."
                rulebook_type += 1
                if rulebook_type >= len(all_rulebooks):
                    rulebook_type = 0
                time.sleep(1)
                # print "delay 1"
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
        working_gender = True
        working_name = True
        working_class = True
        while working_details:
            while working_gender:
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
                working_gender = False
            while working_name:
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
                working_name = False
            # while working_class:
            if args.character_class == "random":
                time.sleep(1)
                print ""
                print "What kind of character are you?"
                print "Enter you class from one of these:", characterClasses
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
            if option == "" or option.upper() == "Y" or option.upper() == "YES":
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
        # print 'Dice rolls'
        for num in range (0,6):
            roll = []
            for diceRolls in range (0,maxRolls):
                roll.append(random.randint(1,6))
                # print roll[-1],
            # print
            roll.sort()
            top_three = roll[-1]+roll[-2]+roll[-3]
            # print top_three,": Top 3 rolls (",roll[-1] , roll[-2], roll[-3],")"
            attributeValues.append ([top_three,roll])
            # attributeValues.append ([0,roll])
            # attributeValues.append ([roll])
        attributeValues.sort()
        if (args.character_class == 'random'):
            args.character_class = random.choice(characterClasses)
        # else:
            # newCharacter = args.character_class
        # print newCharacter, "Character"
        attributes = ['STR','DEX','CON','INT','WIS','CHA']
        characterAttributes = {'STR':0,'DEX':0,'CON':0,'INT':0,'WIS':0,'CHA':0}
        characterAbilities = {}

        hitPoints = {"MaxHP":0,"CurHP":0}
        skills = {
            "Athletics":[0,"STR"],
            "Endurance":[0,"CON"],
            "Acrobatics":[0,"DEX"],
            "Stealth":[0,"DEX"],
            "Thievery":[0,"DEX"],
            "Arcana":[0,"INT"],
            "History":[0,"INT"],
            "Religion":[0,"INT"],
            "Dungeoneering":[0,"WIS"],
            "Heal":[0,"WIS"],
            "Insight":[0,"WIS"],
            "Nature":[0,"WIS"],
            "Perception":[0,"WIS"],
            "Bluff":[0,"CHA"],
            "Diplomacy":[0,"CHA"],
            "Intimidate":[0,"CHA"],
            "Streetwise":[0,"CHA"]
            }
        characterLevel = 1
        characterAbilities = {}
        characterDefenses = {"AC":[10],'FORT':[10],'REF':[10],'WILL':[10] }
        armorProficiencies = [
            "cloth"
            ]
        weaponProficiencies = [
            ]

        feats = {}
        # print attributes
        # print value
        FirstAttribute = ""
        if (args.character_class == 'Commoner'):
            FirstAttribute = random.choice(attributes)
            hitPoints['level_0'] = 2
            hitPoints['perLevel'] = 2
            hitPoints['dailySurges'] = 1
            weaponProficiencies.append("club")
            choices = [
                'Athletics',
                'Endurance',
                'Acrobatics',
                'Stealth',
                'Thievery',
                'Arcana',
                'History',
                'Religion',
                'Dungeoneering',
                'Heal',
                'Insight',
                'Nature',
                'Perception',
                'Bluff',
                'Diplomacy',
                'Intimidate',
                'Streetwise'
                ]
            random.shuffle(choices)
            choice1 = choices.pop()
            choice2 = choices.pop()
            skills[choice1].append(5)
            skills[choice2].append(5)

            statPicker(characterAttributes,attributeValues)



            # skills['Athletics'].append(5)
            # skills['Endurance'].append(5)
            # skills['Acrobatics'].append(5)
            # skills['Stealth'].append(5)
            # skills['Thievery'].append(5)
            # skills['Arcana'].append(5)
            # skills['History'].append(5)
            # skills['Religion'].append(5)
            # skills['Dungeoneering'].append(5)
            # skills['Heal'].append(5)
            # skills['Insight'].append(5)
            # skills['Nature'].append(5)
            # skills['Perception'].append(5)
            # skills['Bluff'].append(5)
            # skills['Diplomacy'].append(5)
            # skills['Intimidate'].append(5)
            # skills['Streetwise'].append(5)

        if (args.character_class == 'Cleric'):
            hitPoints['level_0'] = 7
            hitPoints['perLevel'] = 5
            hitPoints['dailySurges'] = 7
            characterDefenses['WILL'].append(2)
            armorProficiencies.append("leather")
            armorProficiencies.append("hide")
            armorProficiencies.append("chainmail")
            weaponProficiencies.append("simple_melee")
            weaponProficiencies.append("simple_ranged")

            decision = random.choice([1,2])
            if decision == 1: #"Battle Cleric"
                FirstAttribute = 'STR'
                statPicker(characterAttributes,attributeValues,['STR'],['WIS'],['CHA'])
                skills['Diplomacy'].append(5)
                skills['Heal'].append(5)
                skills['Insight'].append(5)
                skills['Religion'].append(5)
            if decision == 2: #"Devoted Cleric"
                FirstAttribute = 'WIS'
                statPicker(characterAttributes,attributeValues,['WIS'],['CHA'],['STR'])
                skills['Arcana'].append(5)
                skills['Heal'].append(5)
                skills['History'].append(5)
                skills['Religion'].append(5)
        if (args.character_class == 'Fighter'):
            hitPoints['level_0'] = 9
            hitPoints['perLevel'] = 6
            hitPoints['dailySurges'] = 9
            characterDefenses['FORT'].append(2)
            armorProficiencies.append("leather")
            armorProficiencies.append("hide")
            armorProficiencies.append("chainmail")
            armorProficiencies.append("scale")
            armorProficiencies.append("light_shield")
            armorProficiencies.append("heavy_shield")
            weaponProficiencies.append("simple_melee")
            weaponProficiencies.append("simple_ranged")
            weaponProficiencies.append("military_melee")
            weaponProficiencies.append("military_ranged")

            FirstAttribute = 'STR'
            statPicker(characterAttributes,attributeValues,['STR'],['DEX','CON','WIS'])
        if (args.character_class == 'Paladin'):
            hitPoints['level_0'] = 9
            hitPoints['perLevel'] = 6
            hitPoints['dailySurges'] = 10
            characterDefenses['FORT'].append(1)
            characterDefenses['REF'].append(1)
            characterDefenses['WILL'].append(1)
            armorProficiencies.append("leather")
            armorProficiencies.append("hide")
            armorProficiencies.append("chainmail")
            armorProficiencies.append("scale")
            armorProficiencies.append("plate")
            armorProficiencies.append("light_shield")
            armorProficiencies.append("heavy_shield")
            weaponProficiencies.append("simple_melee")
            weaponProficiencies.append("simple_ranged")
            weaponProficiencies.append("military_melee")


            statPicker(characterAttributes,attributeValues,['STR','CHA'],['WIS'])
            if characterAttributes["STR"] > characterAttributes['CHA']:
                FirstAttribute = 'STR'
            elif characterAttributes["STR"] < characterAttributes['CHA']:
                FirstAttribute = 'CHA'
            else:
                FirstAttribute = random.choice(['STR','CHA'])
        if (args.character_class == 'Ranger'):
            hitPoints['level_0'] = 7
            hitPoints['perLevel'] = 5
            hitPoints['dailySurges'] = 6
            characterDefenses['FORT'].append(1)
            characterDefenses['REF'].append(1)
            armorProficiencies.append("leather")
            armorProficiencies.append("hide")
            weaponProficiencies.append("simple_melee")
            weaponProficiencies.append("simple_ranged")
            weaponProficiencies.append("military_melee")
            weaponProficiencies.append("military_ranged")
            statPicker(characterAttributes,attributeValues,['STR','DEX'],['WIS'])
            if characterAttributes["STR"] > characterAttributes['CHA']:
                FirstAttribute = 'STR'
            elif characterAttributes["STR"] < characterAttributes['CHA']:
                FirstAttribute = 'CHA'
            else:
                FirstAttribute = random.choice(['STR','CHA'])
        if (args.character_class == 'Rogue'):
            hitPoints['level_0'] = 7
            hitPoints['perLevel'] = 5
            hitPoints['dailySurges'] = 6
            characterDefenses['REF'].append(2)
            armorProficiencies.append("leather")
            weaponProficiencies.append("dagger")
            weaponProficiencies.append("hand_crossbow")
            weaponProficiencies.append("shuriken")
            weaponProficiencies.append("sling")
            weaponProficiencies.append("short_sword")
            FirstAttribute = 'DEX'
            statPicker(characterAttributes,attributeValues,['DEX'],['STR'],['CHA'])
        if (args.character_class == 'Warlock'):
            hitPoints['level_0'] = 7
            hitPoints['perLevel'] = 5
            hitPoints['dailySurges'] = 6
            characterDefenses['REF'].append(1)
            characterDefenses['WILL'].append(1)
            armorProficiencies.append("leather")
            weaponProficiencies.append("simple_melee")
            weaponProficiencies.append("simple_ranged")
            decision = random.choice([1,2])
            if decision == 1:
                statPicker(characterAttributes,attributeValues,['CHA'],['INT'],['CON'])
                FirstAttribute = 'CHA'
            if decision == 2:
                statPicker(characterAttributes,attributeValues,['CON'],['INT'],['CHA'])
                FirstAttribute = 'CON'
        if (args.character_class == 'Warlord'):
            hitPoints['level_0'] = 7
            hitPoints['perLevel'] = 5
            hitPoints['dailySurges'] = 7
            characterDefenses['FORT'].append(1)
            characterDefenses['WILL'].append(1)
            armorProficiencies.append("leather")
            armorProficiencies.append("hide")
            armorProficiencies.append("chainmail")
            armorProficiencies.append("light_shield")
            weaponProficiencies.append("simple_melee")
            weaponProficiencies.append("simple_ranged")
            weaponProficiencies.append("military_melee")
            statPicker(characterAttributes,attributeValues,['STR'],['CHA','INT'])
            FirstAttribute = 'STR'
        if (args.character_class == 'Wizard'):
            hitPoints['level_0'] = 6
            hitPoints['perLevel'] = 4
            hitPoints['dailySurges'] = 6
            characterDefenses['WILL'].append(2)
            weaponProficiencies.append("dagger")
            weaponProficiencies.append("quarterstaff")
            decision = random.choice([1,2])
            FirstAttribute = 'INT'
            if decision == 1:
                statPicker(characterAttributes,attributeValues,['INT'],['WIS'],['DEX'])
            if decision == 2:
                statPicker(characterAttributes,attributeValues,['INT'],['DEX'],['CON'])
        if (args.character_class == 'Sorcerer'):
            hitPoints['level_0'] = 7
            hitPoints['perLevel'] = 5
            hitPoints['dailySurges'] = 6
            characterDefenses['WILL'].append(2)
            weaponProficiencies.append("simple_melee")
            weaponProficiencies.append("simple_ranged")
            decision = random.choice([1,2])
            FirstAttribute = 'CHA'
            if decision == 1:
                statPicker(characterAttributes,attributeValues,['CHA'],['WIS'])
                skills['Arcana'].append(5)
                skills['Bluff'].append(5)
                skills['Endurance'].append(5)
                skills['Insight'].append(5)
            if decision == 2:
                statPicker(characterAttributes,attributeValues,['CHA'],['STR'])
                skills['Arcana'].append(5)
                skills['Athletics'].append(5)
                skills['History'].append(5)
                skills['Intimidate'].append(5)
        if (args.character_class == 'Sorcerer'):
            hitPoints['level_0'] = 7
            hitPoints['perLevel'] = 5
            hitPoints['dailySurges'] = 6
            characterDefenses['WILL'].append(2)
            weaponProficiencies.append("simple_melee")
            weaponProficiencies.append("simple_ranged")
            decision = random.choice([1,2])
            FirstAttribute = 'CHA'
            if decision == 1:
                statPicker(characterAttributes,attributeValues,['CHA'],['WIS'])
                skills['Arcana'].append(5)
                skills['Bluff'].append(5)
                skills['Endurance'].append(5)
                skills['Insight'].append(5)
            if decision == 2:
                statPicker(characterAttributes,attributeValues,['CHA'],['STR'])
                skills['Arcana'].append(5)
                skills['Athletics'].append(5)
                skills['History'].append(5)
                skills['Intimidate'].append(5)

        if (args.character_class == 'Barbarian'):
            hitPoints['level_0'] = 9
            hitPoints['perLevel'] = 6
            hitPoints['dailySurges'] = 8
            characterDefenses['FORT'].append(2)
            weaponProficiencies.append("simple_melee")
            weaponProficiencies.append("military_melee")
            armorProficiencies.append("leather")
            armorProficiencies.append("hide")
            decision = random.choice([1,2])
            FirstAttribute = 'STR'
            if decision == 1:
                statPicker(characterAttributes,attributeValues,['CON'],['CHA'])
                skills['Athletics'].append(5)
                skills['Endurance'].append(5)
                skills['Perception'].append(5)
            if decision == 2:
                statPicker(characterAttributes,attributeValues,['CHA'],['CON'])
                skills['Athletics'].append(5)
                skills['Intimidate'].append(5)
                skills['Perception'].append(5)
        if (args.character_class == 'Monk'):
            hitPoints['level_0'] = 7
            hitPoints['perLevel'] = 5
            hitPoints['dailySurges'] = 7
            characterDefenses['WILL'].append(1)
            characterDefenses['FORT'].append(1)
            characterDefenses['REF'].append(1)
            weaponProficiencies.append("club")
            weaponProficiencies.append("dagger")
            weaponProficiencies.append("quarterstaff")
            weaponProficiencies.append("shuriken")
            weaponProficiencies.append("sling")
            weaponProficiencies.append("spear")
            decision = random.choice([1,2])
            FirstAttribute = 'DEX'
            if decision == 1: #Centered Breath
                statPicker(characterAttributes,attributeValues,['DEX'],['WIS'],['STR'])
                characterDefenses['FORT'].append(1)
                skills['Athletics'].append(5)
                skills['Acrobatics'].append(5)
                skills['Perception'].append(5)
                skills['Insight'].append(5)
            if decision == 2: #Stone fist
                statPicker(characterAttributes,attributeValues,['DEX'],['STR'],['WIS'])
                characterDefenses['WILL'].append(1)
                skills['Athletics'].append(5)
                skills['Acrobatics'].append(5)
                skills['Perception'].append(5)
                skills['Endurance'].append(5)

        # print "Here are the stats:"
        # print 'STR:',characterAttributes['STR'], 'Strength Modifier:', attributeModifier(characterAttributes['STR'])
        # print 'DEX:',characterAttributes['DEX'], 'Dexterity Modifier:', attributeModifier(characterAttributes['DEX'])
        # print 'CON:',characterAttributes['CON'], 'Constitution Modifier:', attributeModifier(characterAttributes['CON'])
        # print 'INT:',characterAttributes['INT'], 'Intelligence Modifier:', attributeModifier(characterAttributes['INT'])
        # print 'WIS:',characterAttributes['WIS'], 'Wisdom Modifier:', attributeModifier(characterAttributes['WIS'])
        # print 'CHA:',characterAttributes['CHA'], 'Charisma Modifier:', attributeModifier(characterAttributes['CHA'])
        # print ""
        # print "Apply Racial Modifications"
        if args.character_race == 'random':
            args.character_race = random.choice(characterRaces)

        print "Creating a", args.character_race, args.character_class
        if args.character_race == "Dragonborn":
            skills['History'].append(2)
            skills['Intimidate'].append(2)
            characterAttributes['STR'].append(2)
            characterAttributes['CHA'].append(2)
        if args.character_race == "Dwarf":
            weaponProficiencies.append("throwing_hammer")
            weaponProficiencies.append("warhammer")
            skills['Dungeoneering'].append(2)
            skills['Endurance'].append(2)
            characterAttributes['CON'].append(2)
            characterAttributes['WIS'].append(2)
        if args.character_race == "Eladrin":
            weaponProficiencies.append("longsword")
            characterDefenses['WILL'].append(1)
            skills['Arcana'].append(2)
            skills['History'].append(2)
            characterAttributes['DEX'].append(2)
            characterAttributes['INT'].append(2)
        if args.character_race == "Elf":
            weaponProficiencies.append("longbow")
            weaponProficiencies.append("shortbow")
            skills['Nature'].append(2)
            skills['Perception'].append(2)

            characterAttributes['DEX'].append(2)
            characterAttributes['WIS'].append(2)
        if args.character_race == "Half-Elf":
            characterAttributes['CON'].append(2)
            characterAttributes['CHA'].append(2)
        if args.character_race == "Tiefling":
            characterAttributes['INT'].append(2)
            characterAttributes['CHA'].append(2)
        if args.character_race == "Human":
            characterDefenses['FORT'].append(1)
            characterDefenses['REF'].append(1)
            characterDefenses['WILL'].append(1)
            if menu_option == '1':
                print "Not ready to manually edit human stats"
            if menu_option == '2':
                print "FirstAttribute", FirstAttribute
                characterAttributes[FirstAttribute].append(2)

        updateAttributes(characterAttributes)

        print 'STR:',characterAttributes['STR'], 'Strength Modifier:', attributeModifier(characterAttributes['STR'])
        print 'DEX:',characterAttributes['DEX'], 'Dexterity Modifier:', attributeModifier(characterAttributes['DEX'])
        print 'CON:',characterAttributes['CON'], 'Constitution Modifier:', attributeModifier(characterAttributes['CON'])
        print 'INT:',characterAttributes['INT'], 'Intelligence Modifier:', attributeModifier(characterAttributes['INT'])
        print 'WIS:',characterAttributes['WIS'], 'Wisdom Modifier:', attributeModifier(characterAttributes['WIS'])
        print 'CHA:',characterAttributes['CHA'], 'Charisma Modifier:', attributeModifier(characterAttributes['CHA'])

        updateSkills(skills, characterAttributes)


        print "Skills:"
        print skills
        print "Bonuses:"
        print characterDefenses
        print "armorProficiencies:"
        print armorProficiencies
        print "weaponProficiencies:"
        print weaponProficiencies
        # print ""
        # print "Hit Point Time"

        # if (args.character_class == 'Tough'):
        #     hitPoints['MaxHP'] = 10 + attributeModifier(characterAttributes['CON'])
        #     hitPoints['CurHP'] = hitPoints['MaxHP']
        # elif (args.character_class == 'Fast' or args.character_class == 'Strong'):
        #     hitPoints['MaxHP'] = 8 + attributeModifier(characterAttributes['CON'])
        #     hitPoints['CurHP'] = hitPoints['MaxHP']
        # else:
        #     hitPoints['MaxHP'] = 6 + attributeModifier(characterAttributes['CON'])
        #     hitPoints['CurHP'] = hitPoints['MaxHP']
        print
        characterLevelAbilities = {}

        characterAbilities = {}
        characterAbilities['InitiativeModifier'] = attributeModifier(characterAttributes['DEX'])
        characterAbilities['Defense'] = 10 + attributeModifier(characterAttributes['DEX'])
        if args.last_name == "":
            # last_name = args.last_name
            last_name = name_generator.get_last_name()
        else:
            last_name = args.last_name
        if args.first_name == "":
            pass
            # first_name = args.first_name
            first_name = name_generator.get_first_name(character_gender)
        else:
            first_name = args.first_name
        character = {   "class":args.character_class,
                        "initiative":[
                            0
                            ],
                        "defenses":characterDefenses,
                        "hit points":hitPoints,
                        "gender":character_gender,
                        "name":{
                            "last":last_name,
                            "first":first_name},
                        "abilities":characterAttributes,
                        "equipment":[None],
                        "skills":skills,
                        "equiped":{
                            "armor":None,
                            "right_hand":None,
                            "left_hand":None},
                            "armor_Proficiencies":armorProficiencies,
                            "weapon_Proficiencies":weaponProficiencies,
                        # "attack_details":
                            # {"weapon_name": "unarmed", "complexity": "simple", "type": "melee", "damage_die": "1d3", "damage_type": "non-leathal", "weight": "0"}
                            # {"unarmed":"1d4"}
                        }
    print "-------------------------------------------------------------------------------"
    json_data = json.dumps(character)
    # print json.dumps(character,sort_keys=True, indent=4)
    if (menu_option == '4'):
        conn = sqlite3.connect('dnd_game_4e.sqlite')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS characters
                     (
                     character_name text UNIQUE,
                     player_name text,
                     character_data text
                     )''')
        c.execute('INSERT INTO characters VALUES (?,?,?)', (last_name+"_"+first_name,args.player_name,json_data),)
        conn.commit()
        conn.close()


    # print json.dumps([newCharacter,characterAttributes,hitPoints,characterAbilities], sort_keys=True, indent=4)

if __name__ == "__main__":
    main()
