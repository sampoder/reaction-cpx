import time
from random import randint
from random import choice
from adafruit_circuitplayground import cp

colours = [(25, 0, 0), (0, 25, 0), (0, 0, 25) ]


while True:

    while cp.switch:

        luck = randint(1, 7)

        if luck == 1:

            finalColor = choice(colours)

            cp.pixels[0] = finalColor
            cp.pixels[1] = finalColor
            cp.pixels[2] = finalColor
            cp.pixels[3] = finalColor
            cp.pixels[4] = finalColor

            timePassed = 0

            while cp.button_b == False:

                time.sleep(0.001)

                timePassed+=0.001

            print("Your reaction speed was " + str(timePassed) + " seconds.")

            cp.play_tone(262, 1)

            time.sleep(2)

        else:

            cp.pixels[0] = choice(colours)
            cp.pixels[1] = choice(colours)
            cp.pixels[2] = choice(colours)
            cp.pixels[3] = choice(colours)
            cp.pixels[4] = choice(colours)

        time.sleep(1)
        
    if cp.switch == False:
        
        finalColor = [0,0,0]

        cp.pixels[0] = finalColor
        cp.pixels[1] = finalColor
        cp.pixels[2] = finalColor
        cp.pixels[3] = finalColor
        cp.pixels[4] = finalColor
