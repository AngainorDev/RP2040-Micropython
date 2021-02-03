# "Matrix" rain effect on Raspberry Pi Pico with Pimoroni's RGB keypad

This requires the Pimoroni's enabled micropython from https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md  
See also https://github.com/AngainorDev/RP2040-Micropython/blob/main/Doc/Install_micropython.md for more info


## Why

We plan to use the Raspberry Pi pico and the RGB keypad for a future project.  
First step is to get familiar with the hardware and libraries.

The rain effect from Matrix seemed a good introduction, however limited due to the small number of leds.

![rain effect raspberry pico](https://github.com/AngainorDev/RP2040-Micropython/blob/main/Matrix_Rain_Effect/matrix-rain-pico.gif)

## Required

- Raspberry Pi Pico  
  https://shop.pimoroni.com/products/raspberry-pi-pico
- Pimoroni RGB Key pad  
  https://shop.pimoroni.com/products/pico-rgb-keypad-base

## The code 

See https://github.com/AngainorDev/RP2040-Micropython/blob/main/Matrix_Rain_Effect/rain.py 
It's not very clean, but it works.

Random flakes appear at top and they scroll down, losing brightness as they go.
