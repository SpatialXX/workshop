import pygame  # necessaire pour charger les images et les sons
import random

class sources_tt():
    def __init__(self):
        self.ressources = ["air","charbon","charbon de bois", "bois", "or", "nourriture crue","Nourriture cuisinée"]
        self.nb_ressources = len(self.ressources)

class moteur_charbon_1():
    def __init__(self):
        self.categorie = "moteur"
        self.requete = False
        self.fuel = "combustible"
        self.rendement = 0.08 #il faut 0.032 unité de fuel pour développer 1 chevaux
        self.beaute = -5 #si il est plaisant ou non de se tenir a côté de lui
        self.vie = 50
        self.pannes = 60 #en %  0 = jamais en panne    100 = Toujours en panne
        self.image = pygame.image.load("gui_element/crawler_management/small_steam_engine.png").convert_alpha()
        self.taille = 1
        self.rendement_max  = 2000    #nb cheveaux totaux max
        self.rendement_actu = 0
        self.events = "aucun"
        self.poid = 5000 # 5 000 kg ou 5t
        self.perte_inertie = 1.3 #nb de cheveaux le moteur perd
        self.demande = 0
        self.stockage = [charbon(),charbon()]
        self.priorite_og = 0
        
        self.contient = [[]]
        pos_contenu = [74,167+358]
        for j in range (3):
            self.contient[0].append([stockage(pos_contenu)])
            pos_contenu[0] += 12
        
        
    def ça_place(self,place_general,alenv):
        self.place_general = place_general
        self.alenv = alenv


        self.cord_conso = [place_general+42,142+358]
        self.cord_stock = [place_general+74,167+358]
        
        if self.alenv == True:
 
            tmp = (self.cord_conso[1] - 358) - 368
            tmp = tmp - tmp - tmp
            self.cord_conso[1] = tmp+358

            tmp = (self.cord_stock[1] - 358) - 368
            tmp = tmp - tmp - tmp
            self.cord_stock[1] = tmp+358
            #self.cord_stock[1] = 201+358
#            self.cord_conso[1] = 226+358
            

            
        for j in range(len(self.contient[0])):
            self.contient[0][0][0].pos = self.cord_stock
        

    def nvl_cmd(self,ordre):
        if ordre == 0:
            self.demande = 0
        else:
            self.demande = self.rendement_max/4
            self.demande = self.demande * ordre
        
        print(self.demande)
        
    def update (self):
        for i in range(len(self.contient[0])):
            pass

class sale_repos():
    def __init__(self):
        self.categorie = "repos"
        self.taille = 1
        self.fuel = "None"
        self.requete = False
        self.image = pygame.image.load("gui_element/crawler_management/captain_room.png").convert_alpha()
        self.poid = 4000
        self.stockage = [air(),air()]
        self.priorite_og = 5
            
    def ça_place(self,place_general,alenv):
        self.place_general = place_general
        self.alenv = alenv


class sale_stock():
    def __init__(self):
        self.categorie = "stock"
        self.taille = 1
        self.fuel = "None"
        self.image = pygame.image.load("gui_element/crawler_management/cargo.png").convert_alpha()
        self.poid = 2000
        self.stockage = [charbon(),charbon(),bois()]
        self.requete = False
        self.priorite_og = 1
        self.contient = [[],[],[],[],[],[],[],[]]
        pos_contenu = [5,105]
        tak = 0

        for i in range (2):
            for j in range (4):
                for y in range (4):
                    self.contient[tak].append(stockage(pos_contenu))
                    pos_contenu[0] += 12
                pos_contenu[0] += -48
                pos_contenu[1] += 21
                tak += 1
            pos_contenu[0] = 58
            pos_contenu[1] = 105
        
        #print (self.contient[1][0][0].pos[0])
        
    def ça_place(self,place_general,alenv):
        self.place_general = place_general
        self.alenv = alenv

        self.cord_stock = [place_general+50,137+358]
        
        if self.alenv == True:
            self.cord_stock[1] = 226+358


