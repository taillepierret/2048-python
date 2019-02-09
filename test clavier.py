from graphics.fenetres import *
from graphics.couleurs import *

f = Fenetre()
zg = f.graphique(largeur = 400,hauteur = 300)
p = Point(50,200)
zg.draw_pixel(p,vert)

def deplacement(event):
    """ déplacement d’une balle avec les touches du clavier """
    global p
    global c
    zg.efface(c)
    if event.keysym == 'Right':
        p.x += 5
    elif event.keysym == 'Left':
        p.x -= 5
    elif event.keysym == 'Up':
        p.y -= 5
    elif event.keysym == 'Down':
        p.y += 5
    c = zg.draw_fill_circle(p,10,rouge)
p=Point(300,300)
c = zg.draw_fill_circle(p,10,rouge)
zg.activer_clavier() #ligne à ne pas oublier
zg.bind('<Key>',deplacement)
zg.mainloop()
