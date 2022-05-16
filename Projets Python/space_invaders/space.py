import pygame  # necessaire pour charger les images et les sons
import random

def update_display():
    global sensors
    global snd_left #You may want to load more files here
    #Read the sensors
    sensors = sensorVals()

    if sensors:
        if detect_something():
            snd_left.play()


class celestial():
    def __init__(self):
        self.image = pygame.image.load("sun1.png").convert_alpha()
        self.hig = -400
        self.vitesse = 0.2
        self.vit = 0.4
        self.pos = -400
        self.tat = 0
        self.img1 = pygame.image.load("sun1.png").convert_alpha()
        self.img2 = pygame.image.load("sun2.png").convert_alpha()
        self.img3 = pygame.image.load("sun3.png").convert_alpha()
        self.img4 = pygame.image.load("sun4.png").convert_alpha()
        self.img5 = pygame.image.load("sun5.png").convert_alpha()
    def move(self):
        self.pos += self.vit
        self.hig += self.vitesse
        if self.tat == 1:
            self.image = self.img1
        elif self.tat == 2:
            self.image = self.img2
        elif self.tat == 3:
            self.image = self.img3
        elif self.tat == 4:
            self.image = self.img4
        elif self.tat == 5:
            self.image = self.img5
        
        if self.hig > 700:
            self.tat = random.randint(1,5)
            self.vitesse = -0.2
        if self.hig < -400:
            self.tat = random.randint(1,5)
            self.vitesse = 0.2
            
        if self.pos > 1300:
            self.tat = random.randint(1,5)
            self.vit = -0.4
        if self.pos < -400:
            self.tat = random.randint(1,5)
            self.vit = 0.4


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.sens = ""
        self.image = pygame.image.load('vaisseau1.png').convert_alpha()
        self.position = 100
        self.haut = 50
        self.score = 0
        self.recharge = 0
        self.ammopool=[3,20,1,1000,1000]
    def deplacer_l(self):
        if self.test > -0.8 :
            self.test -= 0.005
        
    def deplacer_r(self):
        if self.test < 0.8 :
            self.test += 0.005
        
    def deplacer_u(self):
        if self.tast > -0.8 :
            self.tast -= 0.005
        #self.haut += self.tast
        
    def deplacer_d(self):
        if self.tast < 0.8 :
            self.tast += 0.005
        #self.haut += self.tast
        
    def tirer(self, fballes):
        self.test -= fballes.recul
        self.energie -= fballes.enrg
        global snd_left #remember to use global
        fballes.snd_left.play()
        self.recharge = -fballes.reload
    
    def deplacer_tt(self):
        self.position += self.test
        
        if self.energie < 124 and self.vie > 0:
            self.energie += 0.02
        if self.energie < 0:
            self.energie += 0.04
        if self.energie < -20:
            self.energie += 1
        
        
        self.haut += self.tast
        if self.position<0:
            self.test += 0.1
        if self.position>586:
            self.test += -0.1
        if self.haut<10:
            self.tast += 0.1
        if self.haut>650:
            self.tast += -0.1
            
            
        if self.recharge < 0:
            self.recharge += 0.01

class Ennemi():
    NbEnnemis = 4
    def __init__(self):
        self.image = pygame.image.load("invader1.png").convert_alpha()
        self.hauteur = random.randint(20,680)
        self.vitesse = 0.1
        self.depart = random.randint(450,950)
        
    def avancer(self):
        if self.hauteur <0:
            self.vitesse = 0.1
        elif self.hauteur > 700:
            self.vitesse = -0.1
        self.hauteur += self.vitesse

class rocher() : 
    nbroc = 4
    def __init__(self) :
        self.image = pygame.image.load('roc.png').convert_alpha()
        self.place = 620
        self.high = 286
        
        self.vitesse = random.randint(1,10)/30
        self.monte = random.randint(1,10)/30
        
        hep = random.randint(1,2)
        if hep == 1:
            self.vitesse = -self.vitesse
        hep = random.randint(1,2)
        if hep == 1:
            self.monte = -self.monte

    def move(self,joueur,joueur2):
        self.place += self.vitesse
        self.high += self.monte
        
        if self.high <0:
            self.monte = -self.monte
        if self.high > 700:
            self.monte = -self.monte
            self.high = 680
        
        if self.monte > 3:
            self.monte = 2
        elif self.monte < -3:
            self.monte = -2
        if self.vitesse > 3:
            self.vitesse = 2
        if self.vitesse < -3:
            self.vitesse = -2
            
        
        if self.place <0:
            self.vitesse = -self.vitesse
        if self.place > 1260:
            self.vitesse = -self.vitesse
            
        if -16< self.high - joueur.haut < 48:
            if -40< self.place - joueur.position < 40: #or self.depart - ennemi.depart < -10:
                joueur.test = self.vitesse/1.2
                joueur.tast = self.monte/1.2
                self.vitesse = -self.vitesse*1.1
                self.monte = -self.monte*1.1
                joueur.energie-= 15
        
        if -16< self.high - joueur2.haut < 48:
            if -40< self.place - joueur2.position < 40: #or self.depart - ennemi.depart < -10:
                joueur2.test = self.vitesse/1.2
                joueur2.tast = self.monte/1.2
                self.vitesse = -self.vitesse*1.1
                self.monte = -self.monte*1.1
                joueur2.energie-= 15

            
            


