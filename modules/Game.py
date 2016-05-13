# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Game.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules personnalisés
import Dungeon
import Player

def create():
        game = dict()
        game["player"] = Player.create()
        game["dungeon"] = Dungeon.create("forest")
        
        Dungeon.generate(game["dungeon"])
        Player.setPosition(game["player"], 5, 5)
        
        return game

def show(g):
        # Affichage de l'interface
        
        # Affichage du donjon
        Dungeon.show(g["dungeon"])
        
        # Affichage du joueur
        Player.show(g["player"])

def interact(g, key):
                if key == "z": 
                        direction = "up"                # le joueur se déplace vers Direction Haut
                elif key == "q": 
                        direction = "left"              # le joueur se déplace vers Direction Gauche
                elif key == "s": 
                        direction = "down"              # le joueur se déplace vers Direction Bas
                elif key == "d": 
                        direction = "right"             # le joueur se déplace vers Direction Droite
                
                Player.move(g["player"], direction)
                
                #elif key == "p":                      # appel de la fonction pause