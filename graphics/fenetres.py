from tkinter import *
from time import *
from random import *
from tkinter.font import *
from math import sqrt

dico_alignement = {'gauche' : W , 'droite' : E, 'haut' : N , 'bas' : S, 'gauche_bas' : SW, 'gauche_haut' : NW, 'droite_bas' : SE,'droite_haut' : NE,
                         'etirement_horizontal' : W+E, 'etirement_vertical' : N+S, 'etirement_total' : N+S+E+W, 'centre' : None}

class Fenetre(Tk):

        """ la classe Fenetre hérite de la classe Tk
                par défaut son titre est GRAPHICS et on peut la redimensionner
                Elle possède les attributs en plus des attributs de la classe Tk:
                - __parametres_cadres__ (paramètres par défaut des cadres et des canvas créés)
                - __parametres_boutons__(paramètres par défaut des boutons créés)
                - __parametres_saisies__ (paramètres nommés des zones de saisie
               
                Elle possède les méthodes :
                - cadre : pour créer un cadre
                - graphique : pour créer une zone graphique
                - bouton : pour créer des boutons de commande
                - saisie : pour créer des zones de saisie
                - etiquette : pour créer des étiquettes """


        def  __init__(self,titre = 'GRAPHICS'):
                """ constructeur de fenêtre, il prend comme argument le titre de la fenêtre"""
                Tk.__init__(self)
                self.resizable(1,1) # par défaut, on autorise le redimensionnemnt
                self.title(titre)
                self.__parametres_cadres__ = {'largeur' : 100, 'hauteur' : 100,'couleur' : 'white','plage' : ((0,0),(0,0)),'marge_hor' : 0,'marge_vert' : 0}
                self.__parametres_boutons__ = {'commande':None ,'largeur' : 10, 'hauteur' : 2,'couleur' : 'grey','plage' : ((0,0),(0,0)),'marge_hor' : 0,'marge_vert' : 0,
                                           'couleur_texte' : 'black','alignement':'centre','texte' : 'bouton'}
                self.__parametres_saisies__ = {'texte_par_defaut':'', 'couleur' : 'white','plage' : ((0,0),(0,0)),'marge_vert' : 0,'marge_hor' : 0,
                                               'alignement' : 'centre','largeur' : 5,'hauteur' : None,'taille_police' : 20,'style_police' : 'Verdana'}
                self.__parametres_etiquettes__ = {'couleur' : 'grey','couleur_texte':'black','plage': ((0,0),(0,0)),'marge_vert':0,'marge_hor':0,
                                                  'alignement':'centre','largeur':10,'hauteur':None,'taille_police':12,'style_police':'Verdana','effet_police' : 'normal'}
                
        def cadre(self,**parametres):
                """ Crée un cadre dans la fenêtre avec comme paramètres nommés par défaut :
                {'largeur' : 100, 'hauteur' : 100,'couleur' : 'white','plage' : ((0,0),(0,0)),'marge_hor' : 0,'marge_vert' : 0}"""
                nouveaux_parametres = self.__parametres_cadres__ 
                for cle in parametres.keys():
                        nouveaux_parametres[cle]=parametres[cle]
                return Cadre(self,**nouveaux_parametres)

        def graphique(self,**parametres):
                """ Crée une zone graphique dans la fenêtre avec comme paramètres nommés par défaut :
                {'largeur' : 100, 'hauteur' : 100,'couleur' : 'white','plage' : ((0,0),(0,0)),'marge_hor' : 0,'marge_vert' : 0}"""

                nouveaux_parametres = self.__parametres_cadres__ 
                for cle in parametres.keys():
                        nouveaux_parametres[cle]=parametres[cle]
                return Graphique(self,**nouveaux_parametres)

        def bouton(self,**parametres):
                """ Crée un bouton dans la fenêtre avec comme paramètres nommés par défaut :
                {'largeur' : 20, 'hauteur' : 10,'couleur' : 'grey','plage' : ((0,0),(0,0)),'marge_hor' : 0,'marge_vert' : 0,
                'couleur_texte' : 'black','alignement'='centre','texte' = 'bouton'}"""
                nouveaux_parametres = self.__parametres_boutons__ 
                for cle in parametres.keys():
                        nouveaux_parametres[cle]=parametres[cle]
                return Bouton(self,**nouveaux_parametres)

        def saisie(self,**parametres):
                """ zone de saisie de texte """
                nouveaux_parametres = self.__parametres_saisies__ 
                for cle in parametres.keys():
                        nouveaux_parametres[cle]=parametres[cle]
                return Saisie(self,**nouveaux_parametres)

        def etiquette(self,texte,**parametres):
                """ Définit une étiquette  """
                dict_effet = {'normal' : 'normal','gras' : 'bold','italique':'italic','souligne':'underline'}
                nouveaux_parametres = self.__parametres_etiquettes__ 
                for cle in parametres.keys():
                        nouveaux_parametres[cle]=parametres[cle]
                return Etiquette(self,texte,**nouveaux_parametres)

        def supprimer(self):
                """supprime la fenêtre"""
                self.destroy()
                
