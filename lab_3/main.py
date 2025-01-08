import math
from turtle import *
from random import random
import tqdm

# створити фігуру. Варіант 3
x_min = 0
x_max = 4
y_min = 0
y_max = 4

def check(x,y):
    if x >= 0 and x <=2:
        if y >=1 and y<=3:
            return True
    elif x>2 and x<=4:
        if y >= 0 and y<=2:
            return True
    return False

# знайти площу
resolution = 1000
counter = 0
speed(0)
screen = Screen()
screen.listen()
screen.tracer(0,0)
for i in tqdm.tqdm(range(resolution)):
    x,y = random()*x_max-x_min, random()*y_max-y_min
    if check(x,y):
        penup()
        goto(x*50,y*50)
        dot(5,"green")
        counter += 1
    else:
        penup()
        goto(x * 50, y * 50)
        dot(5, "red")
    if i%50 == 0:
        screen.update()
print((counter/resolution)*(x_max-x_min)*(y_max-y_min))
goto((x_max-x_min)*50/2,y_min-30)
write("Area = "+str((counter/resolution)*(x_max-x_min)*(y_max-y_min)), False, "center", font=("Courier", 20, "normal"))
screen.update()
input("Press enter to exit")