class sale_repas_1():
    def __init__(self):
        self.categorie = "repas"
        self.requete = False
        self.fuel = "None"
        self.beaute = 3 #si il est plaisant ou non de se tenir a côté de lui
        self.vie = 30
        self.pannes = 0 #en %  0 = jamais en panne    100 = Toujours en panne
        self.image = pygame.image.load("gui_element/crawler_management/eating_room.png").convert_alpha()
        self.taille = 1
        self.events = "aucun"
        self.poid = 3000 # 5 000 kg ou 5t
        self.demande = 0
        self.stockage = [repas_medium(),repas_medium()]
        self.priorite_og = 0
        
        self.contient = [[]]
        pos_contenu = [74,167+358]
        self.siege = 9
        self.siege_p = [False,False,False,False,False,False,False,False,False]
        for j in range (3):
            self.contient[0].append([stockage(pos_contenu)])
            pos_contenu[0] += 12
        
        
    def ça_place(self,place_general,alenv):
        self.place_general = place_general
        self.alenv = alenv


        self.cord_stock = [place_general+45,122+358]
        self.cord_siege = [[place_general+41,100+358],[place_general+26,116+358],[place_general+41,131+358],[place_general+23,144+358],[place_general+8,159+358],[place_general+39,159+358],[place_general+66,124+358],[place_general+81,139+358],[place_general+66,155+358]]
        
        if self.alenv == True:
            self.cord_stock[1] = 241+358
            for ji in range (self.siege):
                tmp = (self.cord_siege[ji][1] - 358) - 368
                tmp = tmp - tmp - tmp
                self.cord_siege[ji][1] = tmp+358
                
            
        for j in range(len(self.contient[0])):
            self.contient[0][0][0].pos = self.cord_stock
        


class stockage():
    def __init__(self,pos):
        self.etage = 3
        self.pos = [pos[0],pos[1]]
        self.contenu = [air(),air(),charbon()]
        

class air():
    def __init__(self):
        self.couleur = [255,255,255]
        self.quel_type = "vide"
        self.masse_m3 = 0
        self.masse = 0
        self.qqt = 15
        self.quoi = "air"
        self.brule = False
        
class charbon():
    def __init__(self):
        self.couleur = [0,0,0]
        self.brule = True
        self.quel_type = "combustible"
        self.quoi = "charbon"
        self.masse_m3 = 1500   #poid d'un m3
        self.qqt = 1000 #en m3 = 1  Capacité max homme = 20 en m3 = 0,02
        
        self.masse = (self.masse_m3 * self.qqt) / 1000
        self.chaufe = 25    #qqt de chaleur fournit
        
        
        self.pos = [0,0]
        self.etat = "vrac"  #vrac / ranger / utile
        

class charbon_bois():
    def __init__(self):
        self.couleur = [255,255,255]
        self.quel_type = "combustible"
        self.brule = True
        self.masse_m3 = 560
        self.chaufe = 23
        self.quoi = "charbon de bois"

        self.masse = (self.masse_m3 * self.qqt) / 1000
        
class bois():
    def __init__(self):
        self.couleur = [255,255,255]
        self.quel_type = "construction"
        self.brule = True
        self.quoi = "bois"
        self.masse_m3 = 500
        self.chaufe = 16
        
        self.qqt = 1000 #en m3 = 1  Capacité max homme = 20 en m3 = 0,02
        
        self.masse = (self.masse_m3 * self.qqt) / 1000
        self.chaufe = 25    #qqt de chaleur fournit
        
        
        self.pos = [0,0]
        self.etat = "vrac"  #vrac / ranger / utile
        
        
class gold():
    def __init__(self):
        self.couleur = pygame.color.Color('#1a1e2f')
        self.quel_type = "richesse"
        self.quoi = "or"
        self.masse_m3 = 19300
        self.qqt = 1000
        self.masse = (self.masse_m3 * self.qqt) / 1000
class water():
    def __init__(self):
        self.couleur = pygame.color.Color('#1a1e2f')
        self.quel_type = "liquide"
        self.quoi = "Eau"
        self.brule = False
        #self.masse_m3 = 
        
class raw_food():
    def __init__(self):
        self.couleur = pygame.color.Color('#1a1e2f')
        self.quel_type = "consommable"
        self.quoi = "Nourriture crue"

class repas_medium():
    def __init__(self):
        self.couleur = [255,255,255]
        self.quel_type = "consommable"
        self.quoi = "Nourriture cuisinée"
        self.brule = False
        self.masse_m3 = 1250
        self.nutrition = 1850 #1850 cal par kg
        
        self.qqt = 1000 #en m3 = 1  Capacité max homme = 20 en m3 = 0,02
        
        self.masse = (self.masse_m3 * self.qqt) / 1000
        
        self.pos = [0,0]
        self.etat = "vrac"  #vrac / ranger / utile