class Cadre(Frame):
        """ Classe permettant de créer une zone graphique dans une fenêtre """

        def __init__(self,f, **parametres):
                """constructeur d'un cadre. Il prend comme paramètre de position une fenêtre f et comme paramètres nommés :
                {'largeur' : 100, 'hauteur' : 100,'couleur' : 'white','plage' : ((0,0),(0,0)),'marge_hor' : 0,'marge_vert' : 0}"""
                #capture des paramètres
                l = parametres['largeur']
                h = parametres['hauteur']
                c = parametres['couleur']
                p = parametres['plage']
                mh = parametres['marge_hor']
                mv = parametres['marge_vert']
                # création du cadre
                Frame.__init__(self,f,width = l, height = l, bg = c)
                # affichage dans la grille
                ligne , colonne = p[0][0] , p[0][1]
                nb_lign , nb_col = p[1][0]-p[0][0]+1 , p[1][1]-p[0][1]+1
                self.grid( row=ligne,column = colonne,rowspan = nb_lign, columnspan= nb_col, padx = mh, pady=mv,sticky = dico_alignement['centre'])
                
        def supprimer(self):
                self.destroy()

class Bouton(Button):
        """ classe définissant un bouton de commande associé à une fonction"""
        
        def __init__(self,f,**parametres) :
                """ constructeur de bouton. Il prend comme arguments nommés :
                {'commande' : None,'largeur' : 20, 'hauteur' : 10,'couleur' : 'grey','plage' : ((0,0),(0,0)),'marge_hor' : 0,'marge_vert' : 0,
                'couleur_texte' : 'black','alignement':'centre','texte' : 'bouton'}"""
                #capture des paramètres
                commande = parametres['commande']
                l = parametres['largeur']
                h = parametres['hauteur']
                c = parametres['couleur']
                ct = parametres['couleur_texte']
                t = parametres['texte']
                p = parametres['plage']
                mh = parametres['marge_hor']
                mv = parametres['marge_vert']
                al = parametres['alignement']
                 
                # création du bouton
                Button.__init__(self,f,text=t,fg=ct,bg=c,command=commande,width=l,height=h)
                # affichage dans la grille
                ligne, colonne = p[0][0],p[0][1]
                nb_lign , nb_col = p[1][0]-p[0][0]+1 , p[1][1]-p[0][1]+1
                self.grid(row=ligne,column = colonne,rowspan = nb_lign, columnspan= nb_col,sticky = dico_alignement[al],padx=mh,pady=mv)

class Saisie(Entry):
        """zone de saisie"""
        def __init__(self,f,**parametres) :
                #capture des paramètres
                td = parametres['texte_par_defaut']
                sp = parametres['style_police']
                tp = parametres['taille_police']
                l = parametres['largeur']
                h = parametres['hauteur']
                c = parametres['couleur']
                p = parametres['plage']
                mh = parametres['marge_hor']
                mv = parametres['marge_vert']
                al = parametres['alignement'] 
                #création de la zone de saisie
                Entry.__init__(self,f,bg=c,width=l,height =h,font = (sp,tp))
                self.insert(0,td)
                # affichage dans la grille
                ligne, colonne = p[0][0],p[0][1]
                nb_lign , nb_col = p[1][0]-p[0][0]+1 , p[1][1]-p[0][1]+1
                self.grid(row=ligne,column = colonne,rowspan = nb_lign, columnspan= nb_col,sticky = dico_alignement[al],padx=mh,pady=mv)
                        
        def effacer(self):
                self.delete(0,END)
        def lire(self):
                return self.get()
        def supprimer(self):
                self.destroy()

