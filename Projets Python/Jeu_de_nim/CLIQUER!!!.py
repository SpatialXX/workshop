import pygame
from pygame.locals import *
import graphe_oriente
import joueur
import random

# lancement des modules inclus dans pygame
pygame.init() 
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont2 = pygame.font.SysFont("century_schoolbook", 30)
myfont = pygame.font.SysFont("hp_simplified_hans", 48)
# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Jeu de Nim") 
# chargement de l'image de fond
fond = pygame.image.load('textures/background.png').convert_alpha()

# creation des joueurs
player1 = joueur.Joueur()
player2 = joueur.Joueur()

# creation du graphe de jeu pour l'intelligence artificielle
G = graphe_oriente.GraphOriente()
###à compléter Partie B : question 2)
##créer le graphe de tous les coups possibles sommets + arcs

#boutons cliquables joueur 1

zone1rect = pygame.Rect(0,0,120,111) #rectangle autour de l'image (10,10) coordonnées et (30,30) largeur et hauteur
zone2rect=pygame.Rect(121,0,120,111)
zone3rect = pygame.Rect(242,0,120,111)

zone4rect = pygame.Rect(1081,0,120,111)
zone5rect = pygame.Rect(960,0,120,111)
zone6rect = pygame.Rect(839,0,120,111)


fleche1_g = pygame.Rect(0,239,60,60)
fleche2_g = pygame.Rect(0,295,60,60)

fleche1_d = pygame.Rect(1136,239,60,60)
fleche2_d = pygame.Rect(1136,295,60,60)

buy1 = pygame.Rect(869,240,104,44)
buy2 = pygame.Rect(869,310,104,44)

jvj_butt = pygame.Rect(261,387,163,116)
jvc_butt = pygame.Rect(526,387,163,116)
bout_butt = pygame.Rect(787,387,163,116)
quit_butt = pygame.Rect(439,524,343,82)
rule_butt = pygame.Rect(482,302,240,60)
retour_butt = pygame.Rect(0,0,81,91)

#reponse question rejouer :
oui = pygame.image.load('textures/oui.png').convert_alpha()
ouirect = pygame.Rect(530,450,50,50)

non = pygame.image.load('textures/non.png').convert_alpha()
nonrect = pygame.Rect(600,450,50,50)


#allumettes

nbAllumettes = 12


conk = pygame.image.load('textures/conk.png').convert_alpha()
bepis = pygame.image.load('textures/bepis.png').convert_alpha()
corn = pygame.image.load('textures/corn_cube.png').convert_alpha()
mone = pygame.image.load('textures/mone.png').convert_alpha()
nft = pygame.image.load('textures/nft.png').convert_alpha()
dogecoin  = pygame.image.load('textures/dogecoin.png').convert_alpha()
plush = pygame.image.load('textures/mogus_plush.png').convert_alpha()

retour = pygame.image.load('textures/retour.png').convert_alpha()
r_back = pygame.image.load('textures/r_back.png').convert_alpha()
regle = pygame.image.load('textures/regles.png').convert_alpha()

liste_images = []
for i in range(nbAllumettes):
    pif = random.randint(1,7)    
    if pif == 1:
        bien = conk
    elif pif == 2:
        bien = bepis
    elif pif == 3:
        bien = corn
    elif pif == 4:
        bien = mone
    elif pif == 5:
        bien = nft
    elif pif == 6:
        bien = dogecoin
    elif pif == 7:
        bien = plush
    liste_images.append(bien)


#allumette = pygame.image.load('textures/allumette.png')

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


pygame.mixer.init()        
pygame.mixer.music.load('textures/still_time_first_strike.ogg')
pygame.mixer.music.play(-1, 0.0)


