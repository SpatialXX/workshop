import pygame  # necessaire pour charger les images et les sons
import random
import salles

def update_display():
    global sensors
    global snd_left #You may want to load more files here
    #Read the sensors
    sensors = sensorVals()

    if sensors:
        if detect_something():
            snd_left.play()


class lamap():
    def __init__(self):
        #self.image = pygame.image.load("maps.jpg").convert_alpha()
        self.hig = -1000
        self.pos = -1000

        self.vts_generale = 0
        self.vts_relative = 0

        self.direc = 2
        self.dificu = 1
    def deplacer_l(self):
        self.direc -= 1
   
    def deplacer_r(self):
        self.direc += 1

    def machine_ava(self):
        self.vts_relative += 0.05
        
    def machine_arr(self):
        self.vts_relative -= 0.05

        
        
        
    def move(self):
        self.vts_generale = self.vts_relative / self.dificu
    
        if self.direc == 0:
            self.hig += self.vts_generale
            
        elif self.direc == 1:
            self.pos -= self.vts_generale / 2
            self.hig += self.vts_generale / 2
            
        elif self.direc == 2:
            self.pos -= self.vts_generale

        elif self.direc == 3:
            self.pos -= self.vts_generale /2
            self.hig -= self.vts_generale / 2
            
        elif self.direc == 4:
            self.hig -= self.vts_generale

        elif self.direc == 5:
            self.pos += self.vts_generale /2
            self.hig -= self.vts_generale / 2

        elif self.direc == 6:
            self.pos += self.vts_generale
            
        elif self.direc == 7:
            self.pos += self.vts_generale /2
            self.hig += self.vts_generale / 2            
            

        elif self.direc == 8:
            self.direc = 0
            
        elif self.direc < 0:
            self.direc = 7
        


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.sens = ""

        self.position = 300
        self.haut = 118

    def deplacer_tt(self, lamap):
        
        if lamap.direc == 0:
            self.image = pygame.image.load('landship_monte.png').convert_alpha()
            
        elif lamap.direc == 1:
            self.image = pygame.image.load('landship_angle_haut.png').convert_alpha()
            
        elif lamap.direc == 2:
            self.image = pygame.image.load('landship_cote.png').convert_alpha()
            
        elif lamap.direc == 3:
            self.image = pygame.image.load('landship_angle_desc.png').convert_alpha()
            
        elif lamap.direc == 4:
            self.image = pygame.image.load('landship_desc.png').convert_alpha()
            
        elif lamap.direc == 5:
            self.image = pygame.image.load('landship_angle_desc.png').convert_alpha()            
            self.image = pygame.transform.flip(self.image, True, False)
            
        elif lamap.direc == 6:
            self.image = pygame.image.load('landship_cote.png').convert_alpha()            
            self.image = pygame.transform.flip(self.image, True, False)
            
        elif lamap.direc == 7:
            self.image = pygame.image.load('landship_angle_haut.png').convert_alpha()            
            self.image = pygame.transform.flip(self.image, True, False)
           


class case():
    def __init__(self,posi,sprite,pos_dp) :
        self.pos = posi
        self.pos_depart = pos_dp
        #self.image = pygame.image.load("invader1.png").convert_alpha()
        #self.hauteur = random.randint(20,680)
    
        case = "terrain/case.png"
    
        prairie = "terrain/prairie.png"
        foret = "terrain/foret.png"
        mer = "terrain/mer.png"
        coline = "terrain/colline.png"
        mont = "terrain/mont.png"
        sapin = "terrain/sapin.png"

        self.explore = random.randint(1,5)
        

        self.image = pygame.image.load(case).convert_alpha()
        self.dificu = 1
        self.desc = "erreur"
        
        spé = 0
        
        if sprite == '_':   
            self.image = pygame.image.load(prairie).convert_alpha()
            self.dificu = 1
            self.desc = "prairie"
            
            if self.explore < 3:
               self.explore = random.randint(1,5) 
               spé = 1
            
        elif sprite == 'f':   
            self.image = pygame.image.load(foret).convert_alpha()
            self.dificu = 1.25
            self.desc = "foret"
            
            if self.explore < 2:
               self.explore = random.randint(1,5)
               spé = 1
            
        elif sprite == 'm':   
            self.image = pygame.image.load(mer).convert_alpha()
            self.dificu = 5
            self.desc = "mer"
            
            if self.explore < 0:
               self.explore = random.randint(1,5)
               spé = 1
                    
        elif sprite == 'c':   
            self.image = pygame.image.load(coline).convert_alpha()
            self.dificu = 1.5
            self.desc = "coline"
            
            if self.explore < 4:
               self.explore = random.randint(1,5)
               spé = 1
            
                  
        elif sprite == '^':   
            self.image = pygame.image.load(mont).convert_alpha()
            self.dificu = 2
            self.desc = "montagne"
            
            if self.explore < 0:
               self.explore = random.randint(1,5)
               spé = 1

        elif sprite == 's':   
            self.image = pygame.image.load(sapin).convert_alpha()
            self.dificu = 1.25
            self.desc = "sapin"
            
            if self.explore < 2:
               self.explore = random.randint(1,5)
               spé = 1

        if spé == 0:
            self.explore = random.randint(1,20)

    def actualiser(self,carte):
        
        self.pos[0] = self.pos_depart[0] + carte.pos
        self.pos[1] = self.pos_depart[1] + carte.hig
            
  
    def proxi(self,player,carte,exploration):
        if -168 < self.pos[0] - player.position < 32:
            if -100 < self.pos[0] - player.position < -36:
                if -144 < self.pos[1] - player.haut < 7:
                    carte.dificu = self.dificu
                    
                    player.proche = self.pos_depart
                    
                    exploration.lequel = self.explore
                    
                    
            elif -125< self.pos[1] - player.haut < -12:
                carte.dificu = self.dificu
                player.proche = self.pos_depart
                exploration.lequel = self.explore
                
