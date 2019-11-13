#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This constants file is for a space Alien game
#  with sound

# CircuitPython screen size is 160x120 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60
TOTAL_NUMBER_OF_ALIENS = 8
TOTAL_NUMBER_OF_LASERS = 5
SHIP_SPEED = 1
LASER_SPEED = 2
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y * SPRITE_SIZE

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}
NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
