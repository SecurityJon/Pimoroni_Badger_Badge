###########################################################
#
#              HP Bar Badge
#
# Press 'Up' or 'C' to increase the HP bar
# Press 'Down' or 'A' to decrease the HP bar
# Press 'B' to invert the display
###########################################################

import time
import badger2040
import badger_os
import random

###########################################################
#
#               Configure these
#
###########################################################

USER_CONFIGURED_NAME = "@SecurityJon" #Insert your name here to go at the top right
USER_CONFIGURED_TEXT_SIZE = 2         #If the name isn't displaying right, make this figure smaller
SPEED_AND_GHOST = "no"                #Change to yes to make the dispay update faster, but you'll get some small ghosting issues

###########################################################


# Global Constants
WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT

# Health Numbers
DEFAULT_HEALTH = 5000
HEALTH = DEFAULT_HEALTH
MAX_HEALTH = 10000
HEALTH_STEPS = 1000
DISPLAY_HEALTH = HEALTH

# HP Bar
DEFAULT_HP_BAR = 5
HP_BAR = DEFAULT_HP_BAR
MAX_HP_BAR = 10

#Padding
LEFT_PADDING = 5
RIGHT_PADDING = 5
BOTTOM_PADDING = 5
TOP_PADDING = 5
BAR_HORIZONAL_PADDING = 10
BAR_VERTICAL_PADDING = 40

#Bar sizes
BAR_THICKNESS = 3

#HP text
HPNAME_TEXT_FONT = "bitmap8"
HPNAME_TEXT_SIZE = 3
HPNAME_TEXT_THICKNESS = 3

#User Name
USER = USER_CONFIGURED_NAME
USER_TEXT_SIZE = USER_CONFIGURED_TEXT_SIZE
USER_FONT = "bitmap8"
USER_FONT_THICKNESS = 2

#Health Text Font
HEALTH_TEXT_SIZE = 2
HEALTH_FONT = "bitmap8"
HEALTH_FONT_THICKNESS = 2

#Keep track of display invert
DISPLAY_INVERTED = False


# ------------------------------
#      Drawing functions
# ------------------------------

def inital_load():
    #Set the background to white
    display.pen(15)
    display.clear()
    
    #Change the pen to black and add the bar thickness
    display.pen(0)    
    display.thickness(BAR_THICKNESS)
    
    ###################################
    #         HP Bar outline
    ###################################    
    #Top bar
    bar_x_start = 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING
    bar_x_end = WIDTH - RIGHT_PADDING - BAR_HORIZONAL_PADDING
    bar_y_start = 0 + TOP_PADDING + BAR_VERTICAL_PADDING
    bar_y_end = 0 + TOP_PADDING + BAR_VERTICAL_PADDING
    display.line(bar_x_start, bar_y_start, bar_x_end, bar_y_end)
    #bottom bar
    bar_x_start = 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING
    bar_x_end = WIDTH - RIGHT_PADDING - BAR_HORIZONAL_PADDING
    bar_y_start = HEIGHT - BOTTOM_PADDING - BAR_VERTICAL_PADDING
    bar_y_end = HEIGHT - BOTTOM_PADDING - BAR_VERTICAL_PADDING
    display.line(bar_x_start, bar_y_start, bar_x_end, bar_y_end)
    #left bar
    bar_x_start = 0 + LEFT_PADDING
    bar_x_end = 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING     
    ##bottom bit   
    bar_y_start = round(0 + TOP_PADDING + BAR_VERTICAL_PADDING + (((HEIGHT - TOP_PADDING - BAR_VERTICAL_PADDING) - (0 + TOP_PADDING + BAR_VERTICAL_PADDING)) / 2))
    bar_y_end = HEIGHT - TOP_PADDING - BAR_VERTICAL_PADDING
    display.line(bar_x_start, bar_y_start, bar_x_end, bar_y_end)
    ##top bit
    bar_y_start = round(0 + TOP_PADDING + BAR_VERTICAL_PADDING + (((HEIGHT - TOP_PADDING - BAR_VERTICAL_PADDING) - (0 + TOP_PADDING + BAR_VERTICAL_PADDING)) / 2))
    bar_y_end = 0 + TOP_PADDING + BAR_VERTICAL_PADDING
    display.line(bar_x_start, bar_y_start, bar_x_end, bar_y_end)    
    
    #orig
    #bar_x_start = 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING
    #bar_x_end = 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING
    #bar_y_start = 0 + TOP_PADDING + BAR_VERTICAL_PADDING
    #bar_y_end = HEIGHT - TOP_PADDING - BAR_VERTICAL_PADDING
    #display.line(bar_x_start, bar_y_start, bar_x_end, bar_y_end)
    
    #right bar
    bar_x_start = WIDTH - RIGHT_PADDING - BAR_HORIZONAL_PADDING
    bar_x_end = WIDTH - RIGHT_PADDING - BAR_HORIZONAL_PADDING
    bar_y_start = 0 + TOP_PADDING + BAR_VERTICAL_PADDING
    bar_y_end = HEIGHT - TOP_PADDING - BAR_VERTICAL_PADDING
    display.line(bar_x_start, bar_y_start, bar_x_end, bar_y_end)
    
    ###################################
    #         HP Text
    ###################################
    display.thickness(HPNAME_TEXT_THICKNESS)
    display.font(HPNAME_TEXT_FONT)
    #display.text("HP", 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING, 0 + TOP_PADDING + round((BAR_VERTICAL_PADDING / 2)), scale=HPNAME_TEXT_SIZE, rotation=0.0)
    display.text("HP", 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING, 0 + TOP_PADDING + round((BAR_VERTICAL_PADDING / 4)), scale=HPNAME_TEXT_SIZE, rotation=0.0)
    
    
    ###################################
    #        User Text
    ###################################
    display.thickness(USER_FONT_THICKNESS)
    user_text_x = WIDTH - RIGHT_PADDING - BAR_HORIZONAL_PADDING - display.measure_text(USER, USER_TEXT_SIZE)
    user_text_y = 0 + TOP_PADDING + round((BAR_VERTICAL_PADDING / 2))
    display.font(USER_FONT)
    display.text(USER, user_text_x, user_text_y, scale=USER_TEXT_SIZE, rotation=0.0)