class Etiquette(Label):
        """zone de saisie"""
        def __init__(self,f,texte,**parametres) :
                #capture des paramètres
                sp = parametres['style_police']
                tp = parametres['taille_police']
                ep = parametres['effet_police']
                l = parametres['largeur']
                h = parametres['hauteur']
                c = parametres['couleur']
                ct = parametres['couleur_texte']
                p = parametres['plage']
                mh = parametres['marge_hor']
                mv = parametres['marge_vert']
                al = parametres['alignement']  
                #création de l'étiquette
                Label.__init__(self,f,text=texte,bg=c,fg=ct,width=l,height =h,font = (sp,tp,ep))
                # affichage dans la grille
                ligne, colonne = p[0][0],p[0][1]
                nb_lign , nb_col = p[1][0]-p[0][0]+1 , p[1][1]-p[0][1]+1
                self.grid(row=ligne,column = colonne,rowspan = nb_lign, columnspan= nb_col,sticky = dico_alignement[al],padx=mh,pady=mv)
                        
        def supprimer(self):
                self.destroy()
                
class Point:
        """ classe définissant un point dans une fenêtre graphique
        Les coordonnées doivent être entières"""
        def __init__(self,abscisse,ordonnee):
                """ le constructeur prend l'abscisse et l'ordonnée du point """
                self.x=round(abscisse)
                self.y=round(ordonnee)
        def distance(self,q):
                """distance entre deux points """
                return round(sqrt((self.x-q.x)**2+(self.y-q.y)**2))

