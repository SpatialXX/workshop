class GraphOriente:
    def __init__(self):
        self.liste_sommets = []
        self.liste_arcs = []
        
    def ajouter_sommet(self,A):
        self.liste_sommets.append(A)
    def ajouter_arc (self,A,B):
        self.liste_arcs.append(A,B)
    def supprimer_arc (self, A, B):
        for i in range(self.liste_arcs):
            if self.liste_arcs[i] == (A,B):
                del self.liste_arcs[i]
    def liste_sommets_issus(self,A):
        liste = []
        for i in range(self.liste_arcs):
            if self.liste_arcs[i][0] == A:
                liste.append(self.liste_arcs[i][1])
            
        return liste
        
