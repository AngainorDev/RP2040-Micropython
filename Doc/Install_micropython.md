# How to install Micropython on Raspberry Pi Pico

See https://www.raspberrypi.org/documentation/pico/getting-started/

uf2 files can be used to easily flash your board.  
Hold "BOOTSEL" button down while plugin the board, a USB mass storage device will appear.  
Once the .uf2 file is copied, the board will reboot. You can then use an IDE or a simple terminal to connect to it.  

Thonny is the official recommended IDE, but rshell for instance is also a great and versatile, more light weight, tool.

# Precompiled firmwares

## From micropython

http://micropython.org/download/rp2-pico/

These do not include specific libraries for some adds on, like Pimoroni's.  
Some useful libs like hashlib are not included.

# From pimoroni

With support for the pico backpacks from Pimoroni  
https://shop.pimoroni.com/collections/pico

- Explorer base - LCD screen ,motor drivers, piezo and breadboard
- RGB Keyboard - 16 keys with 16 associated RGB leds
- Unicorn Pack - 7 x 16 rgb led matric + 4 buttons
- Display Pack - 1.14" IPS LCD (SPI)  + 4 buttons + RGB Led
- Scroll pack - 17 x 7 white leds + 4 buttons

https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md  
Demo / examples:  
https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples

Some useful libs like hashlib are not included by default, you'll need to compile your own firmware for that, see

# Raspberry Pi Pico Python SDK

To be found here  
https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf


# Build your own firmware

WIP