class gauge_speed():
    def __init__(self):
        self.image = pygame.image.load("gui_element/indicator.png").convert_alpha()
        self.pos_depart = [142,307]
        self.pos = [142,307]
        
    def avancer(self,carte):
        if carte.vts_generale < 0:
            pos_prevu = self.pos_depart[0] - carte.vts_generale * 450
        else:
            pos_prevu = self.pos_depart[0] + carte.vts_generale * 450
        

        if self.pos[0] - pos_prevu > 0.1 or self.pos[0] - pos_prevu < -0.1:
            if self.pos[0] > pos_prevu:
                self.pos[0] -= 0.08
            elif self.pos[0] != pos_prevu:
                if self.pos[0] < 233:
                    self.pos[0] += 0.08

class gauge_rpm():
    def __init__(self):
        self.image = pygame.image.load("gui_element/indicator.png").convert_alpha()
        self.pos_depart = [142,331]
        self.pos = [142,331]
        self.rpm = 0
        
    def avancer(self,rpm):
        self.rpm = rpm
        
        pos_prevu = self.pos_depart[0] + self.rpm * 0.01

        

        if self.pos[0] - pos_prevu > 0.2 or self.pos[0] - pos_prevu < -0.2:
            if self.pos[0] > pos_prevu:
                self.pos[0] -= 0.1
            elif self.pos[0] != pos_prevu:
                if self.pos[0] < 233:
                    self.pos[0] += 0.1

class speed_order():
    def __init__(self):
        self.back = pygame.image.load("gui_element/speed_back.png").convert_alpha()
        self.stop = pygame.image.load("gui_element/speed_stop.png").convert_alpha()
        self.one = pygame.image.load("gui_element/speed_1.png").convert_alpha()
        self.two = pygame.image.load("gui_element/speed_2.png").convert_alpha()
        self.three = pygame.image.load("gui_element/speed_3.png").convert_alpha()
        self.four = pygame.image.load("gui_element/speed_4.png").convert_alpha()
        
        self.pos = [43,333]
        self.ordre = 0
        
    def ordre_actu(self):
        if self.ordre < 0:
            self.image = self.back
        elif self.ordre == 0:
            self.image = self.stop
        elif self.ordre == 1:
            self.image = self.one
        elif self.ordre == 2:
            self.image = self.two
        elif self.ordre == 3:
            self.image = self.three
        if self.ordre > 3:
            self.image = self.four

class gouvernail():
    def __init__(self):
        self.n = pygame.image.load("gui_element/gouverne_n.png").convert_alpha()
        self.ne = pygame.image.load("gui_element/gouverne_ne.png").convert_alpha()
        self.e = pygame.image.load("gui_element/gouverne_e.png").convert_alpha()
        self.es = pygame.image.load("gui_element/gouverne_es.png").convert_alpha()
        self.s = pygame.image.load("gui_element/gouverne_s.png").convert_alpha()
        self.sw = pygame.image.load("gui_element/gouverne_sw.png").convert_alpha()
        self.w = pygame.image.load("gui_element/gouverne_w.png").convert_alpha()
        self.wn = pygame.image.load("gui_element/gouverne_wn.png").convert_alpha()
        
        self.pos = [262,293]
        
    def orientation(self,carte):
        if carte.direc == 0:
            self.image = self.n
            
        elif carte.direc == 1:
            self.image = self.ne
            
        elif carte.direc == 2:
            self.image = self.e
            
        elif carte.direc == 3:
            self.image = self.es
        
        elif carte.direc == 4:
            self.image = self.s
        
        elif carte.direc == 5:
            self.image = self.sw
            
        elif carte.direc == 6:
            self.image = self.w
        
        elif carte.direc == 7:
            self.image = self.wn

