def setup():
    global cube, cube2,cube3,cube4,cube5,cube6,cube7,cube8,cube9,cube10
    size(1920, 1080, P3D)
    frameRate(120)
    colorMode(HSB)
    cube = Cube(600, 0, 100, 3,100 ) # Creating the cube
    cube2 = Cube(-600, 0, 100, 3, 100)
    cube3 = Cube(600, 0, 100, 3,100 ) # Creating the cube
    cube4 = Cube(-600, 0, 100, 3, 100)
    cube5 = Cube(600, 0, 100, 3,100 ) # Creating the cube
    cube6 = Cube(-600, 0, 100, 3, 100)
    cube7= Cube(600, 0, 100, 3,100 ) # Creating the cube
    cube8 = Cube(-600, 0, 100, 3, 100)
    cube9= Cube(600, 0, 100, 3,100 ) # Creating the cube
    cube10 = Cube(-600, 0, 100, 3, 100)
    #fullScreen(P3D)
theta = 0
h = 0
def draw():
    global cube, cube2,cube3,cube4,cube5,cube6,cube7,cube8,cube9,cube10
    global theta, h, y_offset
    h += 1
    if h == 255:
        h = 0
        
    y_offset = sin(theta) * 10
    colorMode(HSB)
    strokeWeight(3)
    background(0)
    stroke(h, 200, 200)
    translate(width/2, 740 + y_offset, 0)

    rotateX(.5)
    fill(0)
    box(350, 200, 15) #Back window
    
    translate(0, 150, 0)
    rotateX(-.5)
    box(350, 100, 0) #Bumper
    
    box(100, 50, 0) #License plate
    
    translate(-150, -20, 0)
    fill(255, 255, 255)
    box(50, 50, 0) #Left brakelight
    
    translate(300, 0, 0)
    box(50, 50, 0) #Right brakelight
    noFill()
    
    translate(0, 110, 0)
    box(50, 75, 0) #Right wheel
    
    translate(-300, 0, 0)
    box(50, 75, 0) #Left wheel
    
    translate(50, -30, 0)
    circle(0, 0, 15) #Exhaust
    
    translate(70, -80, 0)
    #box(15, 0, 0)
    
    #5
    line(0,0,20,0)
    line(0, 0, 0, 18)
    line(0, 18, 20, 18)
    line(20, 18, 20, 36)
    line(20, 36, 0, 36)
    
    #2
    translate(40, 0, 0)
    line(0, 0, 20, 0)
    line(20, 0, 20, 18)
    line(0, 18, 20, 18)
    line(0, 18, 0, 36)
    line(0, 36, 20, 36)
    
    fill(0)
    translate(70, -50, 0)
    box(5, 30, 0)
    
    translate(-155, 0, 0)
    box(5, 30, 0)
    
    translate(75, -20, 0)
    box(450, 5, 0)
    
    theta += 0.01
    
    
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(200, 230)
    
    blendMode(BLEND)
    colorMode(HSB)
    
    translate(0, -250, -100)
    
    lights()
    strokeWeight(5)

    cube.render() # Callint the render method on the cube
    cube2.render()
    
# A class consists of fields and methods
class Cube:
    
    # Constructor
    def __init__(self, x, y, z, s, h):
        # These are now fields!! Thats what the self word does
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.theta = 0
        self.pos.z = -8000
        
    def render(self):
        if self.pos.z > 1000:
            self.pos.z=-8000
        else:
            pushMatrix()
            translate(self.pos.x, self.pos.y, self.pos.z)
            translate(5, 5, 0);
            scale(self.s)
            box(200)
            popMatrix()
            self.theta += 0.1
            self.pos.z +=20
