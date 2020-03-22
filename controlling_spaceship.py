import Tkinter as tk
import time
import random
import math
import pygame



class CharacterGraphic(object):
    class_screenHeight = 400
    class_screenWidth = 400
    c = [
        0,-12,
        48,-12,
        48,12,
        0,12,
        0,24,
        -24,24,
        -24,-24,
        0,-24,
        0,-12,
        ]
    d = [
        24, -12,
        24,  12,
        -24,  12,
        -24, -12,
        24, -12,
    ]
    def __init__(self, canvas, angle, *args, **kwargs):
        self.canvas = canvas
        self.alive = True
        self.dying = False
        # self.id = canvas.create_rectangle([self.x+1,self.y+1,self.x-1,self.y-1], **kwargs)
        self.id = canvas.create_oval(*args, **kwargs)
        # self.id = canvas.create_window(*args, **kwargs)
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        self.x = (x1 + x2 ) / 2
        self.y = (y1 + y2 ) / 2
        print "x,y"
        print self.x,self.y
        print ("x1, y1, x2, y2")
        print (x1, y1, x2, y2)
        self.vx = 0
        self.vy = 0
        self.color = self.canvas.gettags(self.id)[0]
        self.canvas.addtag_withtag("main", self.id)
        # self.id2 = canvas.create_oval(*args, **kwargs)
        self.health = 100
        # self.box = canvas.create_rectangle(100,100)
        # angle = 0
        self.angle = 0
        coordinates1 = [
            self.x + self.c[0]*math.cos(self.angle) - self.c[1] * math.sin(self.angle), self.y + self.c[0]*math.sin(self.angle) + self.c[1]*math.cos(self.angle),
            self.x + self.c[2]*math.cos(self.angle) - self.c[3] * math.sin(self.angle), self.y + self.c[2]*math.sin(self.angle) + self.c[3]*math.cos(self.angle),
            self.x + self.c[4]*math.cos(self.angle) - self.c[5] * math.sin(self.angle), self.y + self.c[4]*math.sin(self.angle) + self.c[5]*math.cos(self.angle),
            self.x + self.c[6]*math.cos(self.angle) - self.c[7] * math.sin(self.angle), self.y + self.c[6]*math.sin(self.angle) + self.c[7]*math.cos(self.angle),
            self.x + self.c[8]*math.cos(self.angle) - self.c[9] * math.sin(self.angle), self.y + self.c[8]*math.sin(self.angle) + self.c[9]*math.cos(self.angle),
            self.x + self.c[10]*math.cos(self.angle) - self.c[11] * math.sin(self.angle), self.y + self.c[10]*math.sin(self.angle) + self.c[11]*math.cos(self.angle),
            self.x + self.c[12]*math.cos(self.angle) - self.c[13] * math.sin(self.angle), self.y + self.c[12]*math.sin(self.angle) + self.c[13]*math.cos(self.angle),
            self.x + self.c[14]*math.cos(self.angle) - self.c[15] * math.sin(self.angle), self.y + self.c[14]*math.sin(self.angle) + self.c[15]*math.cos(self.angle),
            self.x + self.c[16]*math.cos(self.angle) - self.c[17] * math.sin(self.angle), self.y + self.c[16]*math.sin(self.angle) + self.c[17]*math.cos(self.angle),
            ]
        coordinates2 = [
            self.x + self.d[0]*math.cos(self.angle) - self.d[1] * math.sin(self.angle), self.y + self.d[0]*math.sin(self.angle) + self.d[1]*math.cos(self.angle),
            self.x + self.d[2]*math.cos(self.angle) - self.d[3] * math.sin(self.angle), self.y + self.d[2]*math.sin(self.angle) + self.d[3]*math.cos(self.angle),
            self.x + self.d[4]*math.cos(self.angle) - self.d[5] * math.sin(self.angle), self.y + self.d[4]*math.sin(self.angle) + self.d[5]*math.cos(self.angle),
            self.x + self.d[6]*math.cos(self.angle) - self.d[7] * math.sin(self.angle), self.y + self.d[6]*math.sin(self.angle) + self.d[7]*math.cos(self.angle),
            self.x + self.d[8]*math.cos(self.angle) - self.d[9] * math.sin(self.angle), self.y + self.d[8]*math.sin(self.angle) + self.d[9]*math.cos(self.angle),

        ]
        print "coordinates1"
        print coordinates1
        print "coordinates2"
        print coordinates2

        print "*args"
        print args
        print "**kwargs"
        print kwargs

        # self.shipbody = canvas.create_polygon(coordinates1, outline="black", fill="green",width = 2)
        self.shipbody = canvas.create_polygon(coordinates1, **kwargs)
        # self.shipcabin = canvas.create_polygon(coordinates2, outline="black", fill="yellow",width = 2)
        self.shipcabin = canvas.create_polygon(coordinates2, fill = "white", **kwargs)
        # self.shipcabin = canvas.create_polygon(coordinates2, fill = "yellow", **kwargs)
        # self.shipcabin = None
        # self.HealthId1 = canvas.create_arc(*args, start=359,extent=0, style='chord', fill='black', **kwargs)
        self.HealthId1 = None
        self.HealthId2 = None
        # self.HealthId2 = canvas.create_arc(*args, start=0,extent=359, style='chord', fill=self.color, **kwargs)

        # self.vx = 0
        # self.vy = 0
        # self.vx = random.randint(1,5)
        # self.vy = random.randint(1,5)

    def boundAngle(self,x):
        y = x % 360
        return y

    def turn(self, degrees):
        self.angle = self.angle + 2 * math.pi * degrees / 360
        coordinates1 = [
            self.x + self.c[0]*math.cos(self.angle) - self.c[1] * math.sin(self.angle), self.y + self.c[0]*math.sin(self.angle) + self.c[1]*math.cos(self.angle),
            self.x + self.c[2]*math.cos(self.angle) - self.c[3] * math.sin(self.angle), self.y + self.c[2]*math.sin(self.angle) + self.c[3]*math.cos(self.angle),
            self.x + self.c[4]*math.cos(self.angle) - self.c[5] * math.sin(self.angle), self.y + self.c[4]*math.sin(self.angle) + self.c[5]*math.cos(self.angle),
            self.x + self.c[6]*math.cos(self.angle) - self.c[7] * math.sin(self.angle), self.y + self.c[6]*math.sin(self.angle) + self.c[7]*math.cos(self.angle),
            self.x + self.c[8]*math.cos(self.angle) - self.c[9] * math.sin(self.angle), self.y + self.c[8]*math.sin(self.angle) + self.c[9]*math.cos(self.angle),
            self.x + self.c[10]*math.cos(self.angle) - self.c[11] * math.sin(self.angle), self.y + self.c[10]*math.sin(self.angle) + self.c[11]*math.cos(self.angle),
            self.x + self.c[12]*math.cos(self.angle) - self.c[13] * math.sin(self.angle), self.y + self.c[12]*math.sin(self.angle) + self.c[13]*math.cos(self.angle),
            self.x + self.c[14]*math.cos(self.angle) - self.c[15] * math.sin(self.angle), self.y + self.c[14]*math.sin(self.angle) + self.c[15]*math.cos(self.angle),
            self.x + self.c[16]*math.cos(self.angle) - self.c[17] * math.sin(self.angle), self.y + self.c[16]*math.sin(self.angle) + self.c[17]*math.cos(self.angle)
            ]
        coordinates2 = [
            self.x + self.d[0]*math.cos(self.angle) - self.d[1] * math.sin(self.angle), self.y + self.d[0]*math.sin(self.angle) + self.d[1]*math.cos(self.angle),
            self.x + self.d[2]*math.cos(self.angle) - self.d[3] * math.sin(self.angle), self.y + self.d[2]*math.sin(self.angle) + self.d[3]*math.cos(self.angle),
            self.x + self.d[4]*math.cos(self.angle) - self.d[5] * math.sin(self.angle), self.y + self.d[4]*math.sin(self.angle) + self.d[5]*math.cos(self.angle),
            self.x + self.d[6]*math.cos(self.angle) - self.d[7] * math.sin(self.angle), self.y + self.d[6]*math.sin(self.angle) + self.d[7]*math.cos(self.angle),
            self.x + self.d[8]*math.cos(self.angle) - self.d[9] * math.sin(self.angle), self.y + self.d[8]*math.sin(self.angle) + self.d[9]*math.cos(self.angle),
        ]
        print "coordinates1"
        print map(int,coordinates1)
        print "coordinates2"
        print coordinates2
        # self.canvas.coords(self.shipbody, *map(int,coordinates1))
        self.canvas.coords(self.shipbody, *coordinates1)
        # self.shipbody(coordinates1)
        self.canvas.coords(self.shipcabin, *coordinates2)

    def returnHealth(self):
        pass
    #     if self.alive:
    #         print self.color, "is alive",
    #         if self.health < 0:
    #             self.dying = True
    #     if self.dying:
    #         print "but", self.color, "is dying",
    #     if self.alive:
    #         print ""
    #     return self.health

    # def updateHealthGraphic(self,health):
    #     if self.alive:
    #         self.health = health
    #         if self.health >= 100:
    #             self.canvas.itemconfig(self.HealthId1, start=359,extent=0)
    #             self.canvas.itemconfig(self.HealthId2, start=0,extent=359)
    #         elif self.health <= 0:
    #             self.canvas.itemconfig(self.HealthId1, start=0,extent=359)
    #             self.canvas.itemconfig(self.HealthId2, start=359,extent=0)
    #         else:
    #             print "health is ", health
    #             angle1 = self.health * 180 / 100 + 90
    #             angle2 = self.health * 360 / 100
    #             angle3 = self.health * 360 / 100 - 360
    #             one = -self.boundAngle(angle1 )
    #             two = -self.boundAngle(-angle2)
    #             three = self.boundAngle(angle3)
    #             self.canvas.itemconfig(self.HealthId1, start=one)
    #             self.canvas.itemconfig(self.HealthId1, extent=two)
    #             self.canvas.itemconfig(self.HealthId2, start=one)
    #             self.canvas.itemconfig(self.HealthId2, extent=three)

    def move(self):
        if self.alive:
            # x1, y1, x2, y2 = self.canvas.bbox(self.id)
            # if x2 > self.class_screenWidth:
            #     # self.vx = 0
            #     self.vx = random.randint(-5,-4)
            # if x1 < 0:
            #     # self.vx = 0
            #     self.vx = random.randint(4,5)
            #
            # if y2 > self.class_screenHeight:
            #     # self.vy = 0
            #     self.vy = random.randint(-5,-4)
            #
            # if y1 < 0:
            #     # self.vy = 0
            #     self.vy = random.randint(4,5)
            # if self.health == 0:
            #     self.vy = 0
            #     self.vx = 0

            self.vx = 1 * math.cos(self.angle)
            self.vy = 1 * math.sin(self.angle)


            self.canvas.move(self.id, self.vx, self.vy)
            self.canvas.move(self.shipbody, self.vx, self.vy)
            self.canvas.move(self.shipcabin, self.vx, self.vy)

            x1, y1, x2, y2 = self.canvas.bbox(self.id)
            self.x = (x1 + x2 ) / 2
            self.y = (y1 + y2 ) / 2
            # self.canvas.move(self.HealthId1, self.vx, self.vy)
            # self.canvas.move(self.HealthId2, self.vx, self.vy)
            # x1, y1, x2, y2 = self.canvas.bbox(self.id)
            # self.centerX = (x1 + x2 ) / 2
            # self.centery = (y1 + y2 ) / 2


    def coordinates(self):
        if self.alive:
            x1, y1, x2, y2 = self.canvas.bbox(self.id)
            tag = self.canvas.gettags(self.id)
            # data = self.canvas.coords(self.id2)
            return tag,x1,y1,x2,y2 #,data

    def checkBounds(self):
        # print "checkBounds"
        if self.alive:
            x1,y1,x2,y2 = self.canvas.bbox(self.id)
            results = self.canvas.find_overlapping(x1,y1,x2,y2)
            # touching
            # print results
            for each in results:
                returnTags = self.canvas.gettags(each)
                if ("main" in returnTags):
                    if (self.color in returnTags):
                        pass
                    else:
                        print returnTags

            pass

    def checkAttackRange(self):
        canvas.create_oval
        self.centerX = (x1 + x2 ) / 2
        self.centery = (y1 + y2 ) / 2


    def destroy(self):
        if self.alive:
            self.alive = False
            self.dying = False
            print "DELETED!!!!!"
            self.canvas.delete(self.id)
            self.canvas.delete(self.HealthId1)
            self.canvas.delete(self.HealthId2)

