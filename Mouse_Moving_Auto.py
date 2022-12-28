import mouse
import time 
import random

while (True):
    x = random.randint(600,700)
    y = random.randint(200,600)
    mouse.move(x,y,0.5)
    time.sleep(2)
    
    #mouse.move(2630, 350, absolute=True, duration=3)
    #time.sleep(4)
    #mouse.move(350, 2630, absolute=True, duration=3)
    #time.sleep(4)