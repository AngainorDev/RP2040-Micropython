from utime import sleep_ms
from urandom import getrandbits, randint

import picokeypad as keypad

PIXELS = [0 for i in range(16)]
colors = [255, 128, 196, 255]

def random_color():
    return colors[randint(0, len(colors) - 1)]

def clear_display():
    global PIXELS
    for pixel_index in range(16):
        PIXELS[pixel_index] = 0
        keypad.illuminate(pixel_index, 0, 0, 0)
    keypad.update()


def scroll():
    global PIXELS
    for j in range(1,4):
        for k in range(4):
            PIXELS[(4-j)*4+k] = max(0, PIXELS[(4-j-1)*4+k] - 75)
            keypad.illuminate((4-j)*4+k, 0, PIXELS[(4-j)*4+k] , 0)
    for i in range(4):
        if getrandbits(8) > 180:
            PIXELS[i] = random_color()
            keypad.illuminate(i, 0, PIXELS[i], 0)
        else:
            PIXELS[i] = 0
            keypad.illuminate(i, 0, 0, 0)
    keypad.update()


def run():
    keypad.init()
    keypad.set_brightness(0.5)
    clear_display()
    while True:
        scroll()
        sleep_ms(250)
            
if __name__ == '__main__':
    run()
    