class moteur_charbon_2():
    def __init__(self):
        self.categorie = "moteur"
        self.fuel = "feu"
        self.rendement = 0.06 #il faut 0.06 unité de fuel pour développer 1 chevaux
        self.beaute = -15 #si il est plaisant ou non de se tenir a côté de lui
        self.vie = 70
        self.pannes = 65 #en %  0 = jamais en panne    100 = Toujours en panne
        self.image = pygame.image.load("gui_element/crawler_management/steam_engine.png").convert_alpha()
        self.taille = 2
        self.rendement_max = 2000    #nb cheveaux totaux max
        self.rendement_actu = 0
        self.events = "aucun"
        self.poid = 8000 # 8 000 kg ou 8t
        self.stock_fuel_max = 4000 #4T
        self.perte_inertie = 1 #nb de cheveaux le moteur perd
        self.demande = 0
        
        
        
        
    def ça_place(self,place_general,alenv):
        self.place_general = place_general
        self.alenv = alenv
        
        self.cord_stock = [place_general+30,120+358]
        self.cord_conso = [place_general+70,137+358]
        
        if self.alenv == True:
            self.cord_stock[1] = 248+358
            self.cord_conso[1] = 231+358
            
        

class team():
    def __init__(self):
        self.membre = [bonhomme]
        self.assigne = "aucun"
        self.ordre = "aucun"

