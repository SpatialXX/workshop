import pygame
import random
import envir
import sys
from copy import copy

pygame.init() 

myfont = pygame.font.SysFont("century_school_book", 14)

#screen = pygame.display.set_mode((1300,715))
#screen = pygame.display.set_mode((650,250))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("Land ships")
fond = pygame.image.load('background.png').convert_alpha()


papier = pygame.image.load('gui_element/paper_note.png').convert_alpha()
gui = pygame.image.load('gui_element/main_gui.png').convert_alpha()

crawler_paper = pygame.image.load('gui_element/crawler_paper.png').convert_alpha()

elec = envir.electricity()
lumiere = envir.light()
temps = envir.temps()
crawler = envir.crawler()

team_rock = [envir.team_haut(0)]
humains = envir.list_humain()

carte = envir.lamap()
evenement = envir.event()
evenement.new_mail("event/explo_event_txt.txt",0)
cargo = envir.cargo()
moteur = envir.moteur(cargo)

air_objetr = envir.air_robjet()
air_objet = air_objetr.objet

fenetre_cliquer = -1
fnt_swap_click = 0
fnt_planning_click = 0
nomme_select = -1

class ouvre_carte:
    def __init__(self,carte,carte_generale) :
        with open(carte, "r") as fichier:
            self.listeCase = []
            num_ligne = 0
            for ligne in fichier:
                num_case = 0

                for sprite in ligne:

                    x = num_ligne * 200
                    y = num_case * 150

                    if num_case%2 != 1:
                        x += 100
                
                    num_case += 1
                    pos = [x,y]
                    pos_dp = [x,y]
                    case_ouvert = envir.case(pos,sprite,pos_dp)
                    self.listeCase.append(case_ouvert)
                num_ligne +=1


ouvrage_carte = ouvre_carte("terrain/pos_terrain.txt",carte)


player = envir.Joueur()


gauge_speed = envir.gauge_speed()
gauge_rpm = envir.gauge_rpm()
speed_order = envir.speed_order()
gouvernail = envir.gouvernail()
gauge_fuel_use = envir.gauge_fuel_use()
exploration = envir.exploration()
team_button = envir.team_button()

digit = 100000
x_ini = 404
liste_coord_x = []
for i in range (6):
    coord_x = envir.coord_x(digit,x_ini)
    digit = digit / 10
    x_ini += 6
    liste_coord_x.append(coord_x)
x_ini = 404
digit = 100000
liste_coord_y = []
for i in range (6):
    coord_y = envir.coord_y(digit,x_ini)
    digit = digit / 10
    x_ini += 6
    liste_coord_y.append(coord_y)


### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

pressed = {}


pygame.mixer.init()        

#pygame.mixer.music.load('dooms.ogg')
#pygame.mixer.music.play(-1, 0.0)




