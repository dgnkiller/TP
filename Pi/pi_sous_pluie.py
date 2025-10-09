import random
import math

def genere_point(v_max:int)->tuple[int|float,int|float]:
    """ renvoie les coordonnées d'un point placé aléatoirement
        dans un carré de coté v_max

    Précondition :\
    Exemple(s) :
    $$$
    """
    demi=v_max/2
    x=random.uniform(-demi,demi)
    y=random.uniform(-demi,demi)
    return (x,y)

def est_dans_cercle(point:tuple[int|float,int|float],r:int|float)->bool:
    """ Renvoie true si le point passé en parametre est dans le cercle de rayon r

    Précondition : r>0
    Exemple(s) :
    $$$ est_dans_cercle((3, 4), 5)
    True
    $$$ est_dans_cercle((6, 0), 5)
    False
    """
    (x,y)=point
    return abs(math.sqrt(x**2 + y**2))<=r

def generer_liste_points(n:int,v_max:int)->list[tuple[int|float, int|float, bool]]:
    """ renvoie une liste de triplets (a, y, dans_cercle représentant les points
    et leur appartenance au cercle

    Précondition :
    Exemple(s) :
    $$$
    """
    l=[]
    r= v_max/2
    for _ in range(n):
        x,y=genere_point(v_max)
        dans_cercle=est_dans_cercle((x,y),r)
        collabo=(x,y,dans_cercle)
        l.append(collabo)
    return l

def calcul_pi(liste_points:list[tuple[int|float, int|float, bool]])->float|int:
    """ renvoie la valeur de pi 

    Précondition :
    Exemple(s) :
    $$$ calcul_pi([(0,0,True), (1,1,True), (2,2,True)])
    approx(4)
    $$$ calcul_pi([(0,0,True), (5,5,False), (3,3,True), (6,6,False)])
    approx(2)
    """
    nbr_in_cercle=0
    
    for elmt in liste_points:
        x,y,z=elmt
        if z:
            nbr_in_cercle+=1
# compter les True dans le troisième élément de chaque triplet
# 
# diviser par le nombre total de points
# 
# multiplier par 4
    total_poiints=len(liste_points)
    return (nbr_in_cercle/total_poiints)*4







if __name__ == '__main__':
    print('** Estimer pi avec la pluie **')
    rayon=int(input('Donner le rayon du cercle : '))
    nbr_points=int(input('Donner le nombre de points à générer : '))
    liste=generer_liste_points(nbr_points,rayon*2)
    pi=calcul_pi(liste)
    res=f"La valeur de pi est estimée à {pi}"
    print(res)
    
    
    