class bonhomme():
    def __init__(self,trait,trait_promis,num_trait_total,mental):
    
        deb = ["À","A","Aa","Ab","Ae","Ai","Aj","Au","Ay","Ba","Bai","Be","Bi","Bla","Ble","Bo","Bra","Bri","Bru","Bu","Ca","Cai","Ce","Cha","Che","Chi","Chia","Chlo","Chri","Chry","Ci","Clou","Clu","Co","Cri","Cry","Cy","Da","Dai","De","Deu","Di","Do","Dra"," Du","Dua","Dy","Dzo","E","Ea","Ei","El","Fa","Fe","Fi","Fla","Flo","Fo","Fra","Fre","Fri","Fu","Gü","Ga","Gae","Gau","Geo","Gi","Gio","Giu","Glo","Go","Gre","Gu","Guo","Guy","Ha","Hay","He","Hei","Hi","Ho","Hu","Hui","Hui","I","Io","Jú","Ja","Jay","Je","Ji","Jia","Jie","Jo","Joe","Ju","Jua","Ka","Kai","Ke","Kha","Ki","Ko","Kri","Kse","Ku","Lé","La","Lau","Le","Lei","Li","Lia","Lo","Lou","Lu","Ly","Má","Ma","Maa","Mau","Me","Mi","Mo","Mou","Mu","My","My","Na","Ne","Nea","Ni","Nie","No","Nu","O","Pa","Pau","Pe","Phae","Phi","Pi","Po","Pre","Pri","Pu","Py","Qia","Qio","Qui","Ró","Ra","Rai","Ray","Re","Ree","Reu","Rey","Rhi","Ri","Ro","Ru","Ry","Sa","Sca","Sco"," Se","Sei","Seo","Sha","Shay","Shei","Shi","Shie","Shri","Shu","Si","Sji","Sla","Smi","Smy","So","Sou","Squa","Sta","Ste","Stra","Su","Ta","Tao","Te","Tha","The","Tho","Ti","To","Tre","Tri","Tsu","U","Va","Ve","Vi","Vo","Vu","Wa","We","Wei","Wi","Xa","Xe","Xi","Xia","Xu","Ya","Ye","Yi","Yo","You","Yu","Za","Ze","Zey","Zhe","Zi","Zo"]
        fin = ["-Ca","-Cla","-Mi","-fe","-hao","-hui","-ju","-yeo","-yu","á","ão","a","a^","ao","ba","bda","bde","bdu","be","bi","bo","bra","bri","bu","by","cí","ca","ce","cemea","cha","chae","che","chi","ci","cia","cie","ciou","ckey","ckso","cly","co","cque","cto","cy","da","dda","de","dga","di","dley","do","dou","dra","dri","dva","dwa","dy","dya","e","ey","fí","fa","fe","ffa","ffie","fi","fka","fu","fya","g^","ga","gai","gde","gge","ggy","ghe","ghu","gi","gne","gnu","go","gu","gue","h-mi","ha","hdi","he","hei","hi","hma","hme","hmou","hn_Pau","hnny","hra","i","ia","j","ja","ji","jo","ka","kae","kau","kha","khai","ki","kka","kke","kki","kko","ko","ksa","ksi","kto","ku","l-Fa","l-Ra","la","lay","lbe","lchi","lda","lda","lda","ldo","le","lea","ley","lga","lge","lhe","li","lia","lii","lka","lla","lle","lli","llia","llie","llo","lly","lma","lme","lna","lo","lpe","lphie","lsa","lso","lta","lte","lthe","lti","lu","lvi","ly","mó","ma","maa","mchai","me"," mi","mja","mma","mme","mmi","mmy","mo","mpy","mri","msa","mu","my","mza","n_Da","n-ju","na","nbaa","nca","nce","ncho","nci","nda","nde","ndra","ndre","ndrei","ndsay","ndy","ne","nei","ng_Wei","nga","nge","ngho","ngqi","ngu","ni","nie","nio","nja","nje","nla","nley","nna","nni","nnie","nno","nny","no","nou","nry","nso","nta","nte","nthe","ntho","nti","nu","nue","nwu","ny","nya","nye","nze","nzhu","o","pa","pha","phe","phi","phie","pho","ppe","pu","r-A","rí","ra","rbe","rcu","rdo","rdna","re","rey","rga","rgei","rghe","rgi","rgo","rgré","rgre","rgrje","rhi","ri","rie","rii","rje","rkai","rke","rko","rku","rla","rle","rlie","rlo","rma","rmaa","rme","rmi","rna","rne","ro","rpe","rre","rri","rry","rse","rsu","rte","rtho","rti","ru","rvey","rvi","rwa","ry","rya","rzo","sé","sa","sci","sco","se","sey","sh","sha","shley","shna","shoi","shqa","shu","si","sia","ska","smi","smu","sna","snaa","sni","so","ssa","sse","ssei","ssi","ssie","stí","stín","sta","ste","sti","stia","sto","stu","su","sy","té","tí","ta","tche","te","tha","thy","ti","tkhaa","tma","to","tou","tra","tri","tsi","tsu","tte","tthe","tthi","tto","tviy","tze","u","va","vaa","ve","vi","vie","vo","vy","wa","we","wi","wkwi","wre","xa","xbloo","xe","xi","xte","ya","z","za","ze","zi","zoo","zta","zzie"]
        
        self.nom = ["",""]
        
        for long in range (len(self.nom)):
        
            tak = random.randint(1,2)
            
            self.nom[long] = deb[random.randint(0,len(deb)-1)]
            for i in range (tak):
                self.nom[long]+= fin[random.randint(0,len(fin)-1)]
        print("nom",self.nom)
        
        
        self.homme_rect = pygame.Rect(490-105,358+29,110,34)
        self.team = 0
        self.trait_tot = []
        self.selected = False
        self.ordre = "aucun"
        self.pos = [0,358]
        self.main = air()
        self.place = "nulle"
        self.une_demande = 0
        self.siege = -1
        for i in range(len(trait_promis)):
            trait.lequel_pour_moi(trait_promis[i])
            
            self.trait_tot.append([trait.type_trait])
            
        for i in range(num_trait_total):
            pif = random.randint(1,25)

            trait.lequel_pour_moi(pif)

            self.trait_tot.append([trait.type_trait])
        
        self.mental = mental
        self.fatigue = 0
        self.faim = 0
        
        for y in range(len(self.trait_tot)):
            print(self.trait_tot[y])
            
        self.mental_max = trait.mental_max
        self.gain_fatigue = trait.gain_fatigue
        self.og_vitesse = trait.vitesse
        
        self.force = trait.force
        self.soif = trait.soif
        self.salaire = trait.salaire
        self.calo_conso = trait.calo_conso
        
        self.vitesse = self.og_vitesse - self.main.masse / self.force
        
    
    def direction(self):
        if self.ordre == 'moteur':
            self.direc = "moteur"
            
        elif self.ordre == 'transport':
            if self.une_demande < 1:
                self.direc = "repos"
            else:
                if self.main.quel_type == "vide":
                    self.direc = "stock"
                else:
                    self.direc = "demande"
        
        elif self.ordre == "repas":
            self.direc = "repas"
        
        if self.ordre == 'aucun' or self.ordre == 'repos' or self.direc == 'repos':
            if self.faim > 400 or self.direc == "repas" and self.faim > 0:
                self.direc = "repas"
            elif self.fatigue > 50:
                self.direc = "coucher"
            else:
                self.direc = "repos"
        
                
    def deplacement (self):
        pass
   
