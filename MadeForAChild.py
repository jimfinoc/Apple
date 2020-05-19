import os
temp = os.system("clear")
print("\033[6;3HHello")
print("\033[1;10HMy Name is Katie")


def lPrint(x,y,text):
    print("\033["+str(x)+";"+str(y)+"H"+str(text) )

lPrint(1,1,"Yes")
lPrint(3,3,12)
