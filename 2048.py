from random import randint
from graphics.fenetres import *
from graphics.couleurs import *

def init_grille():
    G=[]
    for i in range(4):
        G.append([0,0,0,0])
    return G

def rdm_2_4(G):
    T=[2,2,2,4] 
    nb=randint(0,3) #choose a number between 2 and 4
    l=randint (0,3) # choose randomly a line
    c=randint(0,3) #choose randomly a column
    while G[l][c] != 0: #find a case not equal to 0
        l=randint (0,3) # choose randomly a line
        c=randint(0,3) #choose randomly a column
    G[l][c]=T[nb]

def zero_to_the_left(G):
    for l in range (4):
        ZERO=[]
        for c in range (4):
            if G[l][c]==0:
                ZERO.append(c)
        nb_zero = len(ZERO)
        if nb_zero == 1 or nb_zero == 2 or nb_zero == 3:
            for plc in ZERO:
                for c in range (1,plc+1):
                    G[l][plc-c],G[l][plc-(c-1)] = G[l][plc-(c-1)],G[l][plc-c]
        
def right(G):
    """return 0 if there is no deplacement"""
    dep=0
    zero_to_the_left(G)
    for l in range (4):
        if G[l][3]==G[l][2]:
            G[l][3]=G[l][3]+G[l][2]
            G[l][2]=0
            dep+=1
        elif G[l][1]==G[l][2]:
            G[l][2]=G[l][1]+G[l][2]
            G[l][1]=0
            dep+=1
        elif G[l][1]==G[l][0]:
            G[l][1]=G[l][1]+G[l][0]
            G[l][0]=0
            dep+=1
    zero_to_the_left(G)
    return dep

def horizontal_mirror(G):
    for l in range (4):
        for c in range (2):
            G[l][c],G[l][3-c]=G[l][3-c],G[l][c]

def transp(G):
    for l in range (3):
        c=1
        while c<=3:
            G[l][c],G[c][l]=G[c][l],G[l][c]
            c+=1
        c+=1

        
def mv_left(G):
    """return 0 if there is no deplacement"""
    horizontal_mirror(G)
    dep=right(G)
    horizontal_mirror(G)
    return dep

def mv_right(G):
    """return 0 if there is no deplacement"""
    return right(G)
    
def mv_down(G):
    """return 0 if there is no deplacement"""
    transp(G)
    dep=right(G)
    transp(G)
    return dep

def mv_up(G):
    """return 0 if there is no deplacement"""
    transp(G)
    horizontal_mirror(G)
    dep=right(G)
    horizontal_mirror(G)
    transp(G)
    return dep

def win(G):
    """ return 1 if you win or return 0 if not yet"""
    for l in range(4):
        for c in range(4):
            if G[l][c]==2048:
                return 1
    return 0

def loose(G):
    """ return 1 if you loose or return 0 if not"""
    nb_zero=0
    for l in range(4):
        for c in range(4):
            if G[l][c]==0:
                nb_zero+=1
    if nb_zero==0:
        return 1
    return 0

def deplacement(G):
    """return 0 if there is no deplacement"""
    touche = 'e'
    while (touche != 'o') and (touche != 'l') and (touche != 'k') and (touche != 'm') and (touche != 'z') and (touche != 'q') and (touche != 's') and (touche != 'd'):
        touche = str(input("entre une touche esh"))
    if touche =='o' or touche =='z':
        dep=mv_up(G)
    elif touche == 'l'or touche =='s':
        dep=mv_down(G)
    elif touche == 'k'or touche =='q':
        dep=mv_left(G)
    elif touche == 'd'or touche =='m':
        dep=mv_right(G)
    return dep

def main():
    G=init_grille()
    rdm_2_4(G)
    rdm_2_4(G)
    print (G)
    while loose(G) ==0 and win(G)==0:
        dep=deplacement(G)
        if dep != 0:
            rdm_2_4(G)
        print (G)
        
main()
