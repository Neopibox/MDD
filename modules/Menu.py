# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Menu.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     03/05/2016 ##
##################################################################

# Modules système
from xml.dom.minidom import parse
import sys
import select
# Modules personnalisés
import Utils
import Game


# constructeur du menu #

def create():
        menu = dict()
        menu["current"] = dict()
        menu["windows"] = dict()
        menu["transitions"] = []        #<-------------- A MODIFIER
        
        # recuperation des infos du fichier xml pour la construction du menu
        path = "assets/menu/Menu.xml"
        doc = parse(path)
        rootElement = doc.documentElement
        
        # recuperation des noms et des données de chaque fenetre pour la creation du dictionnaire menu
        windowNodes = rootElement.getElementsByTagName("windows")
        windowSize = windowNodes.length
        
        for i in range(windowSize):
                #Permet de recuperer le nom de la fenetre pour chaque balise i
                windowTag = windowNodes[i]
                                
                windowName = windowTag.getAttribute("name")
                #print windowTag.attributes.keys()  #permet de recuperer le nom de chaque attribut
                
                
                
                #Recuperation des donnees de chaque fenetre                      #Data
                data = []
                
                #Recuperation du fond de la fenetre
                background=dict()
                background["content"] = []
                background["color"] = []
                
                backgroundTag = windowTag.getElementsByTagName("background")[0]
                container = backgroundTag.firstChild.nodeValue.split("\n")  #Recuperation du texte stocke entre les balises

                for line in container:
                        background["content"].append(list(line))

                
                if backgroundTag.hasAttributes():
                        color = backgroundTag.getAttribute("color")
                        backgroundColor = backgroundTag.getAttribute("backgroundColor")
                        background["color"] = (color, backgroundColor)
                else:
                        background["color"] = (" "," ")
               
               
                #Recuperation des textes de la fenetre
                texts=[]
                textTag = windowTag.getElementsByTagName("text")                       # Balises de texte dans liste textTag
                numberText = textTag.length                                       # Nombre de balises text de la fenetre
                for t in range(numberText):
                        # la variable thisText stocke, a chaque tour de boucle une balise text dans l'ordre où elle se trouve dans le fichier
                        thisText = textTag[t]                                     
                        text=dict()
                        
                        text["content"] = thisText.firstChild.nodeValue
                        x = thisText.getAttribute("x")
                        y = thisText.getAttribute("y")
                        text["position"] = (x,y)
                        
                        color = thisText.getAttribute("color")
                        backgroundColor = thisText.getAttribute("backgroundColor")
                        text["color"] = (color, backgroundColor)
                        
                        text["form"] = thisText.getAttribute("form")
                        
                        texts.append(text)
                
                
                
                #Recuperation des buttons de la fenetre
                button=dict()
                button["selected"]=None
                button["list"]=[]
                
                buttonTag = windowTag.getElementsByTagName("button")
                numberButton = buttonTag.length
                for b in range(numberButton):
                        # la variable thisButton stocke, a chaque tour de boucle une balise button dans l'ordre où elle se trouve dans le fichier
                        thisButton = buttonTag[b]
                        buttonName = thisButton.firstChild.nodeValue
                        button["list"].append(buttonName)
                        
                        #Attribuer un bouton de selectionner pour l'initialisation dans chacune des fenetres
                        button["selected"]=buttonTag[0].firstChild.nodeValue

                data = {"background": background, "texts": texts, "buttons": button}
                
                window = {windowName : data}
                menu["windows"].update(window)
        return menu


# Renvoie le nom de la fenetre courante
def getCurrentWindowName(menu):
        return menu["current"]["name"]

## Renvoie les donnees de la fenetre courante
#def getCurrentWindowData(menu):
        #return menu["current"]["data"]



# Renvoie le texte-image du fond de la fenetre
def getCurrentWindowBackgroundContent(menu):
        return menu["current"]["data"]["background"]["content"]

# Renvoie les couleurs de l'image de fond de la fenetre
def getCurrentWindowBackgroundColor(menu):
        return menu["current"]["data"]["background"]["color"]




# Renvoie la liste des boutons
def getCurrentWindowButtonList(menu):
        return menu["current"]["data"]["buttons"]["list"]

# Renvoie le bouton selectionne 
def getCurrentWindowButtonSelected(menu):
        return menu["current"]["data"]["buttons"]["selected"]


def setCurrentWindowButtonSelected(menu, buttonName):
        menu["current"]["data"]["buttons"]["selected"] = buttonName




