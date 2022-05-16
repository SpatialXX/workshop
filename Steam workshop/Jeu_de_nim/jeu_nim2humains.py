import pygame
from pygame.locals import *
import graphe_oriente
import joueur
import random

# lancement des modules inclus dans pygame
pygame.init() 
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("comicsansms", 30)
# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jeu de Nim") 
# chargement de l'image de fond
fond = pygame.image.load('background.png')

# creation des joueurs
player1 = joueur.Joueur()
player2 = joueur.Joueur()

#boutons cliquables joueur 1
zone1 = pygame.image.load("b1.png") #image du bouton
zone1rect = pygame.Rect(10,10,30,30) #rectangle autour de l'image (10,10) coordonnées et (30,30) largeur et hauteur
zone2 = pygame.image.load("b2.png")
zone2rect=pygame.Rect(10,50,30,30)
zone3 = pygame.image.load("b3.png")
zone3rect = pygame.Rect(10,90,30,30)

#boutons cliquables joueur2
zone4rect = pygame.Rect(700,10,30,30)
zone5rect = pygame.Rect(700,50,30,30)
zone6rect = pygame.Rect(700,90,30,30)

#reponse question rejouer :
oui = pygame.image.load("oui.png")
ouirect = pygame.Rect(10,450,50,50)

non = pygame.image.load("non.png")
nonrect = pygame.Rect(70,450,50,50)


#allumettes
nbAllumettes = 12
allumette = pygame.image.load('allumette.png')

running = True # variable de la boucle de jeu
#choix du joueur qui commence au hasard
n = random.randint(1,2)
if n == 1 :
    player1.joue = True
else :
    player2.joue = True
    
#variables de gestion de fin de partie
fin = False
augmente_score = False
humainVShumain = True

### BOUCLE DE JEU  ###
while running : # boucle infinie pour laisser la fenêtre ouverte
    if humainVShumain : 
        # dessin du fond
        screen.blit(fond,(0,0))
        if player1.joue == True:
            labelJ = myfont.render("joueur1 joue", 1, (255,0,0))
            screen.blit(labelJ, (320, 10))
        if player2.joue == True:
            labelJ2 = myfont.render("joueur2 joue", 1, (255,0,0))
            screen.blit(labelJ2, (320, 10))
        #affichage des allumettes :
        for i in range( nbAllumettes) :
            screen.blit(allumette,(300,i*35+100))

        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                
           
           # gestion de la souris
            elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                if event.button == 1: # 1= clique gauche
                    if zone1rect.collidepoint(event.pos) and player1.joue == True:
                        print(1)
                        if nbAllumettes>=2 :
                            nbAllumettes -=1
                        player1.joue = False
                        player2.joue = True
                    ###Question 2) compléter pour les 5 autres zones correspondant aux boutons de jeux
                    ###Pour rejouer, on teste si le joueur appuie sur oui ou non    
                    if ouirect.collidepoint(event.pos) :
                        fin = False
                        #on choisit au hasard qui joue
                        n = random.randint(1,2)
                        if n == 1 :
                            player1.joue = True
                        else :
                            player2.joue = True
                        nbAllumettes = 12
                        player1.gagne = False
                        player2.gagne = False
                    if nonrect.collidepoint(event.pos) :
                        running = False
        #affichage des boutons de choix
        screen.blit(zone1,(10,10))
        screen.blit(zone2,(10,50))
        screen.blit(zone3,(10,90))
        screen.blit(zone1,(700,10))
        screen.blit(zone2,(700,50))
        screen.blit(zone3,(700,90))
        #gestion de la fin de partie quand il rest une seule allumette
        if nbAllumettes == 1 and player1.joue == True :
            #c'est au joueur 1 de jouer et il reste une seule allumette
            #donc il a perdu
            print('joueur2 gagne')
            fin = True
            player2.gagne = True
            player2.joue = None
            player1.joue = None
            augmente_score = True # permet de dire qu'il faut augmenter le score
        if nbAllumettes == 1 and player2.joue == True :
            ####à compléter question 3)###
            pass
        #affichage du gagnant et du score
        if fin == True : #Si fin de partie
            if player1.gagne :
                label = myfont.render("Le gagnant est joueur1", 1, (255,255,0))
                if augmente_score == True :
                    player1.score+=1
                    augmente_score = False #permet de n'augmenter le score qu'une seule fois
                    
            else :
                ###à compléter question 4) pour gérer quand c'est player 2 qui gagne
                pass
            #gérer la possibilité de rejouer       
            question = myfont.render("Voulez-vous rejouer ?",1,(0,0,0))
            score = myfont.render("joueur 1 a "+str(player1.score)+" points et le joueur 2 a "+str(player2.score)+"points",1,(0,0,0))
            screen.blit(label, (200, 10))
            screen.blit(question,(10,400))
            screen.blit(oui,(10,450))
            screen.blit(non,(70,450))
            screen.blit(score,(10,500))
    
    pygame.display.update() # mise à jour pour ajouter tout changement à l'écran
pygame.quit()
