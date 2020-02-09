import json

dictionary_map = {}
max_x = 10
max_y = 10


def print_dict(dictionary_map,max_x,max_y):
    for j in range (max_y):
        for i in range (max_x):
            print dictionary_map[i,j][0],
        print "\t",
        for i in range (max_x):
            # print "\t",dictionary_map[i,j][1],
            if isinstance( dictionary_map[i,j][1] , str):
                print("% 3s" %(dictionary_map[i,j][1])),
            else:
                print("% 3d" %(dictionary_map[i,j][1])),
        print "\t",
        for i in range (max_x):
            if isinstance( dictionary_map[i,j][2] , str):
                print("% 1s" %(dictionary_map[i,j][2])),
            else:
                print("% 1d" %(dictionary_map[i,j][2])),



        print ""
def find_goals(dictionary_map):
    pass

E = 0
W = 1
S = 2
N = 3
def deceide(dictionary_map, goal, step):
    step = step + 1
    possible = (
        (goal[0]+1,goal[1]  ),
        (goal[0]-1,goal[1]  ),
        (goal[0]  ,goal[1]+1),
        (goal[0]  ,goal[1]-1),
        )
    print goal[0],goal[1]
    best = N
    second_best = N
    third_best = N
    # Are we next to the orgin?
    if possible[N] in dictionary_map:
        if dictionary_map[possible[N]][2] == "O":
            return
    if possible[E] in dictionary_map:
        if dictionary_map[possible[E]][2] == "O":
            return
    if possible[S] in dictionary_map:
        if dictionary_map[possible[S]][2] == "O":
            return
    if possible[W] in dictionary_map:
        if dictionary_map[possible[W]][2] == "O":
            return

    # What is the best path back to our origin?
    if possible[N] in dictionary_map:
        best = N
    elif possible[E] in dictionary_map:
        best = E
    elif possible[W] in dictionary_map:
        best = W
    elif possible[S] in dictionary_map:
        best = S
    if possible[N] in dictionary_map:
        second_best = N
    elif possible[E] in dictionary_map:
        second_best = E
    elif possible[W] in dictionary_map:
        second_best = W
    elif possible[S] in dictionary_map:
        second_best = S
    if possible[N] in dictionary_map:
        third_best = N
    elif possible[E] in dictionary_map:
        third_best = E
    elif possible[W] in dictionary_map:
        third_best = W
    elif possible[S] in dictionary_map:
        third_best = S

    if possible[S] in dictionary_map:
        if dictionary_map[possible[S]][1] < dictionary_map[possible[best]][1]:
            second_best = best
            best = S
    if possible[E] in dictionary_map:
        if dictionary_map[possible[E]][1] < dictionary_map[possible[best]][1]:
            third_best = second_best
            second_best = best
            best = E
    elif dictionary_map[possible[E]][1] < dictionary_map[possible[second_best]][1]:
        third_best = second_best
        second_best = E

    if dictionary_map[possible[W]][1] < dictionary_map[possible[best]][1]:
        third_best = second_best
        second_best = best
        best = W
    elif dictionary_map[possible[W]][1] < dictionary_map[possible[second_best]][1]:
        third_best = second_best
        second_best = W

    print "DeceidingDeceidingDeceidingDeceidingDeceiding",step
    dictionary_map[possible[best]][2] = "*"
    deceide(dictionary_map, possible[best], step)
    if dictionary_map[possible[best]] == dictionary_map[possible[second_best]]:
        dictionary_map[possible[second_best]][2] = "*"
        deceide(dictionary_map, possible[second_best], step)
    if dictionary_map[possible[best]] == dictionary_map[possible[third_best]]:
        dictionary_map[possible[third_best]][2] = "*"
        deceide(dictionary_map, possible[third_best], step)


        # if dictionary_map[possible[N]] < dictionary_map[possible[W]]:
            # if dictionary_map[possible[N]] < dictionary_map[possible[E]]:
            # pass
    # elif dictionary_map[possible[N]] < dictionary_map[possible[S]]:

        # if direction in dictionary_map:
        #     # if dictionary_map[direction][1] == -1 :
        #     if dictionary_map[direction][1] == "M":
        #         print "Wall"
        #     elif dictionary_map[direction][1] == "O":
        #         print "Origin"
        #     elif dictionary_map[direction][1] == "X":
        #         print "Destination"
        #     elif dictionary_map[direction][1] > step:
        #         dictionary_map[direction][1] = step
        #         print ""
        #         look(dictionary_map, direction,step)



def look(dictionary_map, origin, step):
    # print origin
    step = step + 1
    # print step
    possible = (
        (origin[0]+1,origin[1]  ),
        (origin[0]-1,origin[1]  ),
        (origin[0]  ,origin[1]+1),
        (origin[0]  ,origin[1]-1),
        )
    # print "possible",
    # print possible
    # print "step",
    # print step
    for direction in possible:
        if direction in dictionary_map:
            # if dictionary_map[direction][1] == -1 :
            if dictionary_map[direction][1] == "M":
                print "Wall"
            elif dictionary_map[direction][1] == "O":
                print "Origin"
            elif dictionary_map[direction][1] == "X":
                print "Destination"
            elif dictionary_map[direction][1] > step:
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
        dictionary_map[i,j]= [".",1000,"."]
        # dictionary_map[i+max_x*j]="."

# master_list[2][3] = "X"
# master_list[6][7] = "C"

goal = [(4,4),(6,7)]
dictionary_map[goal[0] ] = ["X","X","X"]
dictionary_map[goal[1] ] = ["X","X","X"]

origin = (1,3)
# origin = (0,0)
dictionary_map[origin] = ["O","O","O"]

dictionary_map[3,3] = ["M","M","M"]
dictionary_map[3,4] = ["M","M","M"]
dictionary_map[3,5] = ["M","M","M"]
dictionary_map[3,6] = ["M","M","M"]
dictionary_map[4,3] = ["M","M","M"]
dictionary_map[5,3] = ["M","M","M"]
dictionary_map[6,3] = ["M","M","M"]
dictionary_map[3,7] = ["M","M","M"]
dictionary_map[3,8] = ["M","M","M"]

# print ""
# print "testing"
# print ""
# print "dictionary_map"
# print_dict(dictionary_map,max_x,max_y)
# print dictionary_map
# print "origin"
# print origin
# print "step"
# print 0
# print ""

# print ""
look(dictionary_map,origin,0)
print ""
print "Done Looking"
print ""
deceide(dictionary_map, goal[0], 0)
# deceide(dictionary_map, goal[1], 0)
print "Done Deceiding"
print ""

print("% 10s" %"Map"),
print("% 36s" %"Steps"),
print("% 40s" %"Path"),
print ""
# print "Map","Steps","Path"
print_dict(dictionary_map,max_x,max_y)


# with open('map.json', 'w') as f:
    # pass
    # json.dump(dictionary_map, f)


# master_list =
# # for each_list in master_list:
#     for each in each_list:
#         print each,
#     print ""
