import json
import csv
import sqlite3

# print("")

# a Python object (dict):
# x = {
#   "weapon_name": "Club",
#   "weapon_type":["melee"],
#   "description" : "Like a heavy peice of wood.",
#   "complexity":"Simple",
#   "cost": "10",
#   "damage_type": ["bludgeoning"],
#   "weapon_property": ["not_heavy"],
#   "weight": "2",
#   "damage": "1d4",
# }
# z = {
#   "complexity":"Simple",
#   "type":["Melee"],
#   "weapon_type": "Dagger",
#   "cost": 200,
#   "damage": "1d4",
#   "damage_type": ["piercing"],
#   "weight": 1,
#   "properties": ["Finesse", "Light", "Thrown"],
# }

# y = [x,]

# convert into JSON:
# z = json.dumps(x)

# the result is a JSON string:
# print (x)
# print (z)

# with open('dnd_weapons.txt', 'w') as outfile:
    # json.dump(x, outfile)

# with open('dnd_weapons.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(x)


#print (x.keys())
# csv_columns = ['No','Name','Country']
csv_columns = ['weapon_name','complexity','type','copper_cost','damage_die','damage_type','weight']


# csv_columns = x.keys()/
# dict_data = y
csv_file = "dnd_weapons.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in dict_data:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")
#

weapon_type_list = []
with open(csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=csv_columns, delimiter=',', quotechar='|')
    #reader = csv.DictReader(csvfile, fieldnames=csv_columns)
    # reader = csv.DictReader(csvfile)
    #print (reader)
    # print ("")
    number = 0
    for row in reader:
        number += 1
        #print(', '.join(row))
        loaded_data = dict(row)
        weapon_type_list.append(loaded_data)
        dumped_data = json.dumps(loaded_data)
        # print ("weapon", number, ":" , dumped_data)
        # weaponList.append(dict(row))
# print (weaponList)
#
# print("")
# for each in weaponList:
#     #print (each)
#     pass


# print("")
conn = sqlite3.connect('dnd_game.sqlite')
c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS weapon_types
#              (
#              weapon_name text UNIQUE,
#              weapon_data text
#              )''')
# conn.commit()

# print (json.dumps(x))
# print (type(json.dumps(x)))
# print("")

table_name = "weapon_types"
# c.execute('INSERT INTO weapon_types VALUES (?,?,?, ?,?,?, ?,?,?)', (x["weapon_name"],x["weapon_type"],x["description"],x["complexity"],x["cost"],x["weapon_property"],x["damage_type"],x["weight"],x['damage'],) )
# c.execute('INSERT INTO weapon_types VALUES (?,?,?, ?,?,?, ?,?,?)', (x))
# c.execute('INSERT INTO weapon_types VALUES (?,?)', (x["weapon_name"],json.dumps(x)),)
# for x in weapon_type_list:
#     name = x["weapon_name"]
#     data = json.dumps(x)
#     print ("name")
#     print (name)
#     print ("data")
#     print (data)
#     c.execute('INSERT INTO weapon_types VALUES (?,?)', (name,data))
#     conn.commit()


c.execute('SELECT * FROM weapon_types')
conn.commit()
rows = c.fetchall()
weapons = []

for each in rows:
    # print (json.loads(each[1]))
    pass
    try:
        weapons.append(json.loads(each[1]))
    except:
        # name = each[0]
        # weapons.append({"weapon_name":name})
        # data = json.dumps(each[0])
        # c.execute("UPDATE weapon_types SET weapon_data = ? WHERE weapon_name =?", (name,data))
        # c.execute('INSERT INTO weapon_types VALUES (?,?)', (x["weapon_name"],json.dumps(x)),)
        print ("error!")
    # print ("1")
for each in weapons:
    # pass
    print (each)

conn.commit()
conn.close()
