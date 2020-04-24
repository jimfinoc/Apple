import DnD_Character_Graphic #as character_class


#character_class
class Stats(object):
    def __init__(self):
        self.STR = 10
        self.DEX = 10
        self.CON = 10
        self.WIS = 10
        self.INT = 10
        self.CHA = 10
    def mod(self,value = 10):
        return ( value // 2 - 5)

class Character_Class(DnD_Character_Graphic.CharacterGraphic,object):
    def __init__(self,screen=None, color=DnD_Character_Graphic.WHITE, center= [0,0], direction = [0],character_type = 1):
        super(Character_Class,self).__init__(screen, color, center, direction,character_type)
        self._character_weight = 100
        self._character_inventory = []
        self.stats = Stats()
        # print ("player created")

    def total_weight(self):
        return ( self.character_weight() + self.equipment_weight() )

    def character_weight(self):
        return self._character_weight

    def equipment_weight(self):
        equipment_weight = 0
        for each in self._character_inventory:
            try:
                equipment_weight += each["weight"]
            except:
                pass
        return equipment_weight

if __name__ == '__main__':  # single underscore
    test = Character()
    test.stats.STR = 6
    test.stats.DEX = 12
    test.stats.CON = 10
    test.stats.WIS = 3
    test.stats.INT = 4
    test.stats.CHA = 7
    print (test.stats.STR, test.stats.mod(test.stats.STR) )
    print (test.stats.DEX, test.stats.mod(test.stats.DEX) )
    print (test.stats.CON, test.stats.mod(test.stats.CON) )
    print (test.stats.WIS, test.stats.mod(test.stats.WIS) )
    print (test.stats.INT, test.stats.mod(test.stats.INT) )
    print (test.stats.CHA, test.stats.mod(test.stats.CHA) )
