#character_class
class character_class:
    character_weight = 100
    def __init__(self):
        self._character_weight = 100
        self._character_inventory = []
        print ("player created")


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