class coord_x():
    def __init__(self,digit,x_ini):
        self.pos = [x_ini,305]
        self.digitale = digit
        self.zero = pygame.image.load("letters/petit/0.png").convert_alpha()
        self.un = pygame.image.load("letters/petit/1.png").convert_alpha()
        self.deux = pygame.image.load("letters/petit/2.png").convert_alpha()
        self.trois = pygame.image.load("letters/petit/3.png").convert_alpha()
        self.quatre = pygame.image.load("letters/petit/4.png").convert_alpha()
        self.cinq = pygame.image.load("letters/petit/5.png").convert_alpha()
        self.six = pygame.image.load("letters/petit/6.png").convert_alpha()
        self.sept = pygame.image.load("letters/petit/7.png").convert_alpha()
        self.huit = pygame.image.load("letters/petit/8.png").convert_alpha()
        self.neuf = pygame.image.load("letters/petit/9.png").convert_alpha()
        
    def actualiser(self,general):
        compt = 0

        while general > self.digitale * compt:
            compt += 1


        if general < self.digitale * compt:
            compt += -1

        elif general == self.digitale * compt:
            compt = compt
        
        self.general_apr = general - self.digitale * compt
        
            
        if compt == 0:
            self.image = self.zero
        elif compt == 1:
            self.image = self.un
        elif compt == 2:
            self.image = self.deux
        elif compt == 3:
            self.image = self.trois
        elif compt == 4:
            self.image = self.quatre
        elif compt == 5:
            self.image = self.cinq
        elif compt == 6:
            self.image = self.six
        elif compt == 7:
            self.image = self.sept
        elif compt == 8:
            self.image = self.huit
        elif compt == 9:
            self.image = self.neuf        


class coord_y():
    def __init__(self,digit,x_ini):
        self.pos = [x_ini,319]
        self.digitale = digit
        self.zero = pygame.image.load("letters/petit/0.png").convert_alpha()
        self.un = pygame.image.load("letters/petit/1.png").convert_alpha()
        self.deux = pygame.image.load("letters/petit/2.png").convert_alpha()
        self.trois = pygame.image.load("letters/petit/3.png").convert_alpha()
        self.quatre = pygame.image.load("letters/petit/4.png").convert_alpha()
        self.cinq = pygame.image.load("letters/petit/5.png").convert_alpha()
        self.six = pygame.image.load("letters/petit/6.png").convert_alpha()
        self.sept = pygame.image.load("letters/petit/7.png").convert_alpha()
        self.huit = pygame.image.load("letters/petit/8.png").convert_alpha()
        self.neuf = pygame.image.load("letters/petit/9.png").convert_alpha()

    def actualiser(self,general):
        compt = 0

        while general > self.digitale * compt:
            compt += 1

        if general < self.digitale * compt:
            compt += -1

        elif general == self.digitale * compt:
            compt = compt
        
        self.general_apr = general - self.digitale * compt

        if compt == 0:
            self.image = self.zero
        elif compt == 1:
            self.image = self.un
        elif compt == 2:
            self.image = self.deux
        elif compt == 3:
            self.image = self.trois
        elif compt == 4:
            self.image = self.quatre
        elif compt == 5:
            self.image = self.cinq
        elif compt == 6:
            self.image = self.six
        elif compt == 7:
            self.image = self.sept
        elif compt == 8:
            self.image = self.huit
        elif compt == 9:
            self.image = self.neuf        

class moteur():
    def __init__(self,cargo):
        self.puissance_max = 20000 #20 000 chevaux
        self.conso_max = self.puissance_max / 100000 #20 000 / 100 000 = 0.2
        
        self.vitesse_max = 0.5  #était 0.05
        self.puissance = 0
        self.conso = 0

        
        

            

class gauge_fuel_use():
    def __init__(self):
        self.image = pygame.image.load("gui_element/indicator.png").convert_alpha()
        self.pos_depart = [393,335]
        self.pos = [393,335]

    def avancer_alt(self,cargo):
        if cargo.consomé < 0:
            pos_prevu = self.pos_depart[0] - cargo.consomé * 48
        else:
            pos_prevu = self.pos_depart[0] + cargo.consomé * 48
        

        if self.pos[0] - pos_prevu > 0.1 or self.pos[0] - pos_prevu < -0.1:
            if self.pos[0] > pos_prevu:
                if self.pos[0] < 484:
                    self.pos[0] -= 0.3
            elif self.pos[0] != pos_prevu:
                self.pos[0] += 0.3

class team_button():
    def __init__(self):
        self.image = pygame.image.load("gui_element/team_button.png").convert_alpha()
        self.image2 = pygame.image.load("gui_element/team_list.png").convert_alpha()
        self.image3 = [pygame.image.load("gui_element/team_list_big.png").convert_alpha(),pygame.image.load("gui_element/team_list_big_select.png").convert_alpha()]
        self.image4 = [pygame.image.load("gui_element/team_swap.png").convert_alpha(),pygame.image.load("gui_element/team_swap_select.png").convert_alpha()]
        self.image5 = [pygame.image.load("gui_element/team_planning.png").convert_alpha(),pygame.image.load("gui_element/team_planning_select.png").convert_alpha()]
        self.image6 = pygame.image.load("gui_element/indicator_heure.png").convert_alpha()
        self.pos = [575,358,-300]
        self.rect = pygame.Rect(self.pos[0],self.pos[1],76,68)
        
        self.rect_swap = pygame.Rect(490-55,358,60,34)
        self.rect_planning = pygame.Rect(490-115,358,60,34)
        self.clique = False

            