class game_over():
    def __init__(self):
        self.image = pygame.image.load("fin.png").convert_alpha()
        self.hauteur = 1500
        self.depart = 1500
        
    def la_fin(self,joueur,joueur2):
        if joueur.vie < 0 or joueur2.vie < 0 :
            self.hauteur = 250
            self.depart = 520
            
            
            
class Joueur2() : 
    def __init__(self) :
        self.sens = ""
        self.image = pygame.image.load('vaisseau2.png').convert_alpha()
        self.position = 1136
        self.haut = 536
        self.score = 0
        self.recharge = 0
        self.ammopool=[3,20,1,1000,1000]
    def deplacer_l(self):
        if self.test > -0.8 :
            self.test -= 0.005
        
    def deplacer_r(self):
        if self.test < 0.8 :
            self.test += 0.005
        
    def deplacer_u(self):
        if self.tast > -0.8 :
            self.tast -= 0.005
        
    def deplacer_d(self):
        if self.tast < 0.8 :
            self.tast += 0.005
        #self.haut += self.tast
        
    def tirer(self, fballes2):
        self.test += fballes2.recul
        self.energie -= fballes2.enrg
        global snd_left #remember to use global
        fballes2.snd_left.play()
        self.recharge = -fballes2.reload
    
    def deplacer_tt(self):
        self.position += self.test
        
        if self.energie < 124 and self.vie > 0:
            self.energie += 0.02
        if self.energie < 0:
            self.energie += 0.04
        if self.energie < -20:
            self.energie += 1
        
        self.haut += self.tast
            
        if self.position>1236:
            self.test += -0.01
        if self.position<586:
            self.test += +0.01
        if self.haut<10:
            self.tast += 0.01
        if self.haut>640:
            self.tast += -0.01

        if self.recharge < 0:
            self.recharge += 0.01


class Balle2():
    def __init__(self,joueur2):
        self.joueur2 = joueur2
        self.etat = ""
        self.image = pygame.image.load("balle2.png").convert_alpha()
        self.depart = joueur2.position
        self.hauteur = joueur2.haut
    def bouger(self):
        if self.etat !='tireer':
            self.depart = self.joueur2.position
            self.hauteur = self.joueur2.haut+16
        else:
            if self.depart>0:
                self.depart -= 5
            else:
                self.etat=""
                self.depart=self.joueur2.position
                self.hauteur = self.joueur2.haut+16
    def toucher(self,ennemi, joueur):
        if -20< self.hauteur - ennemi.hauteur < 40:
            if -20< self.depart - ennemi.depart < 40: #or self.depart - ennemi.depart < -10:
                self.etat=""
                self.depart=self.joueur.position
                self.hauteur=self.joueur.haut+16
                ennemi.depart=1250
                self.joueur2.score += 1
                ennemi.vitesse += 0.04
                ennemi.hauteur = random.randint(50,600)
        
        if -16 < self.hauteur - joueur2.haut < 48:
            if -48< self.depart - joueur2.position < 48: #or self.depart - ennemi.depart < -10:
                self.etat=""
                self.depart=self.joueur.position
                self.hauteur=self.joueur.haut+16
                joueur.test-=1
                joueur.energie-=20
                self.joueur2.score += 0.5
                
                if joueur.energie < 15:
                    joueur.vie -= 20
                elif joueur.energie < 35:
                    joueur.vie -= 10
                elif joueur.energie < 75:
                    joueur.vie -= 5





