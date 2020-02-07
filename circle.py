import Tkinter as tk
import time
import random
#
# root = tk.Tk()
# canvas = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
# canvas.grid()
#
# def _create_circle(self, x, y, r, **kwargs):
#     return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
# tk.Canvas.create_circle = _create_circle
#
# def _create_circle_arc(self, x, y, r, **kwargs):
#     if "start" in kwargs and "end" in kwargs:
#         kwargs["extent"] = kwargs["end"] - kwargs["start"]
#         del kwargs["end"]
#     return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
# tk.Canvas.create_circle_arc = _create_circle_arc
#
# # canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)
# # canvas.create_circle_arc(100, 120, 48, fill="green", outline="", start=45, end=140)
# # canvas.create_circle_arc(100, 120, 48, fill="green", outline="", start=275, end=305)
# # canvas.create_circle_arc(100, 120, 45, style="arc", outline="white", width=6, start=270-25, end=270+25)
# canvas.create_circle(150, 40, 20, fill="#BBB", outline="",tags="uno")
#
# root.wm_title("Circles and Arcs")
# root.mainloop()
#
# for i in range(1,10):
#     canvas.move(canvas.find_withtag("uno"),i,i)
#     # time.sleep(1)
#     pass
#     canvas.move()

# ____________________________________________________________________________
class CharacterGraphic(object):
    class_screenHeight = 400
    class_screenWidth = 400
    def __init__(self, canvas, *args, **kwargs):
        # if "screenHeight" in kwargs:
            # class_screenHeight = kwargs.pop("screenHeight")
            # class_screenHeight = kwargs["screenHeight"]

        # if "screenWidth" in kwargs:
            # class_screenWidth = kwargs.pop("screenWidth")
            # class_screenWidth = kwargs["screenWidth"]

        self.canvas = canvas
        self.alive = True
        self.dying = False
        self.id = canvas.create_oval(*args, **kwargs)
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        self.centerX = (x1 + x2 ) / 2
        self.centery = (y1 + y2 ) / 2
        self.color = self.canvas.gettags(self.id)[0]
        self.canvas.addtag_withtag("main", self.id)
        # self.id2 = canvas.create_oval(*args, **kwargs)
        self.health = 100
        self.HealthId1 = canvas.create_arc(*args, start=359,extent=0, style='chord', fill='black', **kwargs)
        self.HealthId2 = canvas.create_arc(*args, start=0,extent=359, style='chord', fill=self.color, **kwargs)

        # self.vx = 0
        # self.vy = 0
        self.vx = random.randint(1,5)
        self.vy = random.randint(1,5)

    def boundAngle(self,x):
        y = x % 360
        return y

    def returnHealth(self):
        if self.alive:
            print self.color, "is alive",
            if self.health < 0:
                self.dying = True
        if self.dying:
            print "but", self.color, "is dying",
        if self.alive:
            print ""
        return self.health

    def updateHealthGraphic(self,health):
        if self.alive:
            self.health = health
            if self.health >= 100:
                self.canvas.itemconfig(self.HealthId1, start=359,extent=0)
                self.canvas.itemconfig(self.HealthId2, start=0,extent=359)
            elif self.health <= 0:
                self.canvas.itemconfig(self.HealthId1, start=0,extent=359)
                self.canvas.itemconfig(self.HealthId2, start=359,extent=0)
            else:
                print "health is ", health
                angle1 = self.health * 180 / 100 + 90
                angle2 = self.health * 360 / 100
                angle3 = self.health * 360 / 100 - 360
                one = -self.boundAngle(angle1 )
                two = -self.boundAngle(-angle2)
                three = self.boundAngle(angle3)
                self.canvas.itemconfig(self.HealthId1, start=one)
                self.canvas.itemconfig(self.HealthId1, extent=two)
                self.canvas.itemconfig(self.HealthId2, start=one)
                self.canvas.itemconfig(self.HealthId2, extent=three)

    def move(self):
        if self.alive:
            x1, y1, x2, y2 = self.canvas.bbox(self.id)
            if x2 > class_screenWidth:
                # self.vx = 0
                self.vx = random.randint(-5,-4)
            if x1 < 0:
                # self.vx = 0
                self.vx = random.randint(4,5)

            if y2 > class_screenHeight:
                # self.vy = 0
                self.vy = random.randint(-5,-4)

            if y1 < 0:
                # self.vy = 0
                self.vy = random.randint(4,5)
            if self.health == 0:
                self.vy = 0
                self.vx = 0

            self.canvas.move(self.id, self.vx, self.vy)
            self.canvas.move(self.HealthId1, self.vx, self.vy)
            self.canvas.move(self.HealthId2, self.vx, self.vy)
            x1, y1, x2, y2 = self.canvas.bbox(self.id)
            self.centerX = (x1 + x2 ) / 2
            self.centery = (y1 + y2 ) / 2


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

        self.canvas = tk.Canvas(self.master, width=screenWidth, height=screenHeight)
        self.canvas.pack()
        self.timer = 0
        CharacterGraphic.class_screenWidth = 1000
        CharacterGraphic.class_screenHeight = 500
        self.aliens = [
            CharacterGraphic(self.canvas, 5, 5, 55, 55, outline="blue", tag='blue'),
            CharacterGraphic(self.canvas, 345, 345, 395, 395, outline="red", tag='red'),
            # CharacterGraphic(self.canvas, 5, 355, 45, 395, outline="blue", tag='green'),
            # CharacterGraphic(self.canvas, 355, 5, 395, 45, outline="blue", tag='yellow'),
            # CharacterGraphic(self.canvas, 355, 5, 395, 45, outline="blue", tag='gray'),
            # CharacterGraphic(self.canvas, 355, 5, 395, 45, outline="blue", tag='white'),
            # CharacterGraphic(self.canvas, 355, 5, 395, 45, outline="red", tag='purple'),
            # CharacterGraphic(self.canvas, 355, 5, 395, 45, outline="red", tag='pink'),
        ]
        # addtag_withtag(tag, item)

        self.canvas.pack()
        self.master.after(0, self.animation)

    def animation(self):
        print "-------------------------"
        # print self.aliens
        for alien in self.aliens:
            alien.move()
            health = alien.returnHealth()
            if health > 0:
                health = 100 - (self.timer%1000) / 10 - 1
                alien.updateHealthGraphic( health )
            elif (health <= 0) and (health > - 10):
                if self.timer%10 == 0:
                    health -= 1
                    print "I'm hurting and health is ", health
                alien.updateHealthGraphic( health )
            elif health <= -10:
                alien.destroy()
            # print "sending health", health
            alien.checkBounds()
            # print alien.coordinates()
        self.IncreaseTimer()
        print "end of round",self.timer
        print ""
        self.master.after(1, self.animation)

    def IncreaseTimer(self):
        self.timer += 1

    def returnTimer(self):
        return self.timer

# ____________________________________________________________________________

root = tk.Tk()
app = Application(root,screenWidth="1000",screenHeight="500")
root.mainloop()
