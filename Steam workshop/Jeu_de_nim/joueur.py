
import pygame
class Joueur:
    def __init__(self):
        self.joue = False
        self.score = 0
        self.gagne = False
        self.etat = ""
        self.costume = 13
        self.select = 0
        self.stupid = 0
        self.hazard = 0
        amongus = [pygame.image.load('textures/amongus.png').convert_alpha(),pygame.image.load('textures/drip_mogus.png').convert_alpha(),pygame.image.load('textures/amongus.png').convert_alpha()]
        
        bogdanov = pygame.image.load('textures/bogdanov.png').convert_alpha()
        bogdanov = [bogdanov,bogdanov,bogdanov]
        
        chungus = [pygame.image.load('textures/chungus.png').convert_alpha(),pygame.image.load('textures/mega_chungus.png').convert_alpha(),pygame.image.load('textures/chungus.png').convert_alpha()]
        
        bob = [pygame.image.load('textures/spunch_bop_gangsta.png').convert_alpha(),pygame.image.load('textures/spunch_bop_gangsta.png').convert_alpha(),pygame.image.load('textures/spunch_bop.png').convert_alpha()]
        
        godzilla = [pygame.image.load('textures/gozilla.png').convert_alpha(),pygame.image.load('textures/gozilla_cash.png').convert_alpha(),pygame.image.load('textures/gozilla_no_cash.png').convert_alpha()]
        
        doge = [pygame.image.load('textures/doge.png').convert_alpha(), pygame.image.load('textures/muscle_doge.png').convert_alpha(),pygame.image.load('textures/angry_doge.png').convert_alpha()]
        
        gnome = [pygame.image.load('textures/gnome.png').convert_alpha(),pygame.image.load('textures/you_gnomed.png').convert_alpha(),pygame.image.load('textures/gnome.png').convert_alpha()]
        
        orang = pygame.image.load('textures/orang.png').convert_alpha()
        orang = [orang,orang,orang]
        
        stonks = [pygame.image.load('textures/stonks.png').convert_alpha(), pygame.image.load('textures/mega_stonks.png').convert_alpha(), pygame.image.load('textures/stinks.png').convert_alpha()]
        
        wojak = [pygame.image.load('textures/soy_wojak.png').convert_alpha(), pygame.image.load('textures/soy_wojak_smort.png').convert_alpha(), pygame.image.load('textures/soy_wojak_sad.png').convert_alpha()]
        
        walter = pygame.image.load('textures/walter.png').convert_alpha()
        walter = [walter,walter,walter]
        
        mega_stonks = [pygame.image.load('textures/mega_stonks.png').convert_alpha(), pygame.image.load('textures/mega_stonks.png').convert_alpha(), pygame.image.load('textures/stinks.png').convert_alpha()]
        
        giga_chad = pygame.image.load('textures/giga_chad.png').convert_alpha()
        giga_chad = [giga_chad,giga_chad,giga_chad]
        
        self.brainlet = [pygame.image.load('textures/brainlet1.png').convert_alpha(),pygame.image.load('textures/brainlet2.png').convert_alpha(),pygame.image.load('textures/brainlet3.png').convert_alpha(),pygame.image.load('textures/brainlet4.png').convert_alpha()]
        
        self.cosmetic = [stonks,orang,walter,gnome,bob,doge,wojak,amongus,chungus,godzilla,bogdanov,giga_chad,mega_stonks]
        self.cost = [0,1,1,1,2,2,2,3,3,3,3,5,5,0]
        self.nom = ["Meme man", "orang", "walter","gnome","Spunch Bop", "doge", "Soy wojak", "amogus", "Big Chungus", "Very cash money", "Bogdanov", "Giga Chad", "Mega Stonks"]
        self.kalm = 0

        self.bon = [True,False,False,False,False,False,False,False,False,False,False,False,False]
    def set_etat(self,etat):
        self.etat = etat
