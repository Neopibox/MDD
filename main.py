# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Main.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules système
import sys
import os
import time
import select
import tty 
import termios


# Modules personnalisés
sys.path.append('./modules/')
import Game
import Utils
import Player
import Menu


# Interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

# Donnee du jeu
direction = "None"

game = Game.create()
menu = Menu.create()

refresh = True

def init():
        #interaction clavier
        tty.setcbreak(sys.stdin.fileno())
        
        #cacher le curseur
        os.system('setterm -cursor off')
        #os.system('setterm -repeat off')
        

        Menu.setCurrentWindow(menu,"mainMenu")


        
#def show():
        #effacer la console 
        #sys.stdout.write("\033[1;1H")
        #sys.stdout.write("\033[2J")
        #os.system('setterm -clear all')
       
        
        ##affichage du joueur)
        ##deplacement du joueur:
        #x, y = Player.getPosition(player)
        #Utils.goto(x,y)
        #sys.stdout.write("Link")
        
        

def run():
        while True:
                
                currentWindowName = Menu.getCurrentWindowName(menu)
                if currentWindowName != "Game":
                        if refresh==True:
                                Menu.show(menu)
                else:
                        Game.show(game)
                interact()
                #move()
                time.sleep(0.2)
        
#def move():
        #global player, direction      
       
        ##deplacement du joueur:
        #x, y = Player.getPosition(player)
        #dt = 0.25

        #if direction == 'Up': Player.setPosition(player, x, y-1*dt)
        #if direction == 'Down': Player.setPosition(player, x, y+1*dt)
        #if direction == 'Right': Player.setPosition(player, x+2*dt, y)
        #if direction == 'Left': Player.setPosition(player, x-2*dt, y)
        #direction = " "

        
        #print Player.getPosition(player)    
        

def interact(): 
        global direction, refresh, game
       
        refresh = False
        #gestion des evenements clavier
        if isData():                                    #si une touche est appuyee
                read = sys.stdin.read(1)
                
                currentWindowName = Menu.getCurrentWindowName(menu)
                
                if currentWindowName != "Game":
                        Menu.interact(menu, read)
                else:
                        Game.interact(game, read)
                        
                if read == "\x1b": 
                        quit()                          # \x1b = touche echap / appel de la fonction qui permet de quitter le jeu

                #elif read == "\x08": 
                refresh = True
                
                
                
        
        
        while isData():
                sys.stdin.read(5)
                #termios.tcflush(sys.stdin, termios.TCIFLUSH)   # Permet de vider, le buffer des touches d'entree
                

def isData():
        #recuperation des elements clavier
        return select.select([sys.stdin], [], [], 0.0) == ([sys.stdin], [], [])

def quit():
        global old_settings
        #restauration des parametres du terminal
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        
        #rendre visible le curseur
        os.system('setterm -cursor on')
        
        sys.exit()
init()
run()