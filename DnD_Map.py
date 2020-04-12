import sqlite3
conn = sqlite3.connect('dnd_game.sqlite')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS map
             (
             coordinates text UNIQUE,
             description text
             )''')


print ("")
print ("everything in the table")
c.execute('SELECT * FROM map')
conn.commit()
rows = c.fetchall()
print (rows)
print ("")
# for each in rows:
    # print (each)

x = 2
y = 1
position = (str(x)+","+str(y),)
# position = ('0,-1',)
terrain = ('grass',)

print ("")
print ("now working on the table")
c.execute('SELECT * FROM map WHERE coordinates=?', position)
conn.commit()

rows = c.fetchall()
print (rows)
if not rows:
    print (position, "is new!")
    c.execute("INSERT INTO map VALUES (?,?)", (position[0],terrain[0],) )
    conn.commit()
else:
    print (position, "already exists!")
    c.execute("UPDATE map SET description = ? WHERE coordinates =?", (terrain[0],position[0]),)
    conn.commit()

print ("")
print ("everything in our range of:")
x_range = 2
y_range = 2
print ("x from", -x_range," to ", x_range)
print ("y from", -y_range," to ", y_range)
c.execute('SELECT * FROM map')
conn.commit()
rows = c.fetchall()
# print (rows)
# print ("")

# for each in rows:
    # print (each)
for y in range(y_range,-y_range-1,-1):
    for x in range(-x_range,x_range+1,1):
        position = (str(x)+","+str(y),)
        c.execute('SELECT * FROM map WHERE coordinates=?', position)
        conn.commit()
        data = c.fetchall()
        if not data:
            print (".",)
        else:
            print (data[0][1][0]),
    print ("")

# c.execute("INSERT INTO map VALUES ('1,0','grass')")

# Save (commit) the changes

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