###Boucle MENU : au choix : 2 joueurs humains ou 1 humain contre ordi en IA apprenante
menu = True
costume = False
fondmenu = pygame.image.load('textures/menu.png').convert_alpha()
f1d = pygame.image.load('textures/f1d.png').convert_alpha()
gui = pygame.image.load('textures/gui_select.png').convert_alpha()
humainVShumain = True
humainVSordi = False
place_gui1 = 480
place_gui2 = 480
bon_pas = False
rule=False
### BOUCLE DE JEU  ###
while running : # boucle infinie pour laisser la fenêtre ouverte

    while menu :
        
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                menu = False # menu est sur False
                running = False
            if costume == False or rule == False:
                if event.type == MOUSEBUTTONUP: 
                    if event.button == 1:
                        if jvj_butt.collidepoint(event.pos):
                            if player1.bon[player1.select] == True and player2.bon[player2.select] == True:
                                humainVShumain = True
                                humainVSordi = False
                                menu = False
                                player1.set_etat("humain")
                                player2.set_etat("humain")
                                costume = False
                                player1.hazard = random.randint(0,3)
                                player2.hazard = random.randint(0,3)
                                
                    
                        if jvc_butt.collidepoint(event.pos):
                            if player1.bon[player1.select] == True:
                                humainVSordi = True
                                humainVShumain = False
                                menu = False
                                player1.set_etat("humain")
                                player2.set_etat("ordi")
                                compt = 0
                                costume = False
                                player1.hazard = random.randint(0,3)
                                player2.hazard = random.randint(0,3)
                    
                        if bout_butt.collidepoint(event.pos):
                            costume = True
                            
                        if quit_butt.collidepoint(event.pos):
                            menu = False # menu est sur False
                            running = False
                        
                        if rule_butt.collidepoint(event.pos):
                            rule = True
                            
                            
                screen.blit(fondmenu,(0,0))
            if rule == True:
                if event.type == MOUSEBUTTONUP: # quand je relache le bouton
                    if event.button == 1: # 1= clique gauche
                        if retour_butt.collidepoint(event.pos):
                            if player1.bon[player1.select] == True and player2.bon[player2.select] == True:
                                rule = False
                screen.blit(regle,(0,0))  
                screen.blit(retour,(0,0))  
                
                                
                                
            if costume == True:
                   
                if event.type == MOUSEBUTTONUP: # quand je relache le bouton
                    
                    if event.button == 1: # 1= clique gauche
                        if retour_butt.collidepoint(event.pos):
                            if player1.bon[player1.select] == True and player2.bon[player2.select] == True:
                                costume = False
                                bon_pas = False
                            else:
                                bon_pas = True
                                
                                
                        
                        if fleche1_g.collidepoint(event.pos) and place_gui1 < 480 :
                            place_gui1 += 160
                            player1.select -= 1
                                                                
                        elif fleche1_d.collidepoint(event.pos)and place_gui1 > -1440:
                            place_gui1 -= 160
                            player1.select += 1


                        
                        elif fleche2_g.collidepoint(event.pos) and place_gui2 < 480 :
                            place_gui2 += 160
                            player2.select -= 1
                            
                        elif fleche2_d.collidepoint(event.pos)and place_gui2 > -1440:
                            place_gui2 -= 160
                            player2.select += 1                            

                        if buy1.collidepoint(event.pos) and player1.bon[player1.select] == False :
                            if player1.score == player1.cost[player1.select] or player1.score > player1.cost[player1.select]:
                                player1.bon[player1.select] = True
                                player1.score = player1.score - player1.cost[player1.select]

                        if buy2.collidepoint(event.pos) and player2.bon[player2.select] == False :
                            if player2.score == player2.cost[player2.select] or player2.score > player2.cost[player2.select]:
                                player2.bon[player2.select] = True
                                player2.score = player2.score - player2.cost[player2.select]
   
                black = pygame.color.Color('#000000')
                
                
                
                #659 240
                #154 240
                f2d = pygame.transform.flip(f1d, True, True)
                
                screen.blit(fond,(0,0))
                screen.blit(gui,(0,0))

                screen.blit(f2d,(0,235))
                screen.blit(f2d,(0,295))

                screen.blit(f1d,(1136,235))
                screen.blit(f1d,(1136,295))



                if player1.bon[player1.select] == False:
                    prix_1 = myfont2.render(str(player1.cost[player1.select]), 1, (255,255,255))
                    screen.blit(prix_1, (659, 240))
                
                nom_1 = myfont.render(str(player1.nom[player1.select]), 1, (158,236,85))
                screen.blit(nom_1, (160, 240))
                
                money1 = myfont2.render(str(player1.score), 1, (255,255,255))
                screen.blit(money1, (773, 240))
                
                if player2.bon[player2.select] == False:
                    prix_2 = myfont2.render(str(player2.cost[player2.select]), 1, (255,255,255))
                    screen.blit(prix_2, (659, 311))
                
                nom_2 = myfont.render(str(player2.nom[player2.select]), 1, (158,236,85))
                screen.blit(nom_2, (160, 311))
                
                money2 = myfont2.render(str(player2.score), 1, (255,255,255))
                screen.blit(money2, (773, 311))
                
                for i in range (player1.costume):
                    screen.blit(player1.cosmetic[i][0],(i*160+place_gui1,10))
                
                for i in range (player2.costume):
                    image = pygame.transform.flip(player2.cosmetic[i][0], True, False)
                    
                    screen.blit(image,(i*160+place_gui2,361))   
                
                screen.blit(retour,(0,0))   
                if bon_pas == True:
                    pas_bon = myfont.render("Un joueur a un personnage non acheter", 1, (255,0,0))
                    screen.blit(pas_bon, (81, 0))

        pygame.display.update()


    if humainVShumain == True : 
        # dessin du fond
        screen.blit(r_back,(0,0))
        if player1.joue == True:
            labelJ = myfont.render(player1.nom[player1.select]+" joue", 1, (158,236,0))
            screen.blit(labelJ, (450, 40))
        if player2.joue == True:
            labelJ2 = myfont.render(player2.nom[player2.select]+" joue", 1, (236,158,0))
            screen.blit(labelJ2, (450, 40))
        #affichage des allumettes :
        for i in range( nbAllumettes) :
            image = liste_images[i]
            
            screen.blit(image,(i*100,200))
        
        if player1.stupid == 0:
            screen.blit(player1.cosmetic[player1.select][player1.kalm],(10,311))
        else:
            screen.blit(player1.brainlet[player1.hazard],(10,311))
            
        image = pygame.transform.flip(player2.cosmetic[player2.select][player2.kalm], True, False)
        if player2.stupid == 0:
            screen.blit(image,(1050,311))
        else:
            image = pygame.transform.flip(player2.brainlet[player2.hazard], True, False)
            screen.blit(image,(1050,311))            
        
        
        
        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                
           
           # gestion de la souris
            elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                if event.button == 1: # 1= clique gauche
                    if zone1rect.collidepoint(event.pos) and player1.joue == True:

                        if nbAllumettes>=2 :
                            player2.kalm = 0
                            
                            if nbAllumettes < 5 and nbAllumettes -1 != 1:
                                player1.stupid = 1
                        
                            nbAllumettes -=1
                            player1.joue = False
                            player2.joue = True
                            
                            
                            

                            
                    if zone2rect.collidepoint(event.pos) and player1.joue == True :

                        if nbAllumettes>=3 :
                            player1.kalm = 0
                            player2.kalm = 0
                            
                            if nbAllumettes < 5 and nbAllumettes -2 != 1:
                                player1.stupid = 1
                        
                            nbAllumettes -=2
                            player1.joue = False
                            player2.joue = True
                            
                            
                            

                            
                    if zone3rect.collidepoint(event.pos) and player1.joue == True :

                        if nbAllumettes>=4 :
                            nbAllumettes -=3
                            player1.joue = False
                            player2.joue = True
                            
                            player1.kalm = 1
                            player2.kalm = 2



                        
                    if zone4rect.collidepoint(event.pos) and player2.joue == True:

                        if nbAllumettes>=2 :
                            player1.kalm = 0
                        
                            if nbAllumettes < 5 and nbAllumettes -1 != 1:
                                player2.stupid = 1
                        
                            nbAllumettes -=1
                            player2.joue = False
                            player1.joue = True
                            
                            
                            


                            
                    if zone5rect.collidepoint(event.pos) and player2.joue == True :

                        if nbAllumettes>=3 :
                            player1.kalm = 0
                            player2.kalm = 0
                            
                            if nbAllumettes < 5 and nbAllumettes -2 != 1:
                                player2.stupid = 1
                            
                            nbAllumettes -=2
                            player2.joue = False
                            player1.joue = True
                            
                            player1.kalm = 0
                            player2.kalm = 0
                            

                            
                    if zone6rect.collidepoint(event.pos) and player2.joue == True :

                        if nbAllumettes>=4 :
                            nbAllumettes -=3
                            player2.joue = False
                            player1.joue = True
                            
                            player1.kalm = 2
                            player2.kalm = 1


                            
                    if ouirect.collidepoint(event.pos) :
                        fin = False
                        n = random.randint(1,2)
                        if n == 1 :
                            player1.joue = True
                        else :
                            player2.joue = True
                        nbAllumettes = 12
                        player1.gagne = False
                        player2.gagne = False
                        player1.stupid = 0
                        player2.stupid = 0
                        liste_images = []
                        for i in range(nbAllumettes):
                            pif = random.randint(1,7)    
                            if pif == 1:
                                bien = conk
                            elif pif == 2:
                                bien = bepis
                            elif pif == 3:
                                bien = corn
                            elif pif == 4:
                                bien = mone
                            elif pif == 5:
                                bien = nft
                            elif pif == 6:
                                bien = dogecoin
                            elif pif == 7:
                                bien = plush
                            liste_images.append(bien)
                        
                    if nonrect.collidepoint(event.pos) :
                        #running = False
                        menu = True
                        
                        liste_images = []
                        for i in range(nbAllumettes):
                            pif = random.randint(1,7)    
                            if pif == 1:
                                bien = conk
                            elif pif == 2:
                                bien = bepis
                            elif pif == 3:
                                bien = corn
                            elif pif == 4:
                                bien = mone
                            elif pif == 5:
                                bien = nft
                            elif pif == 6:
                                bien = dogecoin
                            elif pif == 7:
                                bien = plush
                            liste_images.append(bien)



        if nbAllumettes == 1 and player1.joue == True :

            fin = True
            player2.gagne = True
            # render text
            player2.joue = None
            player1.joue = None
            augmente_score = True
            
        if nbAllumettes == 1 and player2.joue == True :

            fin = True
            player1.gagne = True
            # render text
            player2.joue = None
            player1.joue = None
            augmente_score = True
            
            
        if fin == True :
            if player1.gagne :
                gagne = myfont.render("Le gagnant est ", 1, (158,236,0))
                label = myfont.render(player1.nom[player1.select], 1, (158,236,0))
                if augmente_score == True :
                    player1.score+=1
                    augmente_score = False
                    player1.kalm = 1
                    player2.kalm = 2
                    
            else :
                gagne = myfont.render("Le gagnant est ", 1, (236,158,0))
                label = myfont.render(player2.nom[player2.select], 1, (236,158,0))
                if augmente_score == True :
                    player2.score+=1
                    augmente_score = False
                    player1.kalm = 2
                    player2.kalm = 1
                    
            question = myfont.render("Voulez-vous rejouer ?",1,(255,255,255))
            
            
            screen.blit(gagne, (450, 40))
            screen.blit(label, (450, 70))
            screen.blit(question,(420,400))
            screen.blit(oui,(530,450))
            screen.blit(non,(600,450))
            
            
            
    if humainVSordi == True :
           
        screen.blit(r_back,(0,0))
        if player1.joue == True:
            labelJ = myfont.render(player1.nom[player1.select]+" joue", 1, (158,236,0))
            screen.blit(labelJ, (450, 40))
        if player2.joue == True:
            labelJ2 = myfont.render(player2.nom[player2.select]+" joue", 1, (236,158,0))
            screen.blit(labelJ2, (450, 40))
        #affichage des allumettes :
        for i in range( nbAllumettes) :
            image = liste_images[i]
            
            screen.blit(image,(i*100,200))
        
        if player1.stupid == 0:
            screen.blit(player1.cosmetic[player1.select][player1.kalm],(10,311))
        else:
            screen.blit(player1.brainlet[player1.hazard],(10,311))
            
        image = pygame.transform.flip(player2.cosmetic[player2.select][player2.kalm], True, False)
        if player2.stupid == 0:
            screen.blit(image,(1050,311))
        else:
            image = pygame.transform.flip(player2.brainlet[player2.hazard], True, False)
            screen.blit(image,(1050,311))            
        

        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                
           
           # gestion de la souris
            elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                if event.button == 1: # 1= clique gauche
                    if zone1rect.collidepoint(event.pos) and player1.joue == True:

                        if nbAllumettes>=2 :
                        
                            player1.joue = False
                            player2.joue = True
                        
                            if nbAllumettes < 5 and nbAllumettes -1 != 1:
                                player1.stupid = 1
                        
                            nbAllumettes -=1

                    if zone2rect.collidepoint(event.pos) and player1.joue == True :

                        if nbAllumettes>=3 :
                            player1.joue = False
                            player2.joue = True
                            if nbAllumettes < 5 and nbAllumettes -2 != 1:
                                player1.stupid = 1
                        
                            nbAllumettes -=2
                            
                    if zone3rect.collidepoint(event.pos) and player1.joue == True :

                        if nbAllumettes>=4 :
                            nbAllumettes -=3
                            player1.joue = False
                            player2.joue = True
                    #il n'y a plus que les trois boutons du joueur humain
                    if ouirect.collidepoint(event.pos) :
                        fin = False
                        n = random.randint(1,2)
                        if n == 1 :
                            player1.joue = True
                        else :
                            player2.joue = True
                        nbAllumettes = 12
                        player1.gagne = False
                        player2.gagne = False
                        
                        player1.stupid = 0
                        player2.stupid = 0
                        
                        liste_images = []
                        for i in range(nbAllumettes):
                            pif = random.randint(1,7)    
                            if pif == 1:
                                bien = conk
                            elif pif == 2:
                                bien = bepis
                            elif pif == 3:
                                bien = corn
                            elif pif == 4:
                                bien = mone
                            elif pif == 5:
                                bien = nft
                            elif pif == 6:
                                bien = dogecoin
                            elif pif == 7:
                                bien = plush
                            liste_images.append(bien)

                        
                    if nonrect.collidepoint(event.pos) :
                        menu = True
                        liste_images = []
                        for i in range(nbAllumettes):
                            pif = random.randint(1,7)    
                            if pif == 1:
                                bien = conk
                            elif pif == 2:
                                bien = bepis
                            elif pif == 3:
                                bien = corn
                            elif pif == 4:
                                bien = mone
                            elif pif == 5:
                                bien = nft
                            elif pif == 6:
                                bien = dogecoin
                            elif pif == 7:
                                bien = plush
                            liste_images.append(bien)


        
        
        
        #l'ordi choisi son coup :
        if player2.joue == True and nbAllumettes >1 :
            compt += 0.1
            if compt > 50:
                compt = 0
            
                #à compléter Partie B question 3) le player2 ordi doit choisir son coups grâce au graphe G des coups
                #il doit choisir au hasard parmi la liste des arcs issus du sommet correspondant au nb d'allumettes
            
                u = random.randint(1,3)
                if nbAllumettes < 5:
                    nbAllumettes -= nbAllumettes -1
                    player2.joue = False
                    player1.joue = True
                
                else:
                    if u==1:

                        nbAllumettes -=1
                        player2.joue = False
                        player1.joue = True
                        
                        player1.kalm = 0

                            
                    if u == 2:

                        nbAllumettes -=2
                        player2.joue = False
                        player1.joue = True
                        
                        player1.kalm = 0
                        player2.kalm = 0
                            
                    if u == 3:

                        nbAllumettes -=3
                        player2.joue = False
                        player1.joue = True
                        
                        player1.kalm = 2
                        player2.kalm = 1
            
            
            # à compléter partie C question 2) : gérer si la liste de coups issus du nbd'allumettes présente est vide (gobelet vide dans vidéo)

        if nbAllumettes == 1 and player1.joue == True :

            fin = True
            player2.gagne = True
            # render text
            player2.joue = None
            player1.joue = None
            augmente_score = True
            
        if nbAllumettes == 1 and player2.joue == True :

            fin = True
            player1.gagne = True
            # render text
            player2.joue = None
            player1.joue = None
            augmente_score = True
            
            
        if fin == True :
            if player1.gagne :
                gagne = myfont.render("Le gagnant est ", 1, (158,236,0))
                label = myfont.render(player1.nom[player1.select], 1, (158,236,0))
                if augmente_score == True :
                    player1.score+=1
                    augmente_score = False
                    player1.kalm = 1
                    player2.kalm = 2
                    
            else :
                gagne = myfont.render("Le gagnant est ", 1, (236,158,0))
                label = myfont.render(player2.nom[player2.select], 1, (236,158,0))
                if augmente_score == True :
                    player2.score+=1
                    augmente_score = False
                    player1.kalm = 2
                    player2.kalm = 1
                    
            question = myfont.render("Voulez-vous rejouer ?",1,(255,255,255))
            
            
            screen.blit(gagne, (450, 40))
            screen.blit(label, (450, 70))
            screen.blit(question,(420,400))
            screen.blit(oui,(530,450))
            screen.blit(non,(600,450))
    pygame.display.update() # pour ajouter tout changement à l'écran
pygame.quit()




#if player2.joue == True and nBallumettes >1:
 #   liste_voisins = G.liste_sommets_issus(nbAllumettes)
  #  nbAllumettes = random.choice (liste_voisins)
   # player2.joue = False