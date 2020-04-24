from random import randint
import Tkinter as tk
import numpy as np
import math
import time
import re

CountToNextAttack = 5

class charClass:

    def __init__(self, nameValue="Test", xValue=0, yValue=0):
        self.name = nameValue
        self.x = xValue
        self.y = yValue
        self.direction = 0
        self.velocity = 0
        self.radius = 25
        self.characterClass = "None"
        self.circleID = -1
        self.graphicIDs = []
        self.team = "None"
        self.tasks = []
        self.healthBarIDs = 0
        self.health = randint(1,6)+randint(1,6)+randint(1,6)
        self.healthMax = self.health
        self.Critical = 20
        self.readyCounterToNextAttack = 5
        self.teamColor = "#ffffff"
        self.ammo = 1
        self.rangeWeaponDistance = 250




    def assignClass (self,characterClass):
        self.characterClass = characterClass

    def attackRange(self,defendingCharacterName,characterDictionary):
        if self.readyCounterToNextAttack >= CountToNextAttack:
            if self.ammo > 0:
                attackRoll = randint(1,20)
                self.readyCounterToNextAttack = 0
                # print "Attack Roll is ",
                # print attackRoll
                if attackRoll == 1:
                    return False
                elif attackRoll >= self.Critical:
                    return True
                elif attackRoll >= characterDictionary[defendingCharacterName].defense():
                    return True
                self.ammo -= 1
            return False

    def attackMelee(self,defendingCharacterName,characterDictionary):
        if self.readyCounterToNextAttack >= CountToNextAttack:
            attackRoll = randint(1,20)
            self.readyCounterToNextAttack = 0
            # print "Attack Roll is ",
            # print attackRoll
            if attackRoll == 1:
                return False
            elif attackRoll >= self.Critical:
                return True
            elif attackRoll >= characterDictionary[defendingCharacterName].defense():
                return True
        return False

    def attackDamage(self):
        return randint(1,2)

    def defense(self):
        return 10

    def takeDamage(self,damageToRemoveFromHealth):
        self.health += -damageToRemoveFromHealth
        return damageToRemoveFromHealth

if __name__ == "__main__":
    # execute only if run as a script
    example = charClass()
    print example
