#from graphics import *

draw_legs()

man_animation = '  '

'''
mask_animation = "__ "

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + mask_animation[i % len(animation)])
    sys.stdout.flush()
print("End!")
'''


man = '''
            
        ( )
        /|\
       / | \  
        / \ 
       /   \ 
            '''

def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms= Line(Point(0, 100), Point(0, 100))
    arms.draw(win)

#for the second question i have to draw a circle which is at the centre of the graphics window. the user inputs the radius of the circle and the circle should come. But for some reasn my code doesnt seem to be working please help

def drawCircle():
    x = input("please enter the radius of the circle: ")
    centre= Point(100, 100)
    circle1 = Circle(centre, x)
    circle1.draw(win)