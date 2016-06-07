# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Room.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules système
from xml.dom.minidom import parse
from string import *

# Modules personnalisés
import Chest
import Arrow
import Entity
import Player
import Mob
import Utils

def create(dungeonName, roomName):
        # -- Initialisation du dictionnaire --
        r = dict()
        r["background"]=[]
        r["entity"]=[]
        r["chests"]=[]
        r["arrows"]=[]
        r["upRoom"]=None
        r["downRoom"]=None
        r["leftRoom"]=None
        r["rightRoom"]=None
        
        # -- Parsage du fichier XML correspondant --
        path = "./assets/rooms/" + dungeonName + "/" + roomName + ".xml"
        doc = parse(path)
        rootBeacon = doc.documentElement

        # Récupération du background
        background = rootBeacon.getElementsByTagName("background")[0].firstChild.nodeValue.split("\n", 41)
        del background[0]
        del background[-1]
        for line in background:
                r["background"].append(list(line))

        # Récupération des mobs
        mobs = rootBeacon.getElementsByTagName("mob")
        nb_mobs = mobs.length
        for i in range(nb_mobs):
                mob = Mob.create()
                #Mob.setType(mob, mobs[i].getAttribute("type"))
                #Mob.setPosition(mob, int(mobs[i].getAttribute("x")), int(mobs[i].getAttribute("y")))
                #Mob.setHealth(mob, int(mobs[i].getAttribute("health")))
                #Mob.setStrength(mob, float(mobs[i].getAttribute("strength")))
                #Mob.setResistance(mob, float(mobs[i].getAttribute("resistance")))
                #Mob.setDamage(mob, int(mobs[i].getAttribute("damage")))
                #Mob.setSprite(mob, mobs[i].firstChild.nodeValue)
                Entity.setType(mob, mobs[i].getAttribute("type"))
                Entity.setPosition(mob, int(mobs[i].getAttribute("x")), int(mobs[i].getAttribute("y")))
                Entity.setHealth(mob, int(mobs[i].getAttribute("health")))
                Entity.setStrength(mob, float(mobs[i].getAttribute("strength")))
                Entity.setResistance(mob, float(mobs[i].getAttribute("resistance")))
                Entity.setDamage(mob, int(mobs[i].getAttribute("damage")))
                Entity.setSprite(mob, strip(mobs[i].firstChild.nodeValue))
                r["entity"].append(mob)
        
        # Récupération des coffres
        chests = rootBeacon.getElementsByTagName("chest")
        nb_chests = chests.length
        for i in range(nb_chests):
                chest = Chest.create()
                Chest.setPosition(chest, int(chests[i].getAttribute("x")), int(chests[i].getAttribute("y")))
                
                # Ajout des items
                items = chests[i].childNodes
                
                for item in items:
                        if item.nodeName == "bonus":
                                bonus = Bonus.create()
                                Bonus.setName(bonus, item.getAttribute("name"))
                                Bonus.setAmount(bonus, item.getAttribute("amount"))
                                Chest.addItem(chest, bonus)
                        elif item.nodeName == "bow":
                                bow = Bow.create()
                                Bow.setName(bow, item.getAttribute("name"))
                                Bow.setDamage(bow, int(item.getAttribute("damage")))
                                Bow.setSprite(bow, item.firstChild.nodeValue)
                                Chest.addItem(chest, bow)
        return r

def getPlayer(r):
        for currentEntity in r["entity"]:
                if(Entity.getType(currentEntity) == "player"):
                        return currentEntity

def addEntity(r, e):
       r["entity"].append(e)

def removeEntity(r, e):
        r["entity"].remove(e) 

def run(r, dt):
        player = getPlayer(r)

        for currentArrow in r["arrows"]:
                newX, newY = Arrow.live(currentArrow, dt)
                
                if isFree(r, newX, newY):
                        Entity.setPosition(currentArrow, newX, newY)
                else:
                        r["arrows"].remove(currentArrow)
                
                # Si une entité (Mob ou Joueur) a été touché, il faut lui enlever de la vie
                hurtedEntity = getEntityByPosition(r, newX, newY)
                if hurtedEntity != -1:
                        health = Entity.getHealth(hurtedEntity)
                        resistance = Entity.getResistance(hurtedEntity)
                        newHealth = health - (Arrow.getDamage(currentArrow)/resistance)
                        Entity.setHealth(hurtedEntity, newHealth)
                        r["arrows"].remove(currentArrow)
         
        for currentEntity in r["entity"]:
                if(Entity.getType(currentEntity) == "player"):
                        newX, newY = Player.live(currentEntity, dt)
                if(Entity.getType(currentEntity) == "skeleton"):
                        newX, newY = Mob.live(currentEntity, player, 3, dt)
                if(Entity.getType(currentEntity) == "guardian"):
                        newX, newY = Mob.live(currentEntity, player, 6, dt)
                if(Entity.getType(currentEntity) == "boss"):
                        newX, newY = Mob.live(currentEntity, player, 12, dt)

                if isFree(r, newX, newY): #and getEntityByPosition(r, newX, newY) == -1:
                        Entity.setPosition(currentEntity, newX, newY)

