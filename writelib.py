import os
import time
global consolas
consolas = ''

# I made my shitty code into a "library" epic awesome
# Welcome to WriteLib - @literallypiedpiper on Discord

def conspartclear():
    os.system("clear")

def consclear():
    global consolas
    consolas = ""
    conspartclear()

def conswrite(string=""):
    global consolas
    consolas = string

def consprint():
    global consolas
    print(consolas)

def write(string="Sample Text", delay=0.05, sleepafter=0, noconsolasnewline=False):
    # Makes the variable where it stores type() output global, then splits the characters of the string variable into
    # a list
    global consolas
    stringlist = [*string]
    i = 0
    yo = ""
    # Defines the string length, the minus 1 added to prevent it from breaking
    string_length = len(stringlist) - 1
    # The loop that does the typing visual
    while i <= string_length:
        yo = yo + stringlist[i]
        i += 1
        conspartclear()
        print(consolas + yo + "█")
        time.sleep(delay)
    # If the new line parameter is True, then no newline
    if noconsolasnewline:
        consolas = consolas + yo
    else:
        consolas = consolas + yo + "\n"
    time.sleep(sleepafter)
    