while running : # boucle infinie pour laisser la fenêtre ouverte

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

            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                crawler.place_gui += 30
            if event.key == pygame.K_LEFT:
                crawler.place_gui -= 30


        
            if event.key == pygame.K_z:
                if speed_order.ordre < 4:
                    speed_order.ordre += 1
                    
                    for i in range (len(coord_type_salles["moteur"])):
                        coord_type_salles["moteur"][i].nvl_cmd(speed_order.ordre)
                

        
            if event.key == pygame.K_s:
                if speed_order.ordre > -1:
                    speed_order.ordre -= 1

                    for i in range (len(coord_type_salles["moteur"])):
                        coord_type_salles["moteur"][i].nvl_cmd(speed_order.ordre)
                

        
            if event.key == pygame.K_q:
                carte.deplacer_l()
            
        
            if event.key == pygame.K_d:
                carte.deplacer_r()
                
                
        
            if event.key == pygame.K_e:
                if carte.vts_generale == 0:
                    bon = 1
                    for i in range (len(exploration.visite)):
                        if player.proche[0] == exploration.visite[i][0]:
                            if player.proche[1] == exploration.visite[i][1]:
                                bon = 0
                    if bon == 1:
                        exploration.explore(player,evenement)

        
        
            if event.key == pygame.K_UP:
                evenement.pos_depart[1] = evenement.pos_depart[1] -18
                
        
            if event.key == pygame.K_DOWN:
                evenement.pos_depart[1] = evenement.pos_depart[1] +18

        
            if event.key == pygame.K_i:
                if lumiere.etat == 'alume':
                    lumiere.etat = "etint"
                    elec.use -= 0.15
                else:
                    lumiere.etat = "alume"
                    elec.use += 0.15
        
            if event.key == pygame.K_t:
                t_tmp = envir.team_haut(len(team_rock))
                team_rock.append(t_tmp)
        
        
        
        if event.type == pygame.MOUSEBUTTONUP: 
            if event.button == 1: 
                
                if exploration.rect.collidepoint(event.pos):
                    if carte.vts_generale == 0:
                        bon = 1
                        for i in range (len(exploration.visite)):
                            if player.proche[0] == exploration.visite[i][0]:
                                if player.proche[1] == exploration.visite[i][1]:
                                    bon = 0
                        if bon == 1:
                            exploration.explore(player,evenement)
                    
                
                
                if team_button.rect.collidepoint(event.pos):
                    if team_button.clique == False:
                        team_button.clique = True
                                
                    else:
                        team_button.clique = False
                        nomme_select = -1
                        fenetre_cliquer = -1
                        
                        
                if team_button.clique == True : 
                    for azer in range(len(team_rock)):
                        if team_rock[azer].rect.collidepoint(event.pos):
                            if team_rock[azer].clique == False:
                                
                                if fnt_swap_click == 1:
                                    if nomme_select != -1:
                                        humains.humain[nomme_select].team = azer

                                else:
                                    fenetre_cliquer = azer
                                
                            else:
                                team_rock[azer].clique = False
                                fenetre_cliquer = -1
                                fnt_swap_click = 0
                                fnt_planning_click = 0
                            nomme_select = -1
                        
                    
                    if fenetre_cliquer != -1:
                        if team_button.rect_swap.collidepoint(event.pos):
                            if fnt_swap_click == 0:
                                fnt_swap_click = 1
                            else:
                                fnt_swap_click = 0
                                
                        if team_button.rect_planning.collidepoint(event.pos):
                            if fnt_planning_click == 0:
                                fnt_planning_click = 1
                                nomme_select = -1
                            else:
                                fnt_planning_click = 0    

                    

                    

                    for y in range(len(humains.humain)):
                        if humains.humain[y].team == fenetre_cliquer:
                            if humains.humain[y].homme_rect.collidepoint(event.pos):
                                if humains.humain[y].selected == True :
                                    nomme_select = -1
                                else:
                                    nomme_select = y
                                    fnt_planning_click = 0
                        
                                
                            

    ### Actualisation de la scene ###
    # deplacement des objets

    player.deplacer_tt(carte)

    
    
    #screen.blit(carte.image,[carte.pos,carte.hig])
    

    
    gauge_speed.avancer(carte)
    speed_order.ordre_actu()
    gouvernail.orientation(carte)
    gauge_fuel_use.avancer_alt(cargo)
    elec.avancer()
    
    
    for azer in range(len(team_rock)):                
        if fenetre_cliquer == azer:
            team_rock[azer].clique = True
        else:
            team_rock[azer].clique = False


    for combien in ouvrage_carte.listeCase:
        combien.actualiser(carte)
        if combien.pos[0] < 651 and combien.pos[0] > -202:
            if combien.pos[1] < 357 and combien.pos[1] > -202:
                screen.blit(combien.image,[combien.pos[0], combien.pos[1]])     #651    -202
        combien.proxi(player,carte,exploration)

    screen.blit(player.image,[player.position,player.haut])


    screen.blit(crawler_paper,[0,358])
    
    coord_type_salles = {"moteur":[],"repos":[],"stock":[],"demande":[],"repas":[]}
    
    for i in range (crawler.sources_tt.nb_ressources):
        crawler.stocks_tt[crawler.sources_tt.ressources[i]] = 0
    
    for wagon in range(crawler.nb_wagon):
        piece_tmp = crawler.constitution[wagon]
        #print (piece_tmp[wagon])
        enc_ok = 0
        for piece in piece_tmp:
            crawler.verifie(wagon,piece,enc_ok)
            screen.blit(crawler.image,[crawler.place_general,358])

            
            if enc_ok == 5:
                coord_type_salles[piece.categorie].append(piece)
                
                if piece.requete == True:
                    coord_type_salles["demande"].append(piece)
                    

            
            enc_ok += 1    
    rpm_tmp = 0
    for i in range (len(coord_type_salles["moteur"])):
        if coord_type_salles["moteur"][i].rendement_actu > 0:
           coord_type_salles["moteur"][i].rendement_actu += - coord_type_salles["moteur"][i].perte_inertie 
           rpm_tmp += coord_type_salles["moteur"][i].rendement_actu
    
    
    gauge_rpm.avancer(rpm_tmp)
    
    
    carte.move()
    cargo.consomation(moteur,elec)
    
    carte.vts_relative = rpm_tmp / 15000
    
    cargo.calcul_poid()
    
    
           
    
    black = pygame.color.Color('#000000')
    gris_clair = pygame.color.Color('#e5e8e8')
 
    pygame.draw.rect(screen, black, [447,306, 42, 20])
    
    fuel_restant = cargo.fuel / cargo.fuel_capacity
    fuel_restant = fuel_restant * 20
    fuel_vide = 20
    fuel_vide = fuel_vide - fuel_restant
    
    pygame.draw.rect(screen, gris_clair, [447,306, 42, fuel_vide])

    screen.blit(papier,[788,503]) #PAPIER
    for l in evenement.lettre_total:
        l.actualiser(evenement.pos_depart[1])
        screen.blit(l.image,[l.pos_x, l.pos_y])
        


    screen.blit(gui,(0,0))
    

    screen.blit(gauge_speed.image,[gauge_speed.pos[0], gauge_speed.pos[1]])
    screen.blit(gauge_rpm.image,[gauge_rpm.pos[0], gauge_rpm.pos[1]])
    screen.blit(speed_order.image,[speed_order.pos[0], speed_order.pos[1]])
    screen.blit(gouvernail.image,[gouvernail.pos[0], gouvernail.pos[1]])
    screen.blit(gauge_fuel_use.image,[gauge_fuel_use.pos[0], gauge_fuel_use.pos[1]])
    
    screen.blit(elec.image[0],[elec.pos[0], elec.pos[1]])
    screen.blit(elec.image[1],[elec.pos[2], elec.pos[1]])

    lumiere.actualiser(elec,temps)

    temps.seconde()
    
    
    quel = 4
    
    for i in range (4):
        pos_horloge = 738
        temps.def_image(quel)
        pos_horloge -= i * 22
        screen.blit(temps.img_irl[1],[pos_horloge, 706])
        pos_horloge -= 11
        screen.blit(temps.img_irl[0],[pos_horloge, 706])
        quel -= 1
        

    
    bon2 = 1
    for i in range (len(exploration.visite)):
        if player.proche[0] == exploration.visite[i][0]:
            if player.proche[1] == exploration.visite[i][1]:
                bon2 = 0
    if bon2 == 1 and carte.vts_generale == 0:
        screen.blit(exploration.image,[exploration.pos[0], exploration.pos[1]])
    else:
        screen.blit(exploration.image,[exploration.pos[2], exploration.pos[2]])
    
    coord_general_x = carte.pos - carte.pos - carte.pos
    for x in liste_coord_x:
        x.actualiser(coord_general_x)
        coord_general_x = x.general_apr
        screen.blit(x.image,[x.pos[0], x.pos[1]])
    
    coord_general_y = carte.hig - carte.hig - carte.hig
    for y in liste_coord_y:
        y.actualiser(coord_general_y)
        coord_general_y = y.general_apr
        screen.blit(y.image,[y.pos[0], y.pos[1]])


    for i in range(len(team_rock)):
        for y in range(len(humains.humain)):
            if humains.humain[y].team == i:
            
                pos_real = [humains.humain[y].pos[0]+crawler.place_gui, humains.humain[y].pos[1]]
                
                #screen.blit(humains.image,[pos_real[0], pos_real[1]])
                fat = 0
                if humains.humain[y].selected == True:
                    lcolor = [255,45,0]
                    fat = 1
                else:
                    lcolor = team_rock[i].color
                    
                pygame.draw.circle(screen, lcolor, [pos_real[0], pos_real[1]], 4+fat)
                
                humains.humain[y].ordre = team_rock[i].ordre[temps.heure[3]]
                
                if y == nomme_select:
                    humains.humain[y].selected = True
                else:
                    humains.humain[y].selected = False
                
                humains.humain[y].faim += humains.humain[y].calo_conso
                
                humains.humain[y].une_demande = len(coord_type_salles["demande"])
                humains.humain[y].direction()
                
                
                
                best_cmp=100000
                best_cmp2=0
                pos_att = [0,358+183]
                
                if humains.humain[y].place != humains.humain[y].direc: 
                    humains.humain[y].siege = -1
                    if humains.humain[y].direc == "stock" or humains.humain[y].direc == "demande":
                        for z1 in range(len(coord_type_salles["demande"])):
                            best_tmp =coord_type_salles["demande"][z1].priorite
                            
                            if best_cmp2 < best_tmp:
                                best_cmp2 = best_tmp
                                n_sal = z1
                        humains.humain[y].demander = coord_type_salles["demande"][n_sal].fuel
                        
                        salle_cherch = coord_type_salles["demande"][n_sal]
                        pos_att[0] = salle_cherch.place_general
                        
                        if humains.humain[y].direc == "stock":
                            for z2 in range(len(coord_type_salles["stock"])):
                                trully = False
                                
                                for z3 in range (len(coord_type_salles["stock"][z2].stockage)):
                                    if humains.humain[y].demander == coord_type_salles["stock"][z2].stockage[z3].quel_type:
                                        trully = True
                                
                                if trully == True:    
                                    best_tmp =coord_type_salles["stock"][z2].place_general - humains.humain[y].pos[0]
                                    best_tmp_cmp = abs(best_tmp)
                                    if best_tmp_cmp < best_cmp:
                                        best_cmp = best_tmp_cmp
                                        n_sal = z2
                                        salle_cherch = coord_type_salles["stock"][z2]
                                        pos_att[0] = salle_cherch.place_general
                                                                
                    else:
                        for z in range(len(coord_type_salles[humains.humain[y].direc])):
                            best_tmp =coord_type_salles[humains.humain[y].direc][z].place_general - humains.humain[y].pos[0]
                            best_tmp_cmp = abs(best_tmp)
                            if best_tmp_cmp < best_cmp:
                                best_cmp = best_tmp_cmp
                                #best = best_tmp
                                n_sal = z
                                salle_cherch = coord_type_salles[humains.humain[y].direc][z]
                                pos_att[0] = salle_cherch.place_general
                    
                    
                    if salle_cherch.fuel != humains.humain[y].main.quel_type and humains.humain[y].main.quel_type != "vide":
                        humains.humain[y].main = air_objet
                    
                    
                    #print("coord salles",coord_type_salles, "coord bonhomme",humains.humain[y].pos[0], "coord bonhomme + gui", pos_real[0],"best",best)
                    humains.humain[y].n_salle = n_sal
                    
                    
                    humains.bouge(pos_real,pos_att,y,16,26,0,3)

                    if humains.arrive == True:
                        humains.humain[y].place = humains.humain[y].direc
                    
                   

                else:
                    homme = humains.humain[y]