# Renvoie les textes avec leurs parametres
def getCurrentWindowText(menu):
        return menu["current"]["data"]["texts"]



# Attribue le nom et les donnees à afficher dans la fenetre courante
def setCurrentWindow(menu, windowName):
        for window in menu["windows"]:
                if window == windowName:
                        name = window
                        data = menu["windows"][window]
                        menu["current"].update({"name": name, "data": data})  #current["Name"], current["data"]
                        break

def getBackgroundWindow(menu):
        return menu["windows"]["frame"]["background"]



# Affiche la fenetre courante
def show(menu):
      
        #Afficher le fond de la fenetre
        background = getBackgroundWindow(menu)["content"]
        color, backgroundColor = getBackgroundWindow(menu)["color"]
        Utils.setTextColor(color, backgroundColor)
       
        for y in range(0, len(background)):
                for x in range(0, len(background[y])):
                        if background[y][x] != " ":
                                Utils.goto(x,y)                                                         # A reutiliser pour affichage
                                sys.stdout.write(background[y][x]+"\n")

        Utils.resetTextFormat()    
         
        foreground = getCurrentWindowBackgroundContent(menu)
        color, backgroundColor = getCurrentWindowBackgroundColor(menu)
        Utils.setTextColor(color, backgroundColor)
        
        for y in range(0, len(foreground)):
                for x in range(0, len(foreground[y])):
                        Utils.goto(x+2,y+1)                                                         # A reutiliser pour affichage
                        sys.stdout.write(foreground[y][x]+"\n")
        Utils.resetTextFormat()   
        

        button = getCurrentWindowButtonList(menu)
        # affichage des bouttons en ligne 
        #for x in range(0, len(button)):
                #Utils.goto(x*30+20,40)                                                         # A reutiliser pour affichage
                #sys.stdout.write(button[x]+"\n")
        
        
        for y in range(0, len(button)):
                Utils.goto(70,y*2+28)                                                         # A reutiliser pour affichage
                if button[y] == getCurrentWindowButtonSelected(menu):
                        Utils.setTextColor("black", "white")
                        sys.stdout.write("> "+button[y]+"\n")
                else : 
                        Utils.resetTextFormat()
                        sys.stdout.write("  "+button[y]+"\n")
                Utils.resetTextFormat()        
        
        
        #affichage des textes
        for t in list(getCurrentWindowText(menu)):
                texte = t["content"]
                color, backgroundColor = t["color"]
                form = t["form"]
                x, y = t["position"]

                Utils.goto(x,y)
                Utils.setTextForm(form)
                Utils.setTextColor(color, backgroundColor)
                
                sys.stdout.write(texte+"\n")
                Utils.resetTextFormat()
                
        


def interact(menu, key):
        
        # Changer le bouton selectionne de la fenetre     
        buttonSelected = getCurrentWindowButtonSelected(menu)
        buttonList = getCurrentWindowButtonList(menu)
        
        index = buttonList.index(buttonSelected)
        if key == "z": 
                if index-1 >= 0:
                        setCurrentWindowButtonSelected(menu, buttonList[index-1])
        elif key == "s":
                if index+1 <= len(buttonList)-1:
                        setCurrentWindowButtonSelected(menu, buttonList[index+1])
        
        # Valider le choix de la fenetre
        elif key == "d": 
                changeWindow(menu) # Changement de fenetre
                
        
        

def changeWindow(menu):
        
        buttonSelected = getCurrentWindowButtonSelected(menu)
        
        if buttonSelected == "Retour":
                transitionSize = len(getTransition(menu))
                setCurrentWindow(menu, menu["transitions"][transitionSize-1])
        if buttonSelected == "Quit":
                quit() 
        
        else:
                addTransition(menu, getCurrentWindowName(menu))
                setCurrentWindow(menu, buttonSelected)


#def createTransition():

def addTransition(menu, nextWindow):
        menu["transitions"].append(nextWindow)

def getTransition(menu):
        return menu["transitions"]


if __name__ == "__main__":
        #initialisation
        menu = create()
        setCurrentWindow(menu,"mainMenu")
        
        #print menu["current"]
        #print getCurrentWindowName(menu)
        #print getCurrentWindowData(menu)
        #print getCurrentWindowBackgroundContent(menu)
        #show(menu)
        def isData():
                #recuperation des elements clavier
                return select.select([sys.stdin], [], [], 0.0) == ([sys.stdin], [], [])
        
 
        
        while True:
                getCurrentWindowButtonSelected(menu)
                if isData():
                        key = sys.stdin.read(1)
                        interact(menu, key)
        