class cargo():
    def __init__(self):
        self.fuel_capacity = 10000 #10 000 L
        self.fuel = 10000 #10 000 L
        self.consomé = 0
        self.poid = 1 
        
    def calcul_poid(self):
        self.poid = 2000 #2T / 2 000 kg
        self.poid += 0.75 * self.fuel #1L = 0,75 kg     9 500 kg
        
        
    def consomation(self,moteur,elec):
        fuel_av = self.fuel
        self.consomé = self.fuel
        self.fuel += -moteur.conso
        moteur.vitesse_max = moteur.puissance_max / self.poid  #15 000 / 9 500 = /10 = 0.21
        moteur.vitesse_max = moteur.vitesse_max/10
        
        if elec.produit < elec.use:
            elec.produit += 0.001

        elif elec.produit > elec.use +0.01:
            elec.produit -= 0.001
        
        self.fuel += - elec.produit        
        
        self.consomé = self.fuel - fuel_av


class exploration():
    def __init__(self):
        self.image = pygame.image.load("gui_element/explore_button.png").convert_alpha()
        self.pos = [495,303,-300]
        self.visite = [[0,0]]
        self.lequel = 0
        
        self.rect = pygame.Rect(495,303,26,26)

    def explore(self,player,event):
        self.visite.append(player.proche)
        event.new_mail("event/explo_event_txt.txt",self.lequel)

        


class event():
    def __init__ (self):
        self.pos_depart = [800,681]
        self.lettre_total = []
        self.bonne_ligne = 0
        
        
        
        
    def new_mail (self,type_event,num_ligne_ext):
        self.num_ligne_ext = num_ligne_ext
        self.ecart_x = 0
        self.ecart_y = 0        
        pos_lettre = [800,681]        
        pos_lettre_next = 0
        
        with open(type_event, "r", encoding='utf-8') as fichier:
            
            num_ligne = 0
            #self.pos_depart[1] = self.pos_depart[1] -72
            for ligne in fichier:
                    
                if num_ligne == self.num_ligne_ext:
                    
                    
                    for sprite in ligne:
                        pos_lettre[0] += pos_lettre_next
                        pos_lettre_next = 0
