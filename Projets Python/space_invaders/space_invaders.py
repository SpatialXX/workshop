import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((1300,700))

#screen = pygame.display.set_mode((650,250))

pygame.display.set_caption("Space Invaders")
# chargement de l'image de fond
fond = pygame.image.load('background.png').convert_alpha()

# creation des ennemis

celeste = space.celestial()


listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)

listeroc = []
for indice in range(space.rocher.nbroc):
    meteor = space.rocher()
    listeroc.append(meteor)
    
    

player = space.Joueur()
kak = 0
att = 0
ramage = pygame.image.load('ammopool.png').convert_alpha()
ramage2 = pygame.image.load('ammopool2.png').convert_alpha()
instru = pygame.image.load('ecran.png').convert_alpha()


listeBalles = []
listeBalles2 = []


player2 = space.Joueur2()
kok = 0
#tir2 = space.Balle2(player2)
#tir2.etat = "chargee"

player.test = 0
player.tast = 0
player.energie = 62
player.vie = 124

player2.test = 0
player2.tast = 0
player2.energie = 62
player2.vie = 124

vaisseau.rap = 0
fin = space.game_over()

haum1 = 0
haub1 = 0
haum2 = 0
haub2 = 0

posg1 = 0
posd1 = 0
posg2 = 0
posd2 = 0

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

pressed = {}




pygame.mixer.init()        



#soundObj = pygame.mixer.Sound('dooms.ogg')
#soundObj.play()
pygame.mixer.music.load('dooms.ogg')
pygame.mixer.music.play(-1, 0.0)

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            pygame.quit()
            sys.exit(0) # pour fermer correctement
       
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN:  # si une touche a été tapée, le marque dans le dictionnaire pressed la touche enfoncer
            pressed[event.key] = True
        if event.type == pygame.KEYUP:
            pressed[event.key] = False
            
        #TIR 2  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:  # espace pour tirer
                if player2.ammopool[kok] > 0:
                    if player2.recharge > 0 or player2.recharge == 0:
                        if player2.energie > 10 :
                            fake_ball2 = space.fballes2(player2)
                            listeBalles2.append(fake_ball2)
                            player2.tirer(fake_ball2)
                            player2.ammopool[kok] -=1
                            
        #TIR
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:  # espace pour tirer
                if player.ammopool[kak] > 0:
                    if player.recharge > 0 or player.recharge == 0:
                        if player.energie > 10 :
                            fake_ball = space.fballes(player)
                            listeBalles.append(fake_ball)
                            player.tirer(fake_ball)
                            player.ammopool[kak] -=1
                        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if kak < 4:
                    kak += 1
                else:
                    kak = 0
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                
                if kok < 4:
                    kok += 1
                else:
                    kok = 0

                    
#    if pressed.get(pygame.K_SPACE):  # Si le joueur veut aller a droite
 #       player.deplacer_r()
        
    if kak == 0:
        player.etat="canon"
    elif kak == 1:
        player.etat="mitraille"
    elif kak == 2:
        player.etat="torpille"
    elif kak == 3:
        player.etat="laser"
    elif kak == 4:
        player.etat="plasma"

    if kok == 0:
        player2.etat="canon"
    elif kok == 1:
        player2.etat="mitraille"
    elif kok == 2:
        player2.etat="torpille"
    elif kok == 3:
        player2.etat="laser"
    elif kok == 4:
        player2.etat="plasma"

    
    if pressed.get(pygame.K_d) and player.energie > 0:  # Si le joueur veut aller a droite
        player.deplacer_r()
    if pressed.get(pygame.K_q)and player.energie > 0:  # Si le joueur veut aller a gauche
        player.deplacer_l()
    if pressed.get(pygame.K_z)and player.energie > 0:  # Si le joueur veut aller a gauche
        player.deplacer_u()
    if pressed.get(pygame.K_s) and player.energie > 0 and player.vie > 0:  # Si le joueur veut aller a gauche
        player.deplacer_d()
        
                      
    if pressed.get(pygame.K_m) and player2.energie > 0 and player2.vie > 0:  # Si le joueur veut aller a droite
        player2.deplacer_r()
    if pressed.get(pygame.K_k) and player2.energie > 0 and player2.vie > 0:  # Si le joueur veut aller a gauche
        player2.deplacer_l()
    if pressed.get(pygame.K_o) and player2.energie > 0 and player2.vie > 0:  # Si le joueur veut aller a gauche
        player2.deplacer_u()
    if pressed.get(pygame.K_l) and player2.energie > 0 and player2.vie > 0:  # Si le joueur veut aller a gauche
        player2.deplacer_d()

        
    ### Actualisation de la scene ###
    # deplacement des objets
    player.deplacer_r()
    player.deplacer_l()
    player.deplacer_u()
    player.deplacer_d()
    player.deplacer_tt()
    
    player2.deplacer_r()
    player2.deplacer_l()
    player2.deplacer_u()
    player2.deplacer_d()
    player2.deplacer_tt()
    
    celeste.move()
    screen.blit(celeste.image,[celeste.pos,celeste.hig])
    
    
    
    
    # dessins des objets
    screen.blit(fin.image,[fin.depart,fin.hauteur])
    
    
    #screen.blit(tir.image,[tir.depart,tir.hauteur]) # BALLE
    screen.blit(player.image,[player.position,player.haut]) # VAISSEAU
    
    #screen.blit(tir2.image,[tir2.depart,tir2.hauteur]) # BALLE
    screen.blit(player2.image,[player2.position,player2.haut]) # VAISSEAU
    
    screen.blit(ramage,[10,580])
    screen.blit(ramage2,[1241,10])
    if att == 0:
        screen.blit(instru,[300,0])
    #else:
    if pressed.get(pygame.K_SPACE):
        att = 1
