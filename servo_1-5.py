#Below imports all the extra functionality required and creates the initialising statement for access to all 16 PWM signals.
from time import *
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

#Below creates an infinite loop
while True:

#Below counts each servo one by one, from 1 to 5
    kit.servo[0].angle = 90
    sleep(.2)
    kit.servo[1].angle = 60
    sleep(.2)
    kit.servo[2].angle = 30
    sleep(.2)
    kit.servo[3].angle = 0
    sleep(.2)

    kit.servo[4].angle = 90
    sleep(.2)
    kit.servo[5].angle = 60
    sleep(.2)
    kit.servo[6].angle = 30
    sleep(.2)
    kit.servo[7].angle = 0
    sleep(.2)

    kit.servo[8].angle = 90
    sleep(.2)
    kit.servo[9].angle = 60
    sleep(.2)
    kit.servo[10].angle = 30
    sleep(.2)
    kit.servo[11].angle = 0
    sleep(.2)

    kit.servo[12].angle = 90
    sleep(.2)
    kit.servo[13].angle = 60
    sleep(.2)
    kit.servo[14].angle = 30
    sleep(.2)
    kit.servo[15].angle = 0
    sleep(.2)
