import cairo
import math
import random
from time import sleep

Xoffset_init = -20
Yoffset_init = 0
Xoffset = Xoffset_init 
Yoffset = Yoffset_init

Xstart = 50
Ystart = 100

Xintermediate = 75
Yintermediate = 75

Xend = 100
Yend = 50

count = 10000
z = int(math.sqrt(count))
print(z)
with cairo.SVGSurface("hearts.svg", 150*z, 150*z) as surface:
      
    for i in range(z):
        for j in range(z):
            context = cairo.Context(surface)

            context.set_source_rgb(1, 0, 0)
            context.set_line_width(1)

            # heart part
            if True:
                context.move_to(Xoffset+50, Yoffset+50)
                context.line_to(Xoffset+50, Yoffset+100)
                context.line_to(Xoffset+100,Yoffset+100)
                context.stroke()
                context.move_to(Xoffset+100, Yoffset+75)
                context.stroke()
                context.arc(Xoffset+100, Yoffset+75, 25, -math.pi/2, math.pi/2)
                context.move_to(Xoffset+50,Yoffset+50)
                context.arc(Xoffset+75, Yoffset+50, 25, math.pi, 0)
                context.stroke()

            if True: # Tame breaks
                context.move_to(Xoffset+Xstart,Yoffset+Ystart)
                xmin = 50 
                xmax = 100
                x1 = random.randint(50,75)
                y1 = random.randint(25,75)
                x2 = random.randint(50,75)
                y2 = random.randint(100,125)

                context.curve_to(Xoffset+x1, Yoffset+y1, Xoffset+x2, Yoffset+y2, Xoffset+Xintermediate, Yoffset+Yintermediate) #last pair is fixed
                context.set_source_rgb(1, 0, 0)
                context.stroke()

                context.move_to(Xoffset+Xintermediate,Yoffset+Yintermediate)
                xmin = 50 
                xmax = 100
                x1 = random.randint(75,100)
                y1 = random.randint(0,50)
                x2 = random.randint(75,100)
                y2 = random.randint(75,125)

                context.curve_to(Xoffset+x1, Yoffset+y1, Xoffset+x2, Yoffset+y2, Xoffset+Xend, Yoffset+Yend) #last pair is fixed
                context.set_source_rgb(1, 0, 0)
                context.stroke()

            else: #wild breaks
                context.move_to(Xoffset+Xstart,Yoffset+Ystart)
                xmin = 50 
                xmax = 100
                x1 = random.randint(xmin,xmax)
                y1 = random.randint(xmin,xmax)
                x2 = random.randint(xmin,xmax)
                y2 = random.randint(xmin,xmax)

                context.curve_to(Xoffset+x1, Yoffset+y1, Xoffset+x2, Yoffset+y2, Xoffset+Xintermediate, Yoffset+Yintermediate) #last pair is fixed
                context.set_source_rgb(1, 0, 0)
                context.stroke()

                context.move_to(Xoffset+Xintermediate,Yoffset+Yintermediate)
                xmin = 50 
                xmax = 100
                x1 = random.randint(xmin,xmax)
                y1 = random.randint(xmin,xmax)
                x2 = random.randint(xmin,xmax)
                y2 = random.randint(xmin,xmax)

                context.curve_to(Xoffset+x1, Yoffset+y1, Xoffset+x2, Yoffset+y2, Xoffset+Xend, Yoffset+Yend) #last pair is fixed
                context.set_source_rgb(1, 0, 0)
                context.stroke()

            Xoffset += 100

        Xoffset = Xoffset_init
        Yoffset += 100