##########
    
    #fin.la_fin()
    
    for extra in listeEnnemis:
        if att == 1:
            extra.avancer()
            screen.blit(extra.image,[extra.depart, extra.hauteur])

    for insta in listeroc:
        if att == 1:
            insta.move(player,player2)
            screen.blit(insta.image,[insta.place, insta.high])

    
    for yep in listeBalles:
        yep.bouger()
        screen.blit(yep.image,[yep.depart, yep.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
        
    for yup in listeBalles2:
        yup.bouger()
        flipped_surface = pygame.transform.flip(yup.image, True, False)
        screen.blit(flipped_surface,[yup.depart, yup.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    
    for ennemi in listeEnnemis:
        for insta in listeroc:
            for yep in listeBalles:
                if yep.toucher(ennemi,player2,insta):
                    ennemi.disparaitre()
        
            for yup in listeBalles2:
                if yup.toucher(ennemi,player,insta):
                    ennemi.disparaitre()
        
            
#        if tir.toucher(ennemi,player2):
 #           ennemi.disparaitre()
  #          player.marquer()
   #         print(f"Score = {player.score} points")
        if fin.la_fin(player,player2):
            running = False 
            sys.exit(0)
            
    
    black = pygame.color.Color('#000000')
    rouge = pygame.color.Color('#fc1300')
    vert = pygame.color.Color('#b3fc00')
    bleu_ciel = pygame.color.Color('#68d2d4')
    
    if player.energie < 15:
        bleu = pygame.color.Color('#fc1300')
    elif player.energie < 35:
        bleu = pygame.color.Color('#fca400')
    elif player.energie < 70:
        bleu = pygame.color.Color('#b3fc00')
    else:
        bleu = pygame.color.Color('#68d2d4')

    if player2.energie < 15:
        bleu2 = pygame.color.Color('#fc1300')
    elif player2.energie < 35:
        bleu2 = pygame.color.Color('#fca400')
    elif player2.energie < 70:
        bleu2 = pygame.color.Color('#b3fc00')
    else:
        bleu2 = pygame.color.Color('#68d2d4')

    
    pygame.draw.rect(screen, black, [player.position-32,player.haut+70, 124, 20]) 
    pygame.draw.rect(screen, bleu, [player.position-32,player.haut+72, player.energie, 15]) 
    
    pygame.draw.rect(screen, black, [player2.position-32,player2.haut+70, 124, 20]) 
    pygame.draw.rect(screen, bleu2, [player2.position-32,player2.haut+72, player2.energie, 15]) 
    
    
    pygame.draw.rect(screen, rouge, [player.position-32,player.haut+95, player.vie, 10])     
    pygame.draw.rect(screen, rouge, [player2.position-32,player2.haut+95, player2.vie, 10]) 
    
    if player.tast < 0:
        haub1 = -player.tast * 50
        haum1 = 0
    else:
        haum1 = player.tast * 50
        haub1 = 0
    pygame.draw.rect(screen, bleu_ciel, [player.position-16,player.haut+32, 10, haum1])     
    pygame.draw.rect(screen, bleu_ciel, [player.position-16,player.haut, 10, haub1])     
    
    if player2.tast < 0:
        haub2 = -player2.tast * 50
        haum2 = 0
    else:
        haum2 = player2.tast * 50
        haub2 = 0
    pygame.draw.rect(screen, bleu_ciel, [player2.position+80,player2.haut+32, 10, haum2])     
    pygame.draw.rect(screen, bleu_ciel, [player2.position+80,player2.haut, 10, haub2])     
    

    if player.test < 0:
        posd1 = -player.test * 50
        posg1 = 0
    else:
        posg1 = player.test * 50
        posd1 = 0
    pygame.draw.rect(screen, bleu_ciel, [player.position,player.haut-16, posg1, 10])     
    pygame.draw.rect(screen, bleu_ciel, [player.position+32,player.haut-16, posd1, 10])     
    
    if player2.test < 0:
        posd2 = -player2.test * 50
        posg2 = 0
    else:
        posg2 = player2.test * 50
        posd2 = 0
    pygame.draw.rect(screen, bleu_ciel, [player2.position+32,player2.haut-16, posg2, 10])     
    pygame.draw.rect(screen, bleu_ciel, [player2.position,player2.haut-16, posd2, 10])         

    pygame.draw.rect(screen, rouge, [player.position-32,player.haut+64, -player.recharge*20, 3])     
    pygame.draw.rect(screen, rouge, [player2.position-32,player2.haut+64, -player2.recharge*20, 3])     
    
    
    pygame.draw.rect(screen, rouge, [50,580, player.ammopool[0]*10, 16])
    pygame.draw.rect(screen, rouge, [50,596, player.ammopool[1]*2, 16])     
    pygame.draw.rect(screen, rouge, [50,612, player.ammopool[2]*10, 16])     
    
    pygame.draw.rect(screen, rouge, [1000,10, player2.ammopool[0]*10, 16])
    pygame.draw.rect(screen, rouge, [1000,26, player2.ammopool[1]*2, 16])     
    pygame.draw.rect(screen, rouge, [1000,42, player2.ammopool[2]*10, 16])
    
    pygame.display.flip()   
    pygame.display.update() # pour ajouter tout changement à l'écran