#################################################################################################################
                        
                        
                        if sprite == ' ':   
                            image = pygame.image.load("letters/space.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 0
                        elif sprite == 'a':   
                            image = pygame.image.load("letters/a_low.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 0
                        elif sprite == 'b':   
                            image = pygame.image.load("letters/b_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 4

                        elif sprite == 'c':   
                            image = pygame.image.load("letters/c_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 0
                        elif sprite == 'd':   
                            image = pygame.image.load("letters/d_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 4

                        elif sprite == 'e':   
                            image = pygame.image.load("letters/e_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 0

                        elif sprite == 'f':   
                            image = pygame.image.load("letters/f_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 4

                        elif sprite == 'g':   
                            image = pygame.image.load("letters/g_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 0

                        elif sprite == 'h':   
                            image = pygame.image.load("letters/h_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 4

                        elif sprite == 'i':   
                            image = pygame.image.load("letters/i_low.png").convert_alpha()
                            self.ecart_x = 5
                            self.ecart_y = 5

                        elif sprite == 'j':   
                            image = pygame.image.load("letters/j_low.png").convert_alpha()
                            self.ecart_x = 5
                            self.ecart_y = 5

                        elif sprite == 'k':   
                            image = pygame.image.load("letters/k_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 4

                        elif sprite == 'l':   
                            image = pygame.image.load("letters/l_low.png").convert_alpha()
                            self.ecart_x = 5
                            self.ecart_y = 4

                        elif sprite == 'm':   
                            image = pygame.image.load("letters/m_low.png").convert_alpha()
                            self.ecart_x = 13
                            self.ecart_y = 0

                        elif sprite == 'n':   
                            image = pygame.image.load("letters/n_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 0

                        elif sprite == 'o':   
                            image = pygame.image.load("letters/o_low.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 0

                        elif sprite == 'p':   
                            image = pygame.image.load("letters/p_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 0

                        elif sprite == 'q':   
                            image = pygame.image.load("letters/q_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 0

                        elif sprite == 'r':   
                            image = pygame.image.load("letters/r_low.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 0

                        elif sprite == 's':   
                            image = pygame.image.load("letters/s_low.png").convert_alpha()
                            self.ecart_x = 6
                            self.ecart_y = 0

                        elif sprite == 't':   
                            image = pygame.image.load("letters/t_low.png").convert_alpha()
                            self.ecart_x = 4
                            self.ecart_y = 3

                        elif sprite == 'u':   
                            image = pygame.image.load("letters/u_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 0

                        elif sprite == 'v':   
                            image = pygame.image.load("letters/v_low.png").convert_alpha()
                            self.ecart_x = 9
                            self.ecart_y = 0

                        elif sprite == 'w':   
                            image = pygame.image.load("letters/w_low.png").convert_alpha()
                            self.ecart_x = 12
                            self.ecart_y = 0

                        elif sprite == 'x':   
                            image = pygame.image.load("letters/x_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 0

                        elif sprite == 'y':   
                            image = pygame.image.load("letters/y_low.png").convert_alpha()
                            self.ecart_x = 9
                            self.ecart_y = 0

                        elif sprite == 'z':   
                            image = pygame.image.load("letters/z_low.png").convert_alpha()
                            self.ecart_x = 6
                            self.ecart_y = 0


                        elif sprite == 'A':   
                            image = pygame.image.load("letters/a_up.png").convert_alpha()
                            self.ecart_x = 11
                            self.ecart_y = 4
                        elif sprite == 'B':   
                            image = pygame.image.load("letters/b_up.png").convert_alpha()
                            self.ecart_x = 12
                            self.ecart_y = 4

                        elif sprite == 'C':   
                            image = pygame.image.load("letters/c_up.png").convert_alpha()
                            self.ecart_x = 9
                            self.ecart_y = 4
                        elif sprite == 'D':   
                            image = pygame.image.load("letters/d_up.png").convert_alpha()
                            self.ecart_x = 11
                            self.ecart_y = 4

                        elif sprite == 'E':   
                            image = pygame.image.load("letters/e_up.png").convert_alpha()
                            self.ecart_x = 10
                            self.ecart_y = 4

                        elif sprite == 'F':   
                            image = pygame.image.load("letters/f_up.png").convert_alpha()
                            self.ecart_x = 10
                            self.ecart_y = 4

                        elif sprite == 'G':   
                            image = pygame.image.load("letters/g_up.png").convert_alpha()
                            self.ecart_x = 12
                            self.ecart_y = 4

                        elif sprite == 'H':   
                            image = pygame.image.load("letters/h_up.png").convert_alpha()
                            self.ecart_x = 13
                            self.ecart_y = 4

                        elif sprite == 'I':   
                            image = pygame.image.load("letters/i_up.png").convert_alpha()
                            self.ecart_x = 5
                            self.ecart_y = 4

                        elif sprite == 'J':   
                            image = pygame.image.load("letters/j_up.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 4

                        elif sprite == 'K':   
                            image = pygame.image.load("letters/k_up.png").convert_alpha()
                            self.ecart_x = 12
                            self.ecart_y = 4

                        elif sprite == 'L':   
                            image = pygame.image.load("letters/l_up.png").convert_alpha()
                            self.ecart_x = 10
                            self.ecart_y = 4

                        elif sprite == 'M':   
                            image = pygame.image.load("letters/m_up.png").convert_alpha()
                            self.ecart_x = 15
                            self.ecart_y = 4

                        elif sprite == 'N':   
                            image = pygame.image.load("letters/n_up.png").convert_alpha()
                            self.ecart_x = 13
                            self.ecart_y = 4

                        elif sprite == 'O':   
                            image = pygame.image.load("letters/o_up.png").convert_alpha()
                            self.ecart_x = 11
                            self.ecart_y = 4

                        elif sprite == 'P':   
                            image = pygame.image.load("letters/p_up.png").convert_alpha()
                            self.ecart_x = 10
                            self.ecart_y = 4

                        elif sprite == 'Q':   
                            image = pygame.image.load("letters/q_up.png").convert_alpha()
                            self.ecart_x = 11
                            self.ecart_y = 4

                        elif sprite == 'R':   
                            image = pygame.image.load("letters/r_up.png").convert_alpha()
                            self.ecart_x = 11
                            self.ecart_y = 4

                        elif sprite == 'S':   
                            image = pygame.image.load("letters/s_up.png").convert_alpha()
                            self.ecart_x = 9
                            self.ecart_y = 4

                        elif sprite == 'T':   
                            image = pygame.image.load("letters/t_up.png").convert_alpha()
                            self.ecart_x = 9
                            self.ecart_y = 4

                        elif sprite == 'U':   
                            image = pygame.image.load("letters/u_up.png").convert_alpha()
                            self.ecart_x = 13
                            self.ecart_y = 4

                        elif sprite == 'V':   
                            image = pygame.image.load("letters/v_up.png").convert_alpha()
                            self.ecart_x = 13
                            self.ecart_y = 4

                        elif sprite == 'W':   
                            image = pygame.image.load("letters/w_up.png").convert_alpha()
                            self.ecart_x = 13
                            self.ecart_y = 4

                        elif sprite == 'X':   
                            image = pygame.image.load("letters/x_up.png").convert_alpha()
                            self.ecart_x = 11
                            self.ecart_y = 4

                        elif sprite == 'Y':   
                            image = pygame.image.load("letters/y_up.png").convert_alpha()
                            self.ecart_x = 11
                            self.ecart_y = 4

                        elif sprite == 'Z':   
                            image = pygame.image.load("letters/z_up.png").convert_alpha()
                            self.ecart_x = 9
                            self.ecart_y = 4

                        elif sprite == '"':   
                            image = pygame.image.load("letters/parenthese.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4

                        elif sprite == '.':   
                            image = pygame.image.load("letters/point.png").convert_alpha()
                            self.ecart_x = 5
                            self.ecart_y = 0

                        elif sprite == '-':   
                            image = pygame.image.load("letters/tiret.png").convert_alpha()
                            self.ecart_x = 6
                            self.ecart_y = 0

                        elif sprite == ',':   
                            image = pygame.image.load("letters/virgule.png").convert_alpha()
                            self.ecart_x = 4
                            self.ecart_y = 0

                        elif sprite == "'":   
                            image = pygame.image.load("letters/apostrophe.png").convert_alpha()
                            self.ecart_x = 3
                            self.ecart_y = 4


                        elif sprite == '?':   
                            image = pygame.image.load("letters/interrogation.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 4

                        elif sprite == '!':   
                            image = pygame.image.load("letters/exclamation.png").convert_alpha()
                            self.ecart_x = 3
                            self.ecart_y = 4

                        elif sprite == 'é':   
                            image = pygame.image.load("letters/é_low.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 5

                        elif sprite == 'è':   
                            image = pygame.image.load("letters/è_low.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 5

                        elif sprite == 'à':   
                            image = pygame.image.load("letters/à_low.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 4

                        elif sprite == 'ë':   
                            image = pygame.image.load("letters/ë_low.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4

                        elif sprite == 'ê':   
                            image = pygame.image.load("letters/ê_low.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4

                        elif sprite == 'ç':   
                            image = pygame.image.load("letters/ç_low.png").convert_alpha()
                            self.ecart_x = 6
                            self.ecart_y = 0
                        
                        elif sprite == '🔽':   
                            image = pygame.image.load("letters/space.png").convert_alpha()
                            self.ecart_x = 0
                            self.ecart_y = 0                       
                            self.saut_ligne(pos_lettre)

                        elif sprite == '0':   
                            image = pygame.image.load("letters/0_zero.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4                        

                        elif sprite == '1':   
                            image = pygame.image.load("letters/1_un.png").convert_alpha()
                            self.ecart_x = 5
                            self.ecart_y = 4                        

                        elif sprite == '2':   
                            image = pygame.image.load("letters/2_deux.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4

                        elif sprite == '3':   
                            image = pygame.image.load("letters/3_trois.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4

                        elif sprite == '4':   
                            image = pygame.image.load("letters/4_quatre.png").convert_alpha()
                            self.ecart_x = 8
                            self.ecart_y = 4

                        elif sprite == '5':   
                            image = pygame.image.load("letters/5_cinq.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4

                        elif sprite == '6':   
                            image = pygame.image.load("letters/6_six.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4

                        elif sprite == '7':   
                            image = pygame.image.load("letters/7_sept.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4

                        elif sprite == '8':   
                            image = pygame.image.load("letters/8_huit.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4

                        elif sprite == '9':   
                            image = pygame.image.load("letters/9_neuf.png").convert_alpha()
                            self.ecart_x = 7
                            self.ecart_y = 4


                            
                        else:   
                            image = pygame.image.load("letters/space.png").convert_alpha()
                            self.ecart_x = 3
                            self.ecart_y = 0
#################################################################################################################

                        pos_lettre_next += self.ecart_x
                        
                        if pos_lettre[0] + self.ecart_x > 1148:
                            self.saut_ligne(pos_lettre)

                        pos_lettre[1] = self.bonne_ligne * 18
                        pos_lettre[1] += self.pos_depart[1] - self.ecart_y
                        #print(pos_lettre,self.ecart_x,pos_lettre_next)
                        
                        lettre_ouvre = lettre(pos_lettre[0],image,self.ecart_y,self.bonne_ligne)
                        self.lettre_total.append(lettre_ouvre)
                num_ligne += 1

        self.saut_ligne(pos_lettre)
        self.saut_ligne(pos_lettre)

        
    def saut_ligne(self,pos_lettre):
        self.bonne_ligne += 1
        pos_lettre[0] = self.pos_depart[0]
        self.pos_depart[1] = self.pos_depart[1] -18
        return pos_lettre
        
        
class lettre():
    def __init__ (self,pos_x,image_ext,ecart_y,bonne_ligne):
        self.pos_x = pos_x
        self.image = image_ext
        self.ligne = bonne_ligne
        self.ecart_y = ecart_y
    def actualiser (self,pos_depart):
        self.pos_y = self.ligne * 18
        self.pos_y += pos_depart - self.ecart_y


class light():
    def __init__ (self):
        self.lumiere =[pygame.image.load("letters/space.png").convert_alpha(),pygame.image.load("gui_element/no_light_day.png").convert_alpha(),pygame.image.load("gui_element/no_light_night.png").convert_alpha(),pygame.image.load("gui_element/light_alarm.png").convert_alpha()]
        self.etat = "alarme"
        print(self.etat)
        self.image = self.lumiere[2]
        self.alarm_blip = 0
    def actualiser (self,elec,temps):
                    
        if self.etat == 'alume':
            self.image = self.lumiere[0]
            if elec.produit < elec.use-0.01:
                self.etint(temps)
        else:
            self.etint(temps)

    def etint(self,temps):
        if temps.day == 'jour':
            self.image = self.lumiere[1]

        else:
            self.image = self.lumiere[2]

class temps():
    def __init__ (self):
        self.heure = [0,0,0,12,0,0]  #0 Année 1 Mois 2 Journée 3 Heure 4 Minute 5 Seconde
        self.day = "jour"
        self.image = [pygame.image.load("letters/0_zero.png").convert_alpha(),pygame.image.load("letters/1_un.png").convert_alpha(),pygame.image.load("letters/2_deux.png").convert_alpha(),pygame.image.load("letters/3_trois.png").convert_alpha(),pygame.image.load("letters/4_quatre.png").convert_alpha(),pygame.image.load("letters/5_cinq.png").convert_alpha(),pygame.image.load("letters/6_six.png").convert_alpha(),pygame.image.load("letters/7_sept.png").convert_alpha(),pygame.image.load("letters/8_huit.png").convert_alpha(),pygame.image.load("letters/9_neuf.png").convert_alpha()]
        self.img_irl = [self.image[0],self.image[0]]
    def seconde(self):
        self.heure[5] += 1
        if self.heure[5] == 30:
            self.heure[5] = 0
            self.heure[4] += 1
            
            
        if self.heure[4] ==60:
            self.heure[4] = 0
            self.heure[3] += 1
            
        if self.heure[3] == 24:
            self.heure[3] = 0
            self.heure[2] += 1
            print("nouvelle journée")
                
        if self.heure[2] == 31:
            self.heure[2] = 0
            self.heure[1] += 1

        if self.heure[1] == 12:
            self.heure[1] = 0
            self.heure[0] += 1

        if self.heure[3] >= 7 and self.heure[3] <= 17:
            self.day = "jour"
        else:
            self.day = "nuit"
            
    def def_image(self,quel):
        compte = self.heure[quel]
        i = 0
        while compte -i *10 >= 10:
            
            i += 1
        compte = compte - i * 10
        
        self.img_irl[0] = self.image[i]
        self.img_irl[1] = self.image[compte]


class electricity():
    def __init__ (self):
        self.use = 0
        self.produit = 0
        self.image = [pygame.image.load("gui_element/indicator.png").convert_alpha(),pygame.image.load("gui_element/indic_max.png").convert_alpha()]
        self.pos_depart = [497,335]
        self.pos = [497,335,497]
    def avancer(self):
        pos_prevu = [0,0]
        
        if self.produit < 0:
            pos_prevu[0] = self.pos_depart[0] - self.produit * 32
        else:
            pos_prevu[0] = self.pos_depart[0] + self.produit * 32
            
        if self.use < 0:
            pos_prevu[1] = self.pos_depart[0] - self.use * 32
        else:
            pos_prevu[1] = self.pos_depart[0] + self.use * 32
        

        if self.pos[0] - pos_prevu[0] > 0.1 or self.pos[0] - pos_prevu[0] < -0.1:
            if self.pos[0] > pos_prevu[0]:
                if self.pos[0] < 587:
                    self.pos[0] -= 0.05
            elif self.pos[0] != pos_prevu[0]:
                self.pos[0] += 0.05


        if self.pos[2] - pos_prevu[1] > 0.1 or self.pos[2] - pos_prevu[1] < -0.1:
            if self.pos[2] > pos_prevu[1]:
                if self.pos[2] < 587:
                    self.pos[2] -= 0.1
            elif self.pos[2] != pos_prevu[1]:
                self.pos[2] += 0.1


class crawler():
    def __init__(self):
        self.constitution = [[1,2,2,1,3,salles.moteur_charbon_1()],[0,1,0,0,0,salles.sale_stock()],[1,3,6,5,5,salles.sale_repos()],[1,3,6,5,5,salles.sale_repas_1()]]     #[chenniles(1oui 0non), type_salle(1pièce, 2pièce, 4pièce, 0aucune), ce qu'il y a dans la pièce] 
        self.nb_wagon = len(self.constitution)
        self.image_init_tracks = [pygame.image.load("blank.png").convert_alpha(),pygame.image.load("gui_element/crawler_management/main_tracks.png").convert_alpha()]
        self.place_gui = 0
        self.stocks_tt = {' ': 0}
        self.sources_tt = salles.sources_tt()
        
        print(self.image_init_tracks[1])
        
        self.image_init_wagon = [self.image_init_tracks[0],1,2,4]
        self.image_init_wagon[1]=pygame.image.load("gui_element/crawler_management/room_size1_full.png").convert_alpha() #1 One room
        self.image_init_wagon[2]=pygame.image.load("gui_element/crawler_management/room_size_1_div2.png").convert_alpha() #2 Two room
        self.image_init_wagon[3]=pygame.image.load("gui_element/crawler_management/room_size_1_div4.png").convert_alpha() #3 Three room

        self.image_init_salle = [self.image_init_tracks[0],1,2,3,4,5,6]     #0  empty
        self.image_init_salle[1] = self.image_init_salle[0]  #1  already taken
        self.image_init_salle[2] = pygame.image.load("gui_element/crawler_management/steam_engine.png").convert_alpha()          #2 steam engine
        self.image_init_salle[3] = pygame.image.load("gui_element/crawler_management/small_steam_engine.png").convert_alpha()    #3 small steam engine
        self.image_init_salle[4] = pygame.image.load("gui_element/crawler_management/alternator.png").convert_alpha()            #4 alternator
        self.image_init_salle[5] = pygame.image.load("gui_element/crawler_management/comms room.png").convert_alpha()          #5 Communication
        self.image_init_salle[6] = pygame.image.load("gui_element/crawler_management/captain_room.png").convert_alpha()          #6 Captain room


        
    def verifie(self,wagon,piece,enc_ok):
        self.place_general = self.place_gui + wagon * 186
        
        self.alenv = False
        
        if enc_ok == 0:
            self.image = self.image_init_tracks[piece]
        elif enc_ok == 1:
            self.image = self.image_init_wagon[piece]
        elif enc_ok == 2:
            self.image = self.image_init_salle[piece]
        elif enc_ok == 3:
            self.place_general += 93
            self.image = self.image_init_salle[piece]
        elif enc_ok == 4:
            self.image = self.image_init_salle[piece]
            flipped_surface = pygame.transform.flip(self.image, False, True)
            self.image = flipped_surface
        
#        else:
 #           self.place_general += 93
  #          self.image = self.image_init_salle[piece]
   #         flipped_surface = pygame.transform.flip(self.image, False, True)
    #        self.image = flipped_surface
    
        else:
            self.place_general += 93
            self.image = piece.image
            
            flipped_surface = pygame.transform.flip(self.image, False, True)
            
            if piece.taille ==2:
                flipped_surface = pygame.transform.flip(self.image, True, True)
            place = self.place_general
            
            self.image = flipped_surface
            
            alenv = True
            
            piece.ça_place(place,alenv)
            
            piece.priorite = piece.priorite_og
            
            requete_tmp = False
            for i in range(len(piece.stockage)):
                
                if piece.stockage[i].qqt < 900 and piece.stockage[i].quel_type == piece.fuel: #650
                    requete_tmp = True
                    
                    if piece.stockage[i].qqt < 350 and piece.priorite > 0:
                        piece.priorite += 3
                    
                elif piece.stockage[i].quel_type == "vide" and piece.fuel != "None":
                    if piece.priorite > 0:
                        piece.priorite += 5
                        requete_tmp = True
                self.stocks_tt[piece.stockage[i].quoi] += piece.stockage[i].qqt
            if requete_tmp == True:
                
                piece.requete = True
            else:
                piece.requete = False
                piece.priorite = piece.priorite_og
            
            


            
class list_humain():
    def __init__(self):
        trait = salles.Trait()
        self.image = pygame.image.load("gui_element/crawler_management/man.png").convert_alpha()
        
        creer_bonhomme = salles.bonhomme(trait,[21],2,150)
        self.humain = [creer_bonhomme]
        for i in range (5):
            creer_bonhomme = salles.bonhomme(trait,[],3,80)
            self.humain.append(creer_bonhomme)
    
    def bouge(self,pos_real,pos_att,num,x_min,x_max,y_min,y_max):
        self.arrive = False
        #print (pos_real,pos_att)
        if pos_real[1] - pos_att[1] < y_min:
            self.humain[num].pos[1]+= self.humain[num].vitesse
            #print("bas")
            
            self.humain[num].faim += (self.humain[num].main.masse / self.humain[num].force)/10
        
        elif pos_real[1] - pos_att[1] > y_max:
            self.humain[num].pos[1]-= self.humain[num].vitesse
            #print("haut")
            
            self.humain[num].faim += (self.humain[num].main.masse / self.humain[num].force)/10
            
        elif pos_real[0] - pos_att[0] < x_min:
            self.humain[num].pos[0]+= self.humain[num].vitesse
            #print("droite")
            
            self.humain[num].faim += (self.humain[num].main.masse / self.humain[num].force)/10

        elif pos_real[0] - pos_att[0] > x_max:
            self.humain[num].pos[0]-= self.humain[num].vitesse
            #print("gauche")
            
            self.humain[num].faim += (self.humain[num].main.masse / self.humain[num].force)/10
            
        
        else:
            self.arrive = True
            #print("k")


class team_haut():
    def __init__(self,nb_team):
        
        self.ordre_tt = ["aucun","moteur","transport","cuisine","construction","gestion","maintenance","communication","repos","repas","coucher"]
        self.ordre = ["aucun","moteur","moteur","moteur","moteur","moteur","moteur","moteur","moteur","moteur","moteur","moteur","moteur","transport","transport","transport","moteur","moteur","moteur","moteur","moteur","moteur","moteur","aucun"]
        self.nb_team = nb_team
        self.color = [255,255,255]
        
        self.nom = "Equipe n°"+str(nb_team)
        if nb_team != 0 :
            for i in range (3):
                couleur = random.randint(0,255)
                self.color[i-1] = couleur
        
        self.rect = pygame.Rect(490,358+29*nb_team,90,34)
        self.clique = False
        
        
class air_robjet():
    def __init__(self):
        self.objet = salles.air()