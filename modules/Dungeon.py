# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			     Dungeon.py	        		##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules système
import os
import math
import random

# Modules personnalisés
import Room

def create(name):
        d = dict()
        d["name"] = name
        d["currentRoom"] = None

        return d

def generate(d):
        # On récupère la liste des salles possibles pour ce donjon
        roomFiles = os.listdir("./assets/rooms/" + d["name"] + "/")
        roomsTotalNumber = len(roomFiles)
        remainingRooms = []
        for i in range(roomsTotalNumber):
                room = Room.create(d["name"], d["name"] + "_" + str(i+1))
                remainingRooms.append(room)
        
        # On choisit aléatoirement la première salle
        d["currentRoom"] = pickUpRandomRoom(remainingRooms)
        
        # Appel de la fonction récursive pour déterminer les salles adjacentes
        recursiveGeneration(d, remainingRooms, d["currentRoom"], 1, roomsTotalNumber)

# Cette fonction génère les salles adjacentes à une case donnée. Elle est, par construction, récursive.
# Elle etudie pour chaque direction, s'il faut mettre (ou non), une salle aléatoire prise dans la liste des salles restantes.
# Si oui, alors la fonction se rappelle-elle même pour définir les salles adjacentes de la salle venant d'être placé.
def recursiveGeneration(d, remainingRooms, currentRoom, roomLevel, roomsTotalNumber):
        # Réglage des coefficients
        depthCoefficient = 0.1
        remainingRoomCoefficient = 1
        
        if(len(remainingRooms) == 0):
                return
        
        for door in ["up", "down", "left", "right"]:
                # Calcule la probabilité
                depthDrivenCoefficient = math.exp(-(roomLevel * depthCoefficient))
                remainingRoomDrivenCoefficient = remainingRoomCoefficient*(len(remainingRooms) / roomsTotalNumber)
                probability = round(depthDrivenCoefficient*remainingRoomDrivenCoefficient*random.rand())
                
                if(roomLevel >= 7):     # Sécurité afin d'éviter d'avoir des donjons trop profonds
                        p = 0
                
                if(probability == 1):
                        if door == "up":
                                if(Room.getUpRoom(currentRoom) == None):
                                        upRoom = pickUpRandomRoom(remainingRooms)
                                        Room.setUpRoom(currentRoom, upRoom)
                                        recursiveGeneration(d, remainingRooms, upRoom, roomLevel + 1, roomsTotalNumber)
                        elif door == "down":
                                if(Room.getDownRoom(currentRoom) == None):
                                        downRoom = pickUpRandomRoom(remainingRooms)
                                        Room.setDownRoom(currentRoom, downRoom)
                                        recursiveGeneration(d, remainingRooms, downRoom, roomLevel + 1, roomsTotalNumber)
                        elif door == "left":
                                if(Room.getLeftRoom(currentRoom) == None):
                                        leftRoom = pickUpRandomRoom(remainingRooms)
                                        Room.setLeftRoom(currentRoom, leftRoom)
                                        recursiveGeneration(d, remainingRooms, leftRoom, roomLevel + 1, roomsTotalNumber)
                        elif door == "right":
                                if(Room.getRightRoom(currentRoom) == None):
                                        rightRoom = pickUpRandomRoom(remainingRooms)
                                        Room.setRightRoom(currentRoom, rightRoom)
                                        recursiveGeneration(d, remainingRooms, rightRoom, roomLevel + 1, roomsTotalNumber)

# Renvoie une salle prise aléatoirement dans la liste des salles restantes et l'enleve de la liste
def pickUpRandomRoom(remainingRooms):
        room = remainingRooms[random.randint(0, len(remainingRooms) - 1)]
        remainingRooms.remove(room)
        return room
                                        
def show(d):
        Room.show(d["currentRoom"])