# ____________________________________________________________________________
class Application(object):
    pygame.init()
    pygame.joystick.init()
    connected = pygame.joystick.get_count()
    print "you have", connected, "connected controllers"
    def __init__(self, master, **kwargs):
        self.master = master
        if "screenHeight" in kwargs:
            screenHeight = kwargs["screenHeight"]
        else:
            screenHeight = 400
        if "screenWidth" in kwargs:
            screenWidth = kwargs["screenWidth"]
        else:
            screenWidth = 400
        for each in range(self.connected):
            self.joystick.append( self.pygame.joystick.Joystick(each) )
            self.joystick[each].init()
            axes = joystick[each].get_numaxes()
            buttons = joystick[each].get_numbuttons()
            hats = joystick[each].get_numhats()
            balls = joystick[each].get_numballs()
            print "axes"
            print (axes)
            print "buttons"
            print (buttons)
            print "hats"
            print (hats)


        self.canvas = tk.Canvas(self.master, width=screenWidth, height=screenHeight)
        # self.canvas.pack()
        self.timer = 0
        CharacterGraphic.class_screenWidth = 1000
        CharacterGraphic.class_screenHeight = 500
        self.ships = [
            # CharacterGraphic(self.canvas, 5, 5, 55, 55, outline="blue", tag='blue'),
            # CharacterGraphic(self.canvas, 345, 345, 395, 395, outline="red", tag='red'),
            # CharacterGraphic(self.canvas, 5, 355, 45, 395, outline="blue", tag='green'),
            # CharacterGraphic(self.canvas, 355, 5, 395, 45, outline="blue", tag='yellow'),
            # CharacterGraphic(self.canvas, 355, 5, 395, 45, outline="blue", tag='gray'),
            # CharacterGraphic(self.canvas, 200, 0, 300, 100, outline="blue", tag='white'),
            # CharacterGraphic(self.canvas, 355, 5, 395, 45, outline="red", tag='purple'),
            # CharacterGraphic(self.canvas, 355, 5, 395, 45, outline="red", tag='pink'),
            CharacterGraphic(self.canvas, 0, 100, 100, 200, 200, outline="red", tag='pink'),
            CharacterGraphic(self.canvas, 1, 200, 200, 300, 300, outline="blue", tag='pink'),
        ]
        # addtag_withtag(tag, item)

        self.canvas.pack()
        self.master.after(0, self.animation)

    def animation(self):
        print ""
        print ""
        print "-------------------------"
        # print self.ships
        for ship in self.ships:
            ship.move()
            if (self.timer%5 == 0):
                ship.turn(1)
            health = ship.returnHealth()
            if health > 0:
                health = 100 - (self.timer%1000) / 10 - 1
                ship.updateHealthGraphic( health )
            elif (health <= 0) and (health > - 10):
                if self.timer%10 == 0:
                    health -= 1
                    print "I'm hurting and health is ", health
                ship.updateHealthGraphic( health )
            elif health <= -10:
                pass
                # ship.destroy()
            # print "sending health", health
            ship.checkBounds()
            # print ship.coordinates()
        self.IncreaseTimer()
        pygame.event.pump()
        #---------------------------------------
        for each in range(connected):
            print "Joystick", each ,":"
            print self.joystick[each].get_axis(xAxisNum)
            print self.joystick[each].get_axis(yAxisNum)
            for eachbutton in range(buttons):
                button = self.joystick[each].get_button(eachbutton)
                print eachbutton, ":",button, "    ",
            print ""
        #---------------------------------------
        print "end of round",self.timer
        print ""
        self.master.after(100, self.animation)

    def IncreaseTimer(self):
        self.timer += 1

    def returnTimer(self):
        return self.timer

# ____________________________________________________________________________
if __name__== "__main__":
    root = tk.Tk()
    app = Application(root,screenWidth="1000",screenHeight="500")
    root.mainloop()