class fballes(pygame.sprite.Sprite):
    def __init__(self,joueur):
        super().__init__()
        self.joueur = joueur
        self.etat = ""
        self.image = pygame.image.load("balle1.png").convert_alpha()
        self.depart = joueur.position
        self.hauteur = joueur.haut+16
        self.hat = 0
    
        if joueur.etat == 'canon':
            self.image = pygame.image.load("balle1.png").convert_alpha()
            self.atk_bc = 24
            self.atk_low = 30
            self.atk_med = 20
            self.atk_high = 15
            self.atk_full = 10
            self.enrg = 0
            self.speed = 4
            self.recul = 0.5
            self.recul_t = 1
            self.reload = 6
            self.ammo = 0
            self.snd_left = pygame.mixer.Sound('arty.ogg')
            
        if joueur.etat == 'mitraille':
            self.image = pygame.image.load("balle1.png").convert_alpha()
            self.atk_bc = 15
            self.atk_low = 10
            self.atk_med = 5
            self.atk_high = 0
            self.atk_full = 0
            self.enrg = 0
            self.speed = 6
            self.recul = 0.15
            self.recul_t = 0.10
            self.reload = 0
            self.ammo = 1
            self.snd_left = pygame.mixer.Sound('brrt.ogg')
    
        if joueur.etat == 'laser':
            self.image = pygame.image.load("laser1.png").convert_alpha()
            self.atk_bc = 10
            self.atk_low = 8
            self.atk_med = 5
            self.atk_high = 2
            self.atk_full = 0
            self.enrg = 4
            self.speed = 8
            self.recul = 0
            self.recul_t = 0.15
            self.reload = 0
            self.ammo = 4
            self.snd_left = pygame.mixer.Sound('laser.ogg')

        if joueur.etat == 'plasma':
            self.image = pygame.image.load("blaster1.png").convert_alpha()
            self.atk_bc = 40
            self.atk_low = 25
            self.atk_med = 20
            self.atk_high = 15
            self.atk_full = 15
            self.enrg = 20
            self.speed = 3
            self.recul = 0.05
            self.recul_t = 0.7
            self.reload = 2
            self.ammo = 5
            self.snd_left = pygame.mixer.Sound('plasma.ogg')

        if joueur.etat == 'torpille':
            self.image = pygame.image.load("torpille1.png").convert_alpha()
            self.atk_bc = 50
            self.atk_low = 70
            self.atk_med = 40
            self.atk_high = 30
            self.atk_full = 20
            self.enrg = 0
            self.speed = 0
            self.recul = 0
            self.recul_t = 1
            self.reload = 2.5
            self.ammo = 2
            self.snd_left = pygame.mixer.Sound('missile.ogg')

    
    def bouger(self):
        if self.depart<1300 or self.etat!='explosion':
            self.depart += self.speed
        else:
            self.etat="explosion"
        if self.etat=='explosion':
            self.depart = 1500
            self.hauteur = 1500
    
    
    def toucher(self,ennemi,joueur2,rocher):
        if -20< self.hauteur - ennemi.hauteur < 40:
            if -20< self.depart - ennemi.depart < 40: #or self.depart - ennemi.depart < -10:
                ennemi.depart= random.randint(450,950)
                self.joueur.score += 1
                
                deter = random.randint(1,2)
                
                if deter == 1:
                    ennemi.hauteur = 0 
                else:
                    ennemi.hauteur = 700
                self.etat="explosion"
                
                typeammo = random.randint(0,2)
                if typeammo == 0:
                    nb_ammo = 2
                elif typeammo == 1:
                    nb_ammo = 7
                else:
                    nb_ammo = 1
                self.joueur.ammopool[typeammo] += nb_ammo
                
                
                
        if self.joueur.etat=='torpille':
            self.speed += 0.0007
            if self.hauteur > joueur2.haut:
                self.hat -= 0.00015
                self.hauteur += self.hat
            elif self.hauteur < joueur2.haut:
                self.hat += 0.00015
                self.hauteur += self.hat
                
                

        if -16< self.hauteur - joueur2.haut < 48:
            if -40< self.depart - joueur2.position < 40: #or self.depart - ennemi.depart < -10:
                self.depart = 1500
                self.hauteur = 1500
                self.etat="explosion"
                joueur2.test+= self.recul_t
                joueur2.energie-= self.atk_bc
                self.joueur.score += 0.5
                
                if joueur2.energie < 15:
                    joueur2.vie -= self.atk_low
                elif joueur2.energie < 35:
                    joueur2.vie -= self.atk_med
                elif joueur2.energie < 75:
                    joueur2.vie -= self.atk_high
                else:
                    joueur2.vie -= self.atk_full
                    
        if -20< self.hauteur - rocher.high < 40:
            if -20< self.depart - rocher.place < 40:
                rocher.vitesse += self.recul_t/4
                self.etat="explosion"        
                


