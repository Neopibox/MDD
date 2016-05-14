# -*- coding: utf-8 -*-
##################################################################
##                                                              ##
##           The Legend Of Zelda - A Link to the Rogue          ##
##          Un projet de Methode de Developpement (MDD)         ##
##                                                              ##
##                           Utils.py                           ##
##                                                              ##
## LEVEQUE Dorian & ROUE Evan   S2P     ENIB         22/04/2016 ##
##################################################################

import sys
import os

def goto(x=0, y=0):
        s_x = str(int(x)+1)
        s_y = str(int(y))
        txt = "\033[" + s_y + ";" + s_x + "H"
        sys.stdout.write(txt)

def setTextColor(color="white", backgroundColor="black"):
        foreground = dict()
        foreground["black"] = 30
        foreground["red"] = 31
        foreground["green"] = 32
        foreground["yellow"] = 33
        foreground["blue"] = 34
        foreground["magenta"] = 35
        foreground["cyan"] = 36
        foreground["light gray"] = 37
        foreground["dark gray"] = 90
        foreground["light red"] = 91
        foreground["light green"] = 92
        foreground["light yellow"] = 93
        foreground["light blue"] = 94
        foreground["light magenta"] = 95
        foreground["light cyan"] = 96
        foreground["white"] = 97
        
        background = dict()
        background["black"] = 40
        background["red"] = 41
        background["green"] = 42
        background["yellow"] = 43
        background["blue"] = 44
        background["magenta"] = 45
        background["cyan"] = 46
        background["light gray"] = 47
        background["dark gray"] = 100
        background["light red"] = 101
        background["light green"] = 102
        background["light yellow"] = 103
        background["light blue"] = 104
        background["light magenta"] = 105
        background["light cyan"] = 106
        background["white"] = 107
        
        for c in foreground : 
                if c == color:
                        foreColor = str(int(foreground[c]))
                        sys.stdout.write("\033["+foreColor+"m")
                        break
        for b in background :
                if b == backgroundColor:
                        backColor = str(int(background[b]))
                        sys.stdout.write("\033["+backColor+"m")
                        break

        #os.system("setterm -foreground "+color)
        #os.system("setterm -background "+backgroundColor)
        return

def setTextForm(form):
        parametres = form        
        for i in parametres.split(", "):
                os.system("setterm -"+i+" on")
        return

def resetTextFormat():
        sys.stdout.write("\033[0m")
        #os.system("setterm -default")

if __name__=="__main__":
        #Test 1
        print "Test 1"
        form = "bold, underline, half-bright"
        setTextForm(form)
        sys.stdout.write("salut\n")
        resetTextFormat()
        sys.stdout.write("coucou\n")
        
        #Test 2
        print "-------------\nTest 2"
        print "Test 2"
        form = ""
        setTextForm(form)
        sys.stdout.write("salut\n")
        resetTextFormat()
        sys.stdout.write("coucou\n")
        
        #Test 3
        print "-------------\nTest 3"
        print "Test 3"
        setTextColor('blue', 'white')
        sys.stdout.write("salut\n")
        resetTextFormat()
        sys.stdout.write("coucou\n")
        
        #Test 4
        print "-------------\nTest 4"
        print "Test 4"
        setTextColor('yellow', 'red')
        goto(20,10)
        sys.stdout.write("salut\n")
        resetTextFormat()
        sys.stdout.write("coucou\n")
        
        