#                    if temps.heure[3] == 13:
 #                       print(homme.direc, homme.n_salle, len(coord_type_salles[homme.direc]), coord_type_salles[homme.direc][0].categorie)
                    salle = coord_type_salles[homme.direc][homme.n_salle]
                    
                    
                    if homme.direc == "moteur":
                        if salle.demande > salle.rendement_actu:
                            if homme.main.quel_type == "vide":
                                pos_att = salle.cord_stock
                                humains.bouge(pos_real,pos_att,y,0,2,0,2)
                                
                                if humains.arrive == True:
                                    
                                    for ze in range (len(salle.stockage)):
                                        if salle.stockage[ze].quel_type == salle.fuel:
                                            if homme.main.quel_type == "vide":
                                                homme.main = copy(salle.stockage[ze])
                                                homme.main.qqt = random.randint(2,homme.force)
                                                
                                                #homme.main.qqt = random.randint(2,homme.force)/homme.main.masse_m3
                                                if salle.stockage[ze].qqt > 0:
                                                    salle.stockage[ze].qqt += -homme.main.qqt
                                                    
                                                else:
                                                    salle.stockage[ze] = air_objet
                                    
                            if homme.main.quel_type == salle.fuel:
                                pos_att = salle.cord_conso
                                humains.bouge(pos_real,pos_att,y,0,2,0,2)
                                if humains.arrive == True:
                                    
                                    salle.rendement_actu += homme.main.chaufe * homme.main.qqt
                                    
                                    homme.main = air_objet
                    
                    if salle.categorie == "stock":
                        pos_att = salle.cord_stock
                        humains.bouge(pos_real,pos_att,y,0,2,0,2)
                        
                        if humains.arrive == True:
                            for ze in range (len(salle.stockage)):
                                if salle.stockage[ze].quel_type == homme.demander:
                                    homme.main = copy(salle.stockage[ze])
                                    homme.main.qqt = random.randint(2,homme.force)
                
                                    if salle.stockage[ze].qqt > 0:
                                        salle.stockage[ze].qqt += -homme.main.qqt    
                                    else:
                                        salle.stockage[ze] = air_objet
                    
                    if homme.direc == "demande":
                        pos_att = salle.cord_stock
                        humains.bouge(pos_real,pos_att,y,0,2,0,2)
                        
                        if humains.arrive == True:
                            
                            for ze in range (len(salle.stockage)):
                                if salle.stockage[ze].quoi == homme.main.quoi and homme.main.quel_type != "vide":
                                    salle.stockage[ze].qqt += homme.main.qqt
                                    homme.main = air_objet
                                elif salle.stockage[ze].quel_type == "vide" and homme.main.quel_type != "vide":
                                    salle.stockage = copy(humme.main)
                                    homme.main = air_objet
                                    

                    if homme.direc == "repas":
                        
                        if homme.main.quel_type == 'vide':
                            pos_att = salle.cord_stock
                            humains.bouge(pos_real,pos_att,y,0,2,0,2)
                        
                            if humains.arrive == True:
                            
                                for ze in range (len(salle.stockage)):
                                    if salle.stockage[ze].quel_type == "consommable":
                                        homme.main = copy(salle.stockage[ze])
                                        homme.main.qqt = random.randint(2,homme.force)
                                        
                                        if salle.stockage[ze].qqt > 0:
                                            salle.stockage[ze].qqt += -homme.main.qqt        
                                        else:
                                            salle.stockage[ze] = air_objet
                                        
                        else :
                            if homme.siege != -1:
                                pos_att = salle.cord_siege[homme.siege]
                                humains.bouge(pos_real,pos_att,y,0,2,0,2)
                                if humains.arrive == True:
                                    munch = -(random.randint(1,10)/10000)
                                    homme.main.qqt += munch
                                    homme.faim += munch * homme.main.nutrition
                                    print (munch, homme.faim)
                                    if homme.main.qqt < 0:
                                        homme.main = air_objet
                            else:
                                for ze in range (salle.siege):
                                    if homme.siege != 1:
                                        if salle.siege_p[ze] == False:
                                            homme.siege = ze
                                            salle.siege_p[ze] = True
                            
                        

                    homme.main.masse = (homme.main.masse_m3 * homme.main.qqt) / 1000
                    
                    homme.vitesse = homme.og_vitesse - (homme.main.masse / homme.force)/1.5
                    
                    if homme.vitesse < 0.3 :
                        homme.vitesse = 0.3

                    
                  
    screen.blit(team_button.image,[team_button.pos[0],team_button.pos[1]])            
        
    if team_button.clique == True:
        for i in range(len(team_rock)):
            screen.blit(team_button.image2,[team_rock[i].rect[0],team_rock[i].rect[1]])
            
            
            
            nom_team = myfont.render(team_rock[i].nom, 1, team_rock[i].color)
            screen.blit(nom_team, (495, team_button.pos[1]+6+29*i))
            z = 0
            
            if team_rock[i].clique == True:
                
                screen.blit(team_button.image4[fnt_swap_click],[team_rock[i].rect[0]-55,358])
                screen.blit(team_button.image5[fnt_planning_click],[team_rock[i].rect[0]-115,358])
                
                for y in range(len(humains.humain)):
                    if humains.humain[y].team == i:
                        z += 1
                        
                        if humains.humain[y].selected == True:
                            image_tmp = team_button.image3[1]
                        else:
                            image_tmp = team_button.image3[0]
                            
                        screen.blit(image_tmp,[team_rock[i].rect[0]-115,358+29*z])
            
                        nom_bonhomme = myfont.render(humains.humain[y].nom[0], 1, team_rock[i].color)
                        screen.blit(nom_bonhomme, (team_rock[i].rect[0]-107, 358+6+29*z))
                        
                        humains.humain[y].homme_rect = pygame.Rect(team_rock[i].rect[0]-115,358+29*z,110,34)


                        carbon = myfont.render(str(crawler.stocks_tt["charbon"]), 1, team_rock[i].color)
                        screen.blit(carbon, (97, 358))
                
                if fnt_planning_click == 1:
                    for y in range (2):
                        for z in range(12):
                            screen.blit(team_button.image2,[team_rock[i].rect[0]-285+85*y,358+29*z])
                            
                            nom_temps = myfont.render(team_rock[i].ordre[z+12*y], 1, (220,220,220))
                            screen.blit(nom_temps, (team_rock[i].rect[0]+8-285+85*y,358+6+29*z))
                    
                    if temps.heure[3] < 13:
                        t = temps.heure[3]-1
                        tk = 0
                    else:
                        t = temps.heure[3] - 12-1
                        tk = 1
                    
                    screen.blit(team_button.image6,[team_rock[i].rect[0]-285+85*tk,358+10+29*t])
                        
    
    
    screen.blit(lumiere.image,[0, 0])
    
    
    pygame.display.flip()   
    pygame.display.update() # pour ajouter tout changement à l'écran
