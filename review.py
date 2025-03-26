import pygame
import numpy as np
import time
import json

with open("data.json", "r") as f:
    review = np.array(json.load(f))

pygame.init()
W = 1600
H = 600
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Oscilloscope review data")


datalength = W
x = np.ravel(np.linspace(0,datalength-1, datalength))
count = len(review)

run = True
pressed = False
a_down = False
d_down = False
while run:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    a_down = True
                if event.key == ord('d'):
                    d_down = True
        elif event.type == pygame.KEYUP:
                if event.key == ord('a'):
                    a_down = False
                if event.key == ord('d'):
                    d_down = False
  
    if a_down:
        count += 5
    elif d_down:
        count -= 5
    count = max(0,min(len(review)-1-datalength,count))

    datapoints1 = np.array(review[:,0])[count:datalength+count]
    datapoints2 = np.array(review[:,1])[count:datalength+count]
    datapoints3 = np.array(review[:,2])[count:datalength+count]

    #print values
    screen.fill((64,64,64))
    d1 = np.stack((x, np.ravel(datapoints1)), axis=-1)
    d2 = np.stack((x, np.ravel(datapoints2)), axis=-1)
    d3 = np.stack((x, np.ravel(datapoints3)), axis=-1)
    pygame.draw.lines(screen, (255,0,0), False, d1, 1)
    pygame.draw.lines(screen, (0,255,0), False, d2, 1)
    pygame.draw.lines(screen, (0,0,255), False, d3, 1)
    
    pygame.display.flip()



pygame.quit()
