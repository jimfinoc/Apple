import json

dictionary_map = {}
max_x = 10
max_y = 10


def print_dict(dictionary_map,max_x,max_y):
    for i in range (max_x):
        for j in range (max_y):
            print dictionary_map[i,j][0],
        print "  ",
        for j in range (max_y):
            print "\t",dictionary_map[i,j][1],

        print ""

def look(dictionary_map, location, step):
    # print location
    step = step + 1
    # print step
    possible = (
        (location[0]+1,location[1]),
        (location[0]-1,location[1]),
        (location[0],location[1]+1),
        (location[0],location[1]-1),
        )
    print "possible",
    print possible
    print "step",
    print step
    for direction in possible:
        if direction in dictionary_map:
            # if dictionary_map[direction][1] == -1 :
            if dictionary_map[direction][1] > step:
                dictionary_map[direction][1] = step
                print ""
                look(dictionary_map, direction,step)
                # print "dictionary_map"
                # print_dict(dictionary_map,max_x,max_y)
                # print dictionary_map
                print "direction",
                print direction
                print "step",
                print step
            else:
                print direction, "already looked at space"

        else:
            print direction, "not in dictionary_map"
            print_dict(dictionary_map,max_x,max_y)


    # print dictionary_map


for i in range (max_x):
    for j in range (max_y):
        dictionary_map[i,j]= [".",100]
        # dictionary_map[i+max_x*j]="."

# master_list[2][3] = "X"
# master_list[6][7] = "C"
dictionary_map[5,7] = ["X",-2]
location = (1,3)
dictionary_map[location] = ["O",-2]

dictionary_map[3,3] = ["M",-1]
dictionary_map[3,4] = ["M",-1]
dictionary_map[3,5] = ["M",-1]
dictionary_map[3,6] = ["M",-1]
dictionary_map[4,3] = ["M",-1]
dictionary_map[5,3] = ["M",-1]
dictionary_map[6,3] = ["M",-1]
dictionary_map[3,7] = ["M",-1]
dictionary_map[3,8] = ["M",-1]
# dictionary_map[location] = ["O",0]
# dictionary_map[location] = ["O",0]

# print_dict(dictionary_map,max_x,max_y)

print ""
print "testing"
print ""
print "dictionary_map"
print_dict(dictionary_map,max_x,max_y)
# print dictionary_map
print "location"
print location
print "step"
print 0
print ""

look(dictionary_map,location,0)


# with open('map.json', 'w') as f:
    # pass
    # json.dump(dictionary_map, f)


# master_list =
# # for each_list in master_list:
#     for each in each_list:
#         print each,
#     print ""
