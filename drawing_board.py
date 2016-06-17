from processing import *

colors = {
    "red": [255, 0, 0],
    "orange": [255, 153, 0],
    "yellow": [255, 255, 0],
    "brown": [100, 40, 40],
    "lightgreen": [0, 255, 0],
    "green": [0, 153, 51],
    "lightpurple": [255, 0, 200],
    "purple": [200, 0, 255],
    "lightblue": [0, 200, 255],
    "blue": [0, 0, 255],
    "black": [0, 0, 0],
    "gray": [209, 209, 209],
    "white": [255, 255, 255]
}

Btns={}
pressed = False
mouseBtn = 0
shapes = []

colorDictXs = {}
currColor = "red"
BtnChoice = "Pencil"
ThickChoice = 1

oval = False
recta = False
currX = 0
currY = 0
finalX = 0
finalY = 0

class Button:
    def __init__(self, words, x, y, shapex, shapey, thickness):
        self.words = words
        self.selected = False
        self.inUse = False
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.shapex = shapex
        self.shapey = shapey
        self.thickness = thickness
        
    def draw(self):
        if self.selected:
            stroke(0, 0, 0)
            fill(255, 255, 255)
            rect(self.x, self.y, self.width, self.height)
        else:
            stroke(209, 209, 209)
            fill(230, 230, 230)
            rect(self.x, self.y, self.width, self.height)

    def drawShape(self):
        if self.words == "pencil":
            stroke(0, 0, 0)
            arc(self.shapex+10, self.shapey, 20, 20, PI, TWO_PI-PI/2)
            arc(self.shapex-10, self.shapey, 20, 20, 0, PI/2)
        if self.words == "oval with no fill color":
            stroke(0,0,0)
            ellipse(self.shapex,self.shapey,20,20)
        if self.words == "rect with no fill color":
            stroke(0,0,0)
            rect(self.shapex,self.shapey,20,20)
        if self.words == "oval with filled color":
            fill(0,0,0)
            ellipse(self.shapex,self.shapey,20,20)
        if self.words == "rect with filled color":
            fill(0,0,0)
            rect(self.shapex,self.shapey,20,20)
        if self.words == "eraser":
            fill(0,0,0)
            quad(self.shapex+5,self.shapey-5,self.shapex+10,self.shapey-5,self.shapex+5,self.shapey,self.shapex,self.shapey)
            fill(255,255,255)
            quad(self.shapex,self.shapey,self.shapex+5,self.shapey,self.shapex,self.shapey+5,self.shapex-5,self.shapey+5)
        if self.thickness == 1:
            strokeWeight(1)
            stroke(0,0,0)
            line(self.shapex-10,self.shapey,self.shapex+10,self.shapey)
        if self.thickness == 2:
            strokeWeight(2)
            stroke(0,0,0)
            line(self.shapex-10,self.shapey,self.shapex+10,self.shapey)
            strokeWeight(1)
        if self.thickness == 3:
            strokeWeight(3)
            stroke(0,0,0)
            line(self.shapex-10,self.shapey,self.shapex+10,self.shapey)
            strokeWeight(1)
        if self.thickness == 4:
            stroke(0,0,0)
            strokeWeight(4)
            line(self.shapex-10,self.shapey,self.shapex+10,self.shapey)
            strokeWeight(1)
            
        
    def toggle(self):
        if self.selected:
            self.selected = False
        else:
            self.selected = True
            
    def checkSelected(self, mouseX, mouseY):
        if mouseX >= self.x and mouseX <= self.x + self.width:
            if mouseY >= self.y and mouseY <= self.y + self.height:
                return True
            else:
                return False
        else:
            return False

class ColorButton:
    def __init__(self, words, x, y):
        self.words = words
        self.selected = False
        self.inUse = False
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

        
    def draw(self):
        if self.selected:
            stroke(0, 0, 0)
            strokeWeight(2)
            fill(colors[self.words][0], colors[self.words][1], colors[self.words][2])
            ellipse(self.x, self.y, self.width, self.height)
            strokeWeight(1)
        else:
            stroke(209, 209, 209)
            strokeWeight(1)
            fill(colors[self.words][0], colors[self.words][1], colors[self.words][2])
            ellipse(self.x, self.y, self.width, self.height)

    
    def toggle(self):
        if self.selected:
            self.selected = False
        else:
            self.selected = True
            
    def checkSelected(self, mouseX, mouseY):
        if mouseX >= self.x - 15 and mouseX <= self.x + 15:
            if mouseY >= self.y -15 and mouseY <= self.y + 15:
                return True
            else:
                return False
        else:
            return False        
        
