# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Mob.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules système
import sys

# Modules personnalisés
import Utils

def create():
        mob = dict()
        mob["type"] = ""
        mob["x"] = -1
        mob["y"] = -1
        mob["health"] = -1
        mob["strength"] = -1
        mob["resistance"] = -1
        mob["damage"] = -1
        mob["sprite"] = ""
        return mob

def move(m):
        return

def show(m):
        Utils.goto(m["x"], m["y"])
        sys.stdout.write(m["sprite"])
        return

def getType(m):
        return m["type"]
        
def setType(m, type):
        m["type"] = type
        return

def getPosition(m):
        return (m["x"], m["y"])
     
def setPosition(m, x, y):
        m["x"] = x
        m["y"] = y
        return

def getHealth(m):
        return m["health"]
        
def setHealth(m, health):
        m["health"] = health
        return

def getStrength(m):
        return m["strength"]
        
def setStrength(m, strength):
        m["strength"] = strength
        return

def getResistance(m):
        return m["resistance"]
        
def setResistance(m, resistance):
        m["resistance"] = resistance
        return

def getDamage(m):
        return m["damage"]
        
def setDamage(m, damage):
        m["damage"] = damage
        return

def getSprite(m):
        return m["sprite"]
        
def setSprite(m, sprite):
        m["sprite"] = sprite
        return