def launchArrow(r, entity):
        arrow = Arrow.create()
        
        ax, ay = Entity.getPosition(entity)
        evx, evy = Entity.getDirection(entity)
        
        ax, ay = ax + evx, ay + evy
        
        Arrow.setPosition(arrow, ax, ay)
        Arrow.setSpeed(arrow, evx*30, evy*30)
        Arrow.setDamage(arrow, Entity.getDamage(entity)*Entity.getStrength(entity))
        
        r["arrows"].append(arrow)

#def movePlayer(direction):
        #x, y = Dungeon.getEntityPosition(getDungeon(g), "player")
        #vx, vy = Dungeon.getEntitySpeed(getDungeon(g), "player")

        

#def collide():
        #x, y = Player.getPosition(g["player"])
        #currentRoom = Dungeon.getCurrentRoom(g["dungeon"])

        #if (key == "z") and (Room.get(currentRoom, x, y-1) == " "): 
                #y = y - 1             # le joueur se déplace vers Direction Haut
        #elif (key == "q") and (Room.get(currentRoom, x-1, y) == " "): 
                #x = x - 1             # le joueur se déplace vers Direction Gauche
        #elif (key == "s") and (Room.get(currentRoom, x, y+1) == " "): 
                #y = y + 1             # le joueur se déplace vers Direction Bas
        #elif (key == "d") and (Room.get(currentRoom, x+1, y) == " "): 
                #x = x + 1             # le joueur se déplace vers Direction Droite
def show(r):
        # Affichage du fond
        for y in range(0, len(r["background"])):
                for x in range(0, len(r["background"][y])):
                        Utils.goto(x+2, y+2)
                        Utils.write(r["background"][y][x]+"\n")
        
        # Affichage des coffres
        for currentChest in r["chests"]:
                x, y = Chest.getPosition(currentChest)
                Utils.goto(x+2, y+1)
                Chest.show(currentChest)
        
        # Affichage des entités
        for currentEntity in r["entity"]:
                Entity.show(currentEntity)
        
        # Affichage des projectiles
        for currentArrow in r["arrows"]:
                Arrow.show(currentArrow)

def drawDoors(r):
        # Affichage des portes
        if r["upRoom"] != None:
                x = round(len(r["background"][1]) / 2, 1) - 8
                y = 0
                drawDoor(r, x, y, 16, 2)

        if r["downRoom"] != None:
                x = round(len(r["background"][1]) / 2, 1) - 8
                y = len(r["background"]) - 2
                drawDoor(r, x, y, 16, 2)

        if r["leftRoom"] != None:
                x = 0
                y = round(len(r["background"]) / 2, 1) - 4
                drawDoor(r, x, y, 3, 8)

        if r["rightRoom"] != None:
                x = len(r["background"][1]) - 3
                y = round(len(r["background"]) / 2, 1) - 4
                drawDoor(r, x, y, 3, 8)

def drawDoor(r, x, y, w, h):
        for i_y in range(0, h):
                for i_x in range(0, w):
                       r["background"][int(y+i_y)][int(x+i_x)] = " "

def getChestByPosition(r, x, y):
        # On parcourt la liste des coffres de la salle
        for currentChest in r["chests"]:
                if Chest.getPosition(currentChest) == (x,y):
                        return currentChest
        
        return -1

def getEntityByPosition(r, x, y):
        # On parcourt la liste des entités de la salle
        for currentEntity in r["entity"]:
                ex, ey = Entity.getPosition(currentEntity)
                ex, ey = int(round(ex)), int(round(ey))
                
                if (ex, ey) == (int(round(x)), int(round(y))):
                        return currentEntity
        
        return -1

def getUpRoom(r):
        return r["upRoom"]

def setUpRoom(r, up_room):
        r["upRoom"] = up_room
        #drawDoors(r)

def getDownRoom(r):
        return r["downRoom"]

def setDownRoom(r, down_room):
        r["downRoom"] = down_room
        #drawDoors(r)

def getLeftRoom(r):
        return r["leftRoom"]

def setLeftRoom(r, left_room):
        r["leftRoom"] = left_room
        #drawDoors(r)

def getRightRoom(r):
        return r["rightRoom"]

def setRightRoom(r, right_room):
        r["rightRoom"] = right_room
        #drawDoors(r)

def isFree(r, x, y):
        if x > 79 or x < 1 or y > 39 or y < 1:
                return False
        elif r["background"][int(round(y))][int(round(x))].encode("utf-8") == " ":
                return True
        else:
                return False
        
def getEntityPosition(r, type):
        for currentEntity in r["entity"]:
                if Entity.getType(currentEntity) == type:
                        return Entity.getPosition(currentEntity)

def setEntityPosition(r, type, x, y):
        for currentEntity in r["entity"]:
                if Entity.getType(currentEntity) == type:
                        Entity.setPosition(currentEntity, x, y)
                        return

# Tests
if __name__ == "__main__":
        room = create("forest", "forest_1")
        Utils.goto(0, 0)
        setUpRoom(room, "anotherRoom")
        show(room)
        print getEntityPosition(room, "player")
        setEntityPosition(room, "player", 20, 30)
        print getEntityPosition(room, "player")

        
