# "Matrix" rain effect on Raspberry Pi Pico with Pimoroni's RGB keypad

This requires the Pimoroni's enabled micropython from https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md


## Why

We plan to use the Raspberry Pi pico and the RGB keypad for a future project.  
First step is to get familiar with the hardware and libraries.

The rain effect from Matrix seemed a good introduction, however limited due to the small number of leds.

## Required

- Raspberry Pi Pico  
  https://shop.pimoroni.com/products/raspberry-pi-pico
- Pimoroni RGB Key pad  
  https://shop.pimoroni.com/products/pico-rgb-keypad-base

## The code 

See rain.py  
It's not very clean, but it works.

Random flakes appear at top and they scroll down, losing brightness as they go.