# Draw the amount of health we have
def health_number_amount(health):
    health_number_to_display = random.randrange(health, health + HEALTH_STEPS, 1)
    if (health_number_to_display > MAX_HEALTH):
        health_number_to_display = MAX_HEALTH
        
    health_to_display = str(health_number_to_display) + "/" + str(MAX_HEALTH)
    display.thickness(HEALTH_FONT_THICKNESS)
    health_text_x = WIDTH - RIGHT_PADDING - BAR_HORIZONAL_PADDING - display.measure_text(health_to_display, HEALTH_TEXT_SIZE)
    health_text_y = HEIGHT - BOTTOM_PADDING - round((BAR_VERTICAL_PADDING / 1.5))
    display.font(HEALTH_FONT)
    display.text(health_to_display, health_text_x, health_text_y, scale=HEALTH_TEXT_SIZE, rotation=0.0)
    
#The HP bar is fixed at 10 units
def hp_bar_display(hp_bar):
    #Define our standard bar
    hpbar_w = round((WIDTH - RIGHT_PADDING - BAR_HORIZONAL_PADDING) / 11.5)
    hpbar_h = 32
    #This hurts my head so its fixed for now, sue me.
    #hpbar_h = (0 + TOP_PADDING + BAR_VERTICAL_PADDING) + (HEIGHT - TOP_PADDING - BAR_VERTICAL_PADDING)
    hpbar_x = 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING + round(hpbar_w / 5)
    hpbar_y = 0 + TOP_PADDING + BAR_VERTICAL_PADDING + round(hpbar_h / 8)
    
    #Define our first bar
    
    for x in range(hp_bar):
        display.rectangle(hpbar_x, hpbar_y, hpbar_w, hpbar_h)
        hpbar_x = (hpbar_x + hpbar_w) + round((hpbar_w / 10))
        

#Increase HP
def healthUp():
    inital_load()
    global HEALTH
    HEALTH = HEALTH + HEALTH_STEPS
    if (HEALTH >= MAX_HEALTH):
        HEALTH = MAX_HEALTH
    health_number_amount(HEALTH)    
    
    global HP_BAR
    HP_BAR = HP_BAR + 1
    if (HP_BAR >= MAX_HP_BAR):
        HP_BAR = MAX_HP_BAR
    hp_bar_display(HP_BAR)
    
#Decrease HP
def healthDown():
    inital_load()
    global HEALTH
    HEALTH = HEALTH - HEALTH_STEPS
    if (HEALTH <= 0):
        HEALTH = 0
    health_number_amount(HEALTH)    
    
    global HP_BAR
    HP_BAR = HP_BAR - 1
    if (HP_BAR <= 0):
        HP_BAR = 0
    hp_bar_display(HP_BAR)
    

def quickFontTest():
    display.pen(15)
    display.clear()
    display.pen(0)
    
    
    display.thickness(3)
    theScale = 5
    textToDisplay = "HP"
    display.font("bitmap6")
    display.text(textToDisplay, 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING, 0 + TOP_PADDING, scale=theScale, rotation=0.0)
    textSize = display.measure_text(textToDisplay, theScale)
    
    display.thickness(4)
    theScale = 4
    textToDisplay = "HP"
    display.font("bitmap8")
    display.text(textToDisplay, 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING + textSize + 10 , 0 + TOP_PADDING, scale=theScale, rotation=0.0)
    textSize = display.measure_text(textToDisplay, theScale)
    
    display.thickness(3)
    theScale = 4
    textToDisplay = "HP"
    display.font("bitmap14_outline")
    display.text(textToDisplay, 0 + LEFT_PADDING + BAR_HORIZONAL_PADDING + textSize + 10 , 0 + TOP_PADDING + textSize, scale=theScale, rotation=0.0)
    textSize = display.measure_text(textToDisplay, theScale)    
    
    
# ------------------------------
#        Program setup
# ------------------------------

# Create a new Badger
display = badger2040.Badger2040()
display.led(0)

if (SPEED_AND_GHOST == "yes"):
    display.update_speed(badger2040.UPDATE_TURBO)
else:
    display.update_speed(badger2040.UPDATE_FAST)


# ------------------------------
#       Main program
# ------------------------------

#First set up
inital_load()  
health_number_amount(DEFAULT_HEALTH)
hp_bar_display(DEFAULT_HP_BAR)

#Quick Font test
#quickFontTest()
    

#Main program
while True:
    # Health down
    if display.pressed(badger2040.BUTTON_A) or display.pressed(badger2040.BUTTON_DOWN):
        healthDown()
        
    # Health up    
    if display.pressed(badger2040.BUTTON_C) or display.pressed(badger2040.BUTTON_UP):
        healthUp()
        
    #Invert display
    if display.pressed(badger2040.BUTTON_B):
        if (DISPLAY_INVERTED == False):
            DISPLAY_INVERTED = True
        else:
            DISPLAY_INVERTED = False    
        display.invert(DISPLAY_INVERTED)
            

    #Update the Display
    display.update()

    # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()