def setup():
    global Btns
    size(540, 400)
    background(255, 255, 255)
    
    pencilBtn = Button("pencil", 15, 15, 30, 30, 0)
    pencilBtn.toggle()    
    Btns["Pencil"] = pencilBtn
    
    OvalnoFillColor = Button("oval with no fill color", 15, 50, 30, 65, 0)    
    Btns["Oval with no fill color"] = OvalnoFillColor
    
    RectnoFillColor = Button("rect with no fill color", 15, 85, 20, 90, 0)    
    Btns["Rect with no fill color"] = RectnoFillColor

    
    OvalFillColor = Button("oval with filled color", 15, 120, 30, 135, 0)    
    Btns["Oval with filled color"] = OvalFillColor

    RectFillColor = Button("rect with filled color", 15, 155, 20, 160, 0)   
    Btns["Rect with filled color"] = RectFillColor

    Eraser = Button("eraser", 15, 190, 30, 205, 0)   
    Btns["Eraser"] = Eraser           

    ThickWeight1 = Button("Thick", 15, 250, 30, 265, 1)
    ThickWeight1.toggle()    
    Btns["thickweight1"] = ThickWeight1
                 
    ThickWeight2 = Button("Thick", 15, 285, 30, 300, 2)  
    Btns["thickweight2"] = ThickWeight2

    ThickWeight3 = Button("Thick", 15, 320, 30, 335, 3)   
    Btns["thickweight3"] = ThickWeight3

    ThickWeight4 = Button("Thick", 15, 355, 30, 370, 4)   
    Btns["thickweight4"] = ThickWeight4
    
    x=85
    for c in colors:
        colorDictXs[c]=ColorButton(c,x,375)
        x += 35
    colorDictXs["red"].toggle()
    
def draw():
    global finalX, finalY
    if mousePressed:
        finalX = mouse.x
        finalY = mouse.y
        initialX = mouse.px
        initialY = mouse.py
    background(255,255,255)
    stroke(209, 209, 209)
    strokeWeight(1)
    fill(230,230,230)
    rect(10,10,40,215)
    rect(10,245,40,145)
    for m in colorDictXs:
        colorDictXs[m].draw()
        
    for s in Btns:
        Btns[s].draw()
        Btns[s].drawShape()
        
                    
    if BtnChoice == "Pencil" and mouseBtn  == 40:
        if (finalX > 60 and finalX < 540) and (finalY > 0 and finalY < 350) and (initialX > 60 and initialX < 540) and (initialY > 0 and initialY < 350):
            createPencil(finalX, finalY, initialX, initialY, currColor, BtnChoice, ThickChoice)  
            
        
    if BtnChoice == "Oval with no fill color": 
            stroke(colors[currColor][0], colors[currColor][1], colors[currColor][2])
            strokeWeight(ThickChoice)
            if pressed:
                noFill()
                if finalX - currX > 0:
                    ellipse(currX + (finalX - currX) / 2, 
                     currY + (finalY - currY) / 2,
                     finalX - currX,
                     finalY - currY)
                else: 
                    ellipse(currX + (finalX - currX) / 2, 
                     currY + (finalY - currY) / 2,
                     currX - finalX,
                     currY - finalY)
                
    if BtnChoice == "Rect with no fill color":
            stroke(colors[currColor][0], colors[currColor][1], colors[currColor][2])
            strokeWeight(ThickChoice)
            if pressed:
                noFill()
                rect(currX, currY, 
                finalX - currX, finalY - currY)
                

    if BtnChoice == "Oval with filled color":
            stroke(colors[currColor][0], colors[currColor][1], colors[currColor][2])
            strokeWeight(ThickChoice)
            if pressed:
                noFill()
                if finalX - currX > 0:
                    ellipse(currX + (finalX - currX) / 2, 
                      currY + (finalY - currY) / 2,
                      finalX - currX,
                      finalY - currY)
                else: 
                    ellipse(currX + (finalX - currX) / 2, 
                      currY + (finalY - currY) / 2,
                      currX - finalX,
                      currY - finalY)
                
    if BtnChoice == "Rect with filled color":
            stroke(colors[currColor][0], colors[currColor][1], colors[currColor][2])
            strokeWeight(ThickChoice)
            if pressed:
                noFill()
                rect(currX, currY, 
                finalX - currX, finalY - currY)
                
    if (BtnChoice == "Eraser") and (finalX > 50 and finalX < 540) and (finalY > 0 and finalY < 335) and pressed:
        createEraser(finalX, finalY)
        
    drawShape()

                                   