class fballes2(pygame.sprite.Sprite):
    def __init__(self,joueur2):
        super().__init__()
        self.joueur2 = joueur2
        self.etat = ""
        self.image = pygame.image.load("balle1.png").convert_alpha()
        self.depart = joueur2.position
        self.hauteur = joueur2.haut+16
        self.hat = 0
    
        if joueur2.etat == 'canon':
            self.image = pygame.image.load("balle1.png").convert_alpha()
            self.atk_bc = 24
            self.atk_low = 30
            self.atk_med = 20
            self.atk_high = 15
            self.atk_full = 10
            self.enrg = 0
            self.speed = 4
            self.recul = 0.5
            self.recul_t = 1
            self.reload = 6
            self.ammo = 0
            self.snd_left = pygame.mixer.Sound('arty.ogg')
            
        if joueur2.etat == 'mitraille':
            self.image = pygame.image.load("balle1.png").convert_alpha()
            self.atk_bc = 15
            self.atk_low = 10
            self.atk_med = 5
            self.atk_high = 0
            self.atk_full = 0
            self.enrg = 0
            self.speed = 6
            self.recul = 0.15
            self.recul_t = 0.10
            self.reload = 0
            self.ammo = 1
            self.snd_left = pygame.mixer.Sound('brrt.ogg')
    
        if joueur2.etat == 'laser':
            self.image = pygame.image.load("laser1.png").convert_alpha()
            self.atk_bc = 10
            self.atk_low = 8
            self.atk_med = 5
            self.atk_high = 2
            self.atk_full = 0
            self.enrg = 4
            self.speed = 8
            self.recul = 0
            self.recul_t = 0.15
            self.reload = 0
            self.ammo = 4
            self.snd_left = pygame.mixer.Sound('laser.ogg')

        if joueur2.etat == 'plasma':
            self.image = pygame.image.load("blaster1.png").convert_alpha()
            self.atk_bc = 40
            self.atk_low = 25
            self.atk_med = 20
            self.atk_high = 15
            self.atk_full = 15
            self.enrg = 20
            self.speed = 3
            self.recul = 0.05
            self.recul_t = 0.7
            self.reload = 2
            self.ammo = 5
            self.snd_left = pygame.mixer.Sound('plasma.ogg')

        if joueur2.etat == 'torpille':
            self.image = pygame.image.load("torpille1.png").convert_alpha()
            
            self.atk_bc = 50
            self.atk_low = 70
            self.atk_med = 40
            self.atk_high = 30
            self.atk_full = 20
            self.enrg = 0
            self.speed = 0
            self.recul = 0
            self.recul_t = 1
            self.reload = 2.5
            self.ammo = 2
            self.snd_left = pygame.mixer.Sound('missile.ogg')
        
    def bouger(self):
        if self.depart>0 or self.etat!='explosion':
            self.depart -= self.speed
        else:
            self.etat="explosion"
        if self.etat=='explosion':
            self.depart = 1500
            self.hauteur = 1500
    
    
    def toucher(self,ennemi,joueur,rocher):
        if -20< self.hauteur - ennemi.hauteur < 40:
            if -20< self.depart - ennemi.depart < 40: #or self.depart - ennemi.depart < -10:
                ennemi.depart= random.randint(450,950)
                self.joueur2.score += 1

                deter = random.randint(1,2)                
                if deter == 1:
                    ennemi.hauteur = 0 
                else:
                    ennemi.hauteur > 700

                
                self.etat="explosion"
                typeammo = random.randint(0,2)
                if typeammo == 0:
                    nb_ammo = 2
                elif typeammo == 1:
                    nb_ammo = 7
                else:
                    nb_ammo = 1
                self.joueur2.ammopool[typeammo] += nb_ammo
                
                
                
                
        if self.joueur2.etat=='torpille':
            self.speed += 0.0007
            if self.hauteur > joueur.haut:
                self.hat -= 0.00012
                self.hauteur += self.hat
            elif self.hauteur < joueur.haut:
                self.hat += 0.00012
                self.hauteur += self.hat
                
                

        if -16< self.hauteur - joueur.haut < 48:
            if -40< self.depart - joueur.position < 40: #or self.depart - ennemi.depart < -10:
                self.depart = 1500
                self.hauteur = 1500
                self.etat="explosion"
                joueur.test-= self.recul_t
                joueur.energie-= self.atk_bc
                self.joueur2.score += 0.5
                
                if joueur.energie < 15:
                    joueur.vie -= self.atk_low
                elif joueur.energie < 35:
                    joueur.vie -= self.atk_med
                elif joueur.energie < 75:
                    joueur.vie -= self.atk_high
                else:
                    joueur.vie -= self.atk_full
                    
        if -20< self.hauteur - rocher.high < 40:
            if -20< self.depart - rocher.place < 40:
                rocher.vitesse -= self.recul_t/4
                self.etat="explosion"        