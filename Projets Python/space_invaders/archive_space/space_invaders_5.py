import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((900,700))
pygame.display.set_caption("Space Invaders") 
# chargement de l'image de fond
fond = pygame.image.load('background.png')

# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)

# creation du joueur
player = space.Joueur()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"


############
player.test = 0
player.tast = 0
vaisseau.rap = 0
############

    

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

pressed = {}



while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))

    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN:  # si une touche a été tapée, le marque dans le dictionnaire pressed la touche enfoncer
            pressed[event.key] = True
        if event.type == pygame.KEYUP:
            pressed[event.key] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # espace pour tirer
                player.tirer()
                tir.etat="tiree"

    if pressed.get(pygame.K_RIGHT):  # Si le joueur veut aller a droite
        player.deplacer_r()
    if pressed.get(pygame.K_LEFT):  # Si le joueur veut aller a gauche
        player.deplacer_l()
    if pressed.get(pygame.K_UP):  # Si le joueur veut aller a gauche
        player.deplacer_u()
    if pressed.get(pygame.K_DOWN):  # Si le joueur veut aller a gauche
        player.deplacer_d()
        
    ### Actualisation de la scene ###
    # deplacement des objets
    player.deplacer_r()
    player.deplacer_l()
    player.deplacer_u()
    player.deplacer_d()
    player.deplacer_tt()
    tir.bouger()
    # dessins des objets
    screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur        


##########
    screen.blit(player.image,[player.position,player.haut]) # appel de la fonction qui dessine le vaisseau du joueur
##########
    
    for extra in listeEnnemis:
        extra.avancer()
        screen.blit(extra.image,[extra.depart, extra.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            player.marquer()
            print(f"Score = {player.score} points")
    pygame.display.update() # pour ajouter tout changement à l'écran