def mousePressed():
    global currColor, BtnChoice, mouseBtn, ThickChoice, currX, currY, pressed, oval, recta
    pressed = True
    currX = mouse.x
    currY = mouse.y
    if mouse.button == 37:
        if (currY >= 360 and currY <= 390) and currX >= 70:
            for r in colorDictXs:
                if colorDictXs[r].checkSelected(currX,currY):
                    colorDictXs[r].selected = True
                    currColor = r
                else:
                    colorDictXs[r].selected = False
        if (currX >= 10 and currX <= 50):
            if Btns["Pencil"].checkSelected(currX,currY):
                BtnChoice = "Pencil"
                Btns["Pencil"].selected = True
                Btns["Oval with no fill color"].selected = False
                Btns["Rect with no fill color"].selected = False
                Btns["Oval with filled color"].selected = False
                Btns["Rect with filled color"].selected = False
                Btns["Eraser"].selected = False
            if Btns["Oval with no fill color"].checkSelected(currX,currY):
                BtnChoice = "Oval with no fill color"
                Btns["Pencil"].selected = False
                Btns["Oval with no fill color"].selected = True
                Btns["Rect with no fill color"].selected = False
                Btns["Oval with filled color"].selected = False
                Btns["Rect with filled color"].selected = False
                Btns["Eraser"].selected = False
            if Btns["Rect with no fill color"].checkSelected(currX,currY):
                BtnChoice = "Rect with no fill color"
                Btns["Pencil"].selected = False
                Btns["Oval with no fill color"].selected = False
                Btns["Rect with no fill color"].selected = True
                Btns["Oval with filled color"].selected = False
                Btns["Rect with filled color"].selected = False
                Btns["Eraser"].selected = False
            if Btns["Oval with filled color"].checkSelected(currX,currY):
                BtnChoice = "Oval with filled color"
                Btns["Pencil"].selected = False
                Btns["Oval with no fill color"].selected = False
                Btns["Rect with no fill color"].selected = False
                Btns["Oval with filled color"].selected = True
                Btns["Rect with filled color"].selected = False
                Btns["Eraser"].selected = False
            if Btns["Rect with filled color"].checkSelected(currX,currY):
                BtnChoice = "Rect with filled color"
                Btns["Pencil"].selected = False
                Btns["Oval with no fill color"].selected = False
                Btns["Rect with no fill color"].selected = False
                Btns["Oval with filled color"].selected = False
                Btns["Rect with filled color"].selected = True
                Btns["Eraser"].selected = False
            if Btns["Eraser"].checkSelected(currX,currY):
                BtnChoice = "Eraser"
                Btns["Pencil"].selected = False
                Btns["Oval with no fill color"].selected = False
                Btns["Rect with no fill color"].selected = False
                Btns["Oval with filled color"].selected = False
                Btns["Rect with filled color"].selected = False
                Btns["Eraser"].selected = True
            if Btns["thickweight1"].checkSelected(currX,currY):
                ThickChoice = 1
                Btns["thickweight1"].selected = True
                Btns["thickweight2"].selected = False
                Btns["thickweight3"].selected = False
                Btns["thickweight4"].selected = False
            if Btns["thickweight2"].checkSelected(currX,currY):
                ThickChoice = 2
                Btns["thickweight1"].selected = False
                Btns["thickweight2"].selected = True
                Btns["thickweight3"].selected = False
                Btns["thickweight4"].selected = False
            if Btns["thickweight3"].checkSelected(currX,currY):
                ThickChoice = 3
                Btns["thickweight1"].selected = False
                Btns["thickweight2"].selected = False
                Btns["thickweight3"].selected = True
                Btns["thickweight4"].selected = False
            if Btns["thickweight4"].checkSelected(currX,currY):
                ThickChoice = 4
                Btns["thickweight1"].selected = False
                Btns["thickweight2"].selected = False
                Btns["thickweight3"].selected = False
                Btns["thickweight4"].selected = True
        if (currX > 50 and currX < 540) and (currY > 0 and currY < 335):
            if Btns["Oval with no fill color"].selected or Btns["Oval with filled color"].selected:
                oval = True
            if Btns["Rect with no fill color"].selected or Btns["Rect with filled color"].selected:
                recta = True
            mouseBtn = 40
            if Btns["Eraser"].selected:
                createEraser(currX, currY)
        
                
            