#"À","A","Aa","Ab","Ae","Ai","Aj","Au","Ay","Ba","Bai","Be","Bi","Bla","Ble","Bo","Bra","Bri","Bru","Bu","Ca","Cai","Ce","Cha","Che","Chi","Chia","Chlo","Chri","Chry","Ci","Clou","Clu","Co","Cri","Cry","Cy","Da","Dai","De","Deu","Di","Do","Dra"," Du","Dua","Dy","Dzo","E","Ea","Ei","El","Fa","Fe","Fi","Fla","Flo","Fo","Fra","Fre","Fri","Fu","Gü","Ga","Gae","Gau","Geo","Gi","Gio","Giu","Glo","Go","Gre","Gu","Guo","Guy","Ha","Hay","He","Hei","Hi","Ho","Hu","Hui","Hui","I","Io","Jú","Ja","Jay","Je","Ji","Jia","Jie","Jo","Joe","Ju","Jua","Ka","Kai","Ke","Kha","Ki","Ko","Kri","Kse","Ku","Lé","La","Lau","Le","Lei","Li","Lia","Lo","Lou","Lu","Ly","Má","Ma","Maa","Mau","Me","Mi","Mo","Mou","Mu","My","My","Na","Ne","Nea","Ni","Nie","No","Nu","O","Pa","Pau","Pe","Phae","Phi","Pi","Po","Pre","Pri","Pu","Py","Qia","Qio","Qui","Ró","Ra","Rai","Ray","Re","Ree","Reu","Rey","Rhi","Ri","Ro","Ru","Ry","Sa","Sca","Sco"," Se","Sei","Seo","Sha","Shay","Shei","Shi","Shie","Shri","Shu","Si","Sji","Sla","Smi","Smy","So","Sou","Squa","Sta","Ste","Stra","Su","Ta","Tao","Te","Tha","The","Tho","Ti","To","Tre","Tri","Tsu","U","Va","Ve","Vi","Vo","Vu","Wa","We","Wei","Wi","Xa","Xe","Xi","Xia","Xu","Ya","Ye","Yi","Yo","You","Yu","Za","Ze","Zey","Zhe","Zi","Zo"
#"_Ca","_Cla","_Mi","-fe","-hao","-hui","-ju","-yeo","-yu","á","ão","a","a^","ao","ba","bda","bde","bdu","be","bi","bo","bra","bri","bu","by","cí","ca","ce","cemea","cha","chae","che","chi","ci","cia","cie","ciou","ckey","ckso","cly","co","cque","cto","cy","da","dda","de","dga","di","dley","do","dou","dra","dri","dva","dwa","dy","dya","e","ey","fí","fa","fe","ffa","ffie","fi","fka","fu","fya","g^","ga","gai","gde","gge","ggy","ghe","ghu","gi","gne","gnu","go","gu","gue","h-mi","ha","hdi","he","hei","hi","hma","hme","hmou","hn_Pau","hnny","hra","i","ia","j","ja","ji","jo","ka","kae","kau","kha","khai","ki","kka","kke","kki","kko","ko","ksa","ksi","kto","ku","l-Fa","l-Ra","la","lay","lbe","lchi","lda","lda","lda","ldo","le","lea","ley","lga","lge","lhe","li","lia","lii","lka","lla","lle","lli","llia","llie","llo","lly","lma","lme","lna","lo","lpe","lphie","lsa","lso","lta","lte","lthe","lti","lu","lvi","ly","mó","ma","maa","mchai","me"," mi","mja","mma","mme","mmi","mmy","mo","mpy","mri","msa","mu","my","mza","n_Da","n-ju","na","nbaa","nca","nce","ncho","nci","nda","nde","ndra","ndre","ndrei","ndsay","ndy","ne","nei","ng_Wei","nga","nge","ngho","ngqi","ngu","ni","nie","nio","nja","nje","nla","nley","nna","nni","nnie","nno","nny","no","nou","nry","nso","nta","nte","nthe","ntho","nti","nu","nue","nwu","ny","nya","nye","nze","nzhu","o","pa","pha","phe","phi","phie","pho","ppe","pu","r-A","rí","ra","rbe","rcu","rdo","rdna","re","rey","rga","rgei","rghe","rgi","rgo","rgré","rgre","rgrje","rhi","ri","rie","rii","rje","rkai","rke","rko","rku","rla","rle","rlie","rlo","rma","rmaa","rme","rmi","rna","rne","ro","rpe","rre","rri","rry","rse","rsu","rte","rtho","rti","ru","rvey","rvi","rwa","ry","rya","rzo","sé","sa","sci","sco","se","sey","sh","sha","shley","shna","shoi","shqa","shu","si","sia","ska","smi","smu","sna","snaa","sni","so","ssa","sse","ssei","ssi","ssie","stí","stín","sta","ste","sti","stia","sto","stu","su","sy","té","tí","ta","tche","te","tha","thy","ti","tkhaa","tma","to","tou","tra","tri","tsi","tsu","tte","tthe","tthi","tto","tviy","tze","u","va","vaa","ve","vi","vie","vo","vy","wa","we","wi","wkwi","wre","xa","xbloo","xe","xi","xte","ya","z","za","ze","zi","zoo","zta","zzie"
   