class Graphique(Canvas):

        """ Classe permettant de créer une zone graphique attachée à une fenêtre donnée
        Elle possède comme attributs:
        __largeur__
        __hauteur__
        __couleur__"""

        def __init__(self,f, **parametres ):
                """constructeur d'une zone graphique, il prend comme paramètres nommés :
                {'largeur' : 100, 'hauteur' : 100,'couleur' : 'noir','plage' : ((0,0),(0,0)),'marge_hor' : 0,'marge_vert' : 0}"""
                #capture des paramètres
                self.__largeur__ = parametres['largeur']
                self.__hauteur__ = parametres['hauteur']
                self.__couleur__ = parametres['couleur']
                p = parametres['plage']
                mh = parametres['marge_hor']
                mv = parametres['marge_vert']
                #création de la zone graphique
                Canvas.__init__(self,f,width = self.__largeur__, height = self.__hauteur__, bg = self.__couleur__)
                
                # affichage dans la grille
                ligne, colonne = p[0][0],p[0][1]
                nb_lign , nb_col = p[1][0]-p[0][0]+1 , p[1][1]-p[0][1]+1
                self.grid(row=ligne,column = colonne,rowspan = nb_lign, columnspan= nb_col,padx = mh,pady=mv,sticky = dico_alignement['centre'])

        def dim(self):
                """retourne les dimensions de la fenêtre sous la forme d'un couple : (largeur,heuteur)"""
                return {'largeur':self.__largeur__, 'hauteur':self.__hauteur__}

        def set_couleur(self,couleur):
                """change lacouleur de fond de la zone graphique"""
                self.configure(bg = couleur)
                self.__couleur__ = couleur

        def set_dim(self,largeur,hauteur):
                """ change la taille de la zone graphique"""
                self.configure(width = largeur,height = hauteur)
                self.__largeur__ = largeur
                self.__hauteur__ = hauteur

        def activer_clavier(self):
                """ active le clavier dans la zone graphique"""
                self.focus_set()

        def supprimer(self):
                """supprime la zone graphique """
                self.destroy()

        # FORMES GRAPHIQUES

        def draw_line(self,p,q,couleur):
                """ dessine un segment entre les points p et q de type POINT avec la couleur donnée """
                l=self.create_line(p.x,p.y,q.x,q.y,fill=couleur)
                self.grid()
                return l

        def draw_pixel(self,p,couleur):
                """ dessine un pixel situé au point p avec la couleur donnée """
                pix=self.create_line(p.x,p.y,p.x+1,p.y,fill=couleur)
                self.grid()
                return pix
        
        def draw_line_pointille(self,p,q,couleur):
                """ dessine une ligne pointillée. la longueur des tirets
                est le double de la longueur des trous.
                Pour plus de détails voir le pramètre nommé dash"""
                l=self.create_line(p.x,p.y,q.x,q.y,fill=couleur,dash=(2,))
                self.grid()
                return l
        
        def draw_rectangle(self,p,q,couleur):
                """ dessine un rectangle de diagonale pq
                dont les côtés sont parallèles aux bords de la fenêtre"""
                r=self.create_rectangle(p.x,p.y,q.x,q.y,outline=couleur)
                self.grid()
                return r
        
        def draw_fill_rectangle(self,p,q,couleur):
                """ dessine un rectangle plein de diagonale pq
                dont les côtés sont parallèles aux bords de la fenêtre"""
                r=self.create_rectangle(p.x,p.y,q.x,q.y,outline=couleur,fill=couleur)
                self.grid()
                return r

        def draw_triangle(self,p,q,r,couleur):
                """ dessine un triangle de sommets p, q et r """
                t=self.create_polygon(p.x,p.y,q.x,q.y,r.x,r.y,outline=couleur)
                self.grid()
                return t

        def draw_fill_triangle(self,p,q,r,couleur):
                """ dessine un triangle plein pqr avec la couleur donnée """
                t=self.create_polygon(p.x,p.y,q.x,q.y,r.x,r.y,outline=couleur,fill=couleur)
                self.grid()
                return t

        def draw_circle(self,p,r,couleur):
                """ dessine un cercle de centre p et de rayon r avec la couleur donnée """
                c=self.create_oval(p.x-r,p.y-r,p.x+r,p.y+r,outline=couleur)
                self.grid()
                return c
        
        def draw_fill_circle(self,p,r,couleur):
                """ dessine un cercle plein de centre p et de rayon r avec la couleur donnée """
                c=self.create_oval(p.x-r,p.y+r,p.x+r,p.y-r,outline=couleur,fill=couleur)
                self.grid()
                return c
        
        def draw_arc(self,p,r,angle_debut,angle_fin,couleur,style="arc"):
                """dessine un arc de cercle de centre p, de rayon r, angle_debut et angle_fin en degrés"""
                Monstyle={"arc":tkinter.ARC,"corde":tkinter.CHORD,"tarte":tkinter.PIESLICE,}
                a=self.create_arc(p.x-r,p.y-r,p.x+r,p.y+r,\
                start=angle_debut,extent=angle_fin,outline=couleur,\
                style=Monstyle[style])
                self.grid()
                return a
        
        def draw_fill_arc(self,p,r,angle_debut,angle_fin,couleur,style="tarte"):
                """dessine un arc de cercle de centre p, de rayon r, angle_debut et angle_fin en degrés"""
                Monstyle={"tarte":tkinter.PIESLICE,"corde":tkinter.CHORD}
                a=self.create_arc(p.x-r,p.y-r,p.x+r,p.y+r,\
                start=angle_debut,extent=angle_fin,\
                outline=couleur,fill=couleur,\
                style=Monstyle[style])
                self.grid()
                return a
        def aff_texte(self,texte,p,taille=20,police='Times',couleur='black',souligne = 'N',gras='N',italique='N'):
                """affiche un texte centré sur le point p """
                if souligne == 'Y':
                        souligne = 'underline'
                else :
                        souligne = 'normal'
                if gras == 'Y':
                        gras = 'bold'
                else :
                        gras = 'normal'
                if italique == 'Y':
                        italique = 'italic'
                else :
                        italique = 'normal'
                style = (police,taille, souligne,italique,gras)
                t=self.create_text(p.x,p.y,text=texte,font=style,fill=couleur)
                return t

        def efface(self,figure):
                """ efface la forme graphique i"""
                self.delete(figure)

        def efface_tout(self):
                """efface tous les objets graphiques de l'écran"""
                self.delete(ALL)



if __name__=="__main__":
        pass
        