def mouseReleased():
    global finalX, finalY, pressed, oval, recta, mouseBtn
    pressed = False
    mouseBtn = 0
    finalX = mouse.x
    finalY = mouse.y
    if oval and (finalX > 50 and finalX < 540) and (finalY > 0 and finalY < 360):
        createCircles(currX, currY, finalX, finalY, currColor, BtnChoice, ThickChoice)
        oval = False
    if recta and (finalX > 50 and finalX < 540) and (finalY > 0 and finalY < 360):
        createRects(currX, currY, finalX, finalY, currColor, BtnChoice, ThickChoice)
        recta = False


def createPencil(currX, currY, initialX, initialY, currColor, BtnChoice, ThickChoice):
    global shapes
    shape = {
	    "type": "pencil",
        "x": currX,
        "y": currY,
        "px": initialX,
        "py": initialY,
        "color": currColor,
        "Btn": BtnChoice,
        "Thick": ThickChoice
    }
    shapes.append(shape)
    
    
def createCircles(currX, currY, finalX, finalY, currColor, BtnChoice, ThickChoice):
    global shapes
    shape = {
	    "type": "circle",
        "x": currX + (finalX - currX) / 2,
        "y": currY + (finalY - currY) / 2,
        "width": finalX - currX,
        "height": finalY - currY,
        "color": currColor,
        "Btn": BtnChoice,
        "Thick": ThickChoice
    }
    shapes.append(shape)
    
            
def createRects(currX, currY, finalX, finalY, currColor, BtnChoice, ThickChoice):
    global shapes
    shape = {
	    "type": "rectangle",
        "x": currX,
        "y": currY,
        "width": finalX - currX,
        "height": finalY - currY,
        "color": currColor,
        "Btn": BtnChoice,
        "Thick": ThickChoice
    }
    shapes.append(shape)
            
def createEraser(currX, currY):
    global shapes
    shape= {
	    "type": "eraser",
        "x": currX,
        "y": currY,
        "side": 25
    }
    shapes.append(shape)

def drawShape():
    for shape in shapes:
        if shape["type"] == "pencil":
            color = shape["color"]
            stroke(colors[color][0], colors[color][1], colors[color][2])
            Thick = shape["Thick"]
            strokeWeight(Thick)
            line(shape["x"], shape["y"], shape["px"], shape["py"])
        if shape["type"] == "circle":
            color = shape["color"]
            stroke(colors[color][0], colors[color][1], colors[color][2])
            Thick = shape["Thick"]
            strokeWeight(Thick)
            Btn = shape["Btn"]
            if Btn == "Oval with no fill color":
                noFill()
            if Btn == "Oval with filled color":
                fill(colors[color][0], colors[color][1], colors[color][2])
            width = shape["width"]
            height = shape["height"]
            if width < 0:
                width *= -1
            if height <0:
                height *= -1
            ellipse(shape["x"], shape["y"], width, height)
        if shape["type"] == "rectangle":
            color = shape["color"]
            stroke(colors[color][0], colors[color][1], colors[color][2])
            Thick = shape["Thick"]
            strokeWeight(Thick)
            Btn = shape["Btn"]
            if Btn == "Rect with no fill color":
                noFill()
            if Btn == "Rect with filled color":
                fill(colors[color][0], colors[color][1], colors[color][2])
            width = shape["width"]
            height = shape["height"]
            rect(shape["x"], shape["y"], width, height)
        if shape["type"] == "eraser":
            stroke(255, 255, 255)
            fill(255, 255, 255)
            rect(shape["x"], shape["y"], shape["side"], shape["side"])
        
run()