class Trait():
    def __init__(self):
        self.type_event = "event/trait.txt"
        self.type_trait = "init"

        
    def lequel_pour_moi(self,num_ligne_ext):
        yup = random.randint(50,120)
        self.vitesse = yup / 100
        self.mental_max = 100
        self.etat_critique = "aucun"
        self.gain_fatigue = 1 #
        self.force = 5   #dgs / 10 (donc 0.5 dgts)    quand transporte qqc, la fatigue et la vitesse sont augmenté par le kg dvs par force.  
        self.salaire = 20 #Lors de la fin de son contrat, vous devrez payer cette somme. Vous pouver augmenter la durrée de son contrat, mais devrer payer une 2ème fois cette somme + taux d'intéret
        self.soif = 1.5 #La quantité d'eau en L consomée a la fin du jour. Si ce besoin n'est pas remplis, perd 15 de vie
        self.calo_conso = 0.016 #La quantité de calorie consomée chaque secondes. 1 minutes = 30 secondes. 1 minutes = 0,5 cal Elle est multipliée par l'effort fournie (divs par la force). Humain moyen = 50cal/h, 2400cal/j. Approx, 0.5 cal/min au repo  1.5 cal/min sur tache penibles   cal_min/j = 720


        with open(self.type_event, "r", encoding='utf-8') as fichier:
            num_ligne = 0
            
            for ligne in fichier:
            
                if num_ligne == num_ligne_ext:
                
                    for sprite in ligne:           
                        if sprite == '😴':  #1 
                            self.type_trait = "fatigue" #gain fatigue ++  salaire -   vie ++
                            self.gain_fatigue += 1
                            self.mental_max += 20
                            self.salaire += -5
                            self.calo_conso += -0.004
                            
                        elif sprite == '😭':   #2
                            self.type_trait = "depressif" #joie max --  perd  +++  plaisance cote--  force --  rebel --  salaire --  vitesse --
                            self.mental_max += -50
                            self.gain_fatigue += 0.5
                            self.vitesse += -0.2
                            self.salaire += -5
                            
                        elif sprite == '🤑':   #3
                            self.type_trait = "avare" #est tenté par l'argent ! peut volé   salaire_min +
                            self.mental_max += 20
                            self.salaire += 15
                            self.soif += -0.2
                            
                        elif sprite == '😱':   #4
                            self.type_trait = "craintif" #perd mental ++ ! uniquement peur  plaisance_cote-
                            self.etat_critique = "peur"
                            
                        elif sprite == '😡':   #5
                            self.type_trait = "colerique" #perd plus vite son mental ! uniquement rage   degats +   plaisance_cote-
                            self.force+= 2
                            self.mental_max += -20
                            self.etat_critique = "rage"
                            
                        elif sprite == '🏃':   #6
                            self.type_trait = "sportif" #gagne plus lentement de la fatigue  force +   degats +   vitesse +   faim ++  soif+   vie +
                            self.gain_fatigue += -0.2
                            self.vitesse += 0.2
                            self.force+= 2
                            self.soif += 0.5
                            self.calo_conso += 0.002
                        
                        elif sprite == '💪':   #7
                            self.type_trait = "muscle" #force ++  degats +  faim +  soif+    vie +
                            self.gain_fatigue += -0.5
                            self.force+= 5
                            self.soif += 0.5
                            self.calo_conso += 0.002
                            
                        elif sprite == '🦵':   #8
                            self.type_trait = "rapide" #gain fatigue -   vitesse ++  faim +   soif ++
                            self.gain_fatigue += -0.1
                            self.vitesse += -0.5
                            self.soif += 0.5
                            self.calo_conso += -0.003
                            
                        elif sprite == '🤛':   #9
                            self.type_trait = "agressif" #perd mental+  !colere uniquement  degats +   chances rebellion +   sociable -   plaisance_cote --
                            self.etat_critique = "rage"
                            self.force+= 1
                        
                        elif sprite == '🤝':   #10
                            self.type_trait = "amicale" #sociable ++   rebel -   plaisance_cote +
                            self.salaire += -3
                            self.soif += -0.1
                        
                        elif sprite == '🙏':   #11
                            self.type_trait = "soumis" #rebel ---  force-  vitesse-  salaire_min ----
                            self.mental_max += 50
                            self.gain_fatigue += 0.5
                            self.salaire += -15
                            self.soif += -0.5
                        
                        elif sprite == '👴':   #12
                            self.type_trait = "vieux" #vitesse -  degats --   force --  salaire_min-   plaisance_cote +   vie --
                            self.gain_fatigue += 0.5
                            self.vitesse += -0.4
                            self.force += -2
                            self.salaire += -10
                        
                        elif sprite == '🔧':   #13
                            self.type_trait = "mecanique"  #taux construction ++    salaire +   vie +
                            self.force+= 2
                            self.salaire += 3
                            self.soif += 0.2
                        
                        elif sprite == '🍳':   #14
                            self.type_trait = "cuisine" #taux cuistot ++     salaire +  plaisance_cote +   vie +
                            self.mental_max += 15
                            self.salaire += 3
                            self.calo_conso += -0.003
                        
                        elif sprite == '🎓':   #15
                            self.type_trait = "intelo" #rebel +   taux radio ++    taux comptable ++   taux navig ++   salaire +   plaisance_cote +
                            self.mental_max += 15
                            self.salaire += 10
                        
                        elif sprite == '💋':   #16
                            self.type_trait = "glamour" #sociable +++    plaisance_cote ++
                        
                        
                        elif sprite == '🎵':   #17
                            self.type_trait = "musicale"  #sociable +  plaisance_cote +++
                            self.mental_max += 25
                        
                        elif sprite == '🔪':   #18
                            self.type_trait = "meurtre" #perte mental+   salaire ----   !meurtre   
                            self.etat_critique = "meurtre"
                            self.force+= 3
                            self.salaire += -10
                        
                        elif sprite == '🍕':   #19
                            self.type_trait = "mangeur" #vie ++  faim ++
                            self.mental_max += 20
                            self.soif += 0.2
                            self.calo_conso += 0.006
                        
                        elif sprite == '🥖':   #20
                            self.type_trait = "maigre" #faim ---   vie -  force --
                            self.calo_conso += -0.009
                            self.force+= -1
                        
                        elif sprite == '📢':   #21
                            self.type_trait = "orateur" #sociable ++   rebel ++
                            self.salaire += 5
                            self.soif += 0.1
                        
                        elif sprite == '🪓':   #22
                            self.type_trait = "bucheron" #force ++   degats ++
                            self.etat_critique = "rage"
                            self.force+= 4
                            self.calo_conso += 0.003
                        
                        
                        elif sprite == '🛐':   #23
                            self.type_trait = "religieux" #rebel --
                            self.etat_critique = "peur"
                            self.mental_max += 50
                            self.salaire += -10
                        
                        elif sprite == '🚱':   #24
                            self.type_trait = "chameaux" #soif ---
                            self.soif += -0.5
                        
                        
                        elif sprite == '🚰':   #25
                            self.type_trait = "fontaine" #soif ++
                            self.soif += 1

                num_ligne += 1
                
        print("vitesse:",self.vitesse)
