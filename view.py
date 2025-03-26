import serial
import serial.tools.list_ports
import pygame
import numpy as np
import time
import json


pygame.init()
W = 1600
H = 600
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Oscilloscope")

port_file = '/dev/ttyACM0'

do = True
while do:
    try:
        port = serial.Serial(port_file, 31250)
        do = False
    except:
        print("could not connect to serialport")
        time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = False


datalength = W
datapoints1 = np.zeros(datalength)
datapoints2 = np.zeros(datalength)
datapoints3 = np.zeros(datalength)
x = np.ravel(np.linspace(0,datalength-1, datalength))
count = 0
review = list()

run = True
while run:
    # start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #read value
    try:
        newpoints = port.readline()
    except:
        continue

    
    #merge value
    tmp = datapoints1.copy()
    datapoints1[0] = H-10-2*int.from_bytes(newpoints[:1])
    datapoints1[1:] = tmp[:-1]

    tmp = datapoints2.copy()
    datapoints2[0] = H-10-2*int.from_bytes(newpoints[1:2])
    datapoints2[1:] = tmp[:-1]

    tmp = datapoints3.copy()
    datapoints3[0] = H-10-2*int.from_bytes(newpoints[2:3])
    datapoints3[1:] = tmp[:-1]
    review.append((datapoints1[0], datapoints2[0], datapoints3[0]))
  


    if count < 0:
        count = 10

        #print values
        screen.fill((64,64,64))
        d1 = np.stack((x, np.ravel(datapoints1)), axis=-1)
        d2 = np.stack((x, np.ravel(datapoints2)), axis=-1)
        d3 = np.stack((x, np.ravel(datapoints3)), axis=-1)
        pygame.draw.lines(screen, (255,0,0), False, d1, 1)
        pygame.draw.lines(screen, (0,255,0), False, d2, 1)
        pygame.draw.lines(screen, (0,0,255), False, d3, 1)
        
        pygame.display.flip()
    count -= 1


pygame.quit()
try:
    port.close()
except:
    pass

with open("data.json", "w") as f:
    json.dump(review, f)