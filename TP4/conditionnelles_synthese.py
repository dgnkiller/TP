# Compléter ici (noms, groupe, contenu fichier, date)
# DJEGNON Yves
# MI 12
# TP4
# 25/09/2025
# Ne pas supprimer cette ligne. <trace>conditionnelles_synthese.py</trace>

####################
# Exercices de synthèse
####################

####################
# Location
####################

# Décommenter et compléter la signature donnée puis faire la suite

ELECTRIQUE_j = 100  
ELECTRIQUE_KM= 0.01
DIESEL_j= 60 
DIESEL_KM= 0.1
ESSENCE_j= 50 
ESSENCE_KM= 0.4

def cout_location(nb_jours:int, nb_km:int, energie:str)->int:
    """ renvoie le cout total de la location 
    
        Précondition : nb_jours>= 0 et nb_km>=0
        Exemple(s) :
        >>> round(cout_location(2,50,'diesel'),1)
        125
        >>> round(cout_location(1,400,'essence'),1)
        210
        >>> round(cout_location(1,1000,'electrique'),1)
        110 
        """    
    if energie== 'electrique':
        prix_jour= ELECTRIQUE_j
        prix_km=ELECTRIQUE_KM
    elif energie=='diesel':
        prix_jour=DIESEL_j
        prix_km=DIESEL_KM
    else:
        prix_jour=ESSENCE_j
        prix_km=ESSENCE_KM
    return  (nb_jours*prix_jour)+(nb_km*prix_km)
        
# Décommenter et compléter la signature donnée puis faire la suite
def arg_minimum(a:int,b:int,c:int)->int:
    """ renvoie 1,2 ou 3 sirepectivement a,b,cest le plus petit des 3 nbr
    
        Précondition : aucune
        Exemple(s) :
        >>> arg_minimum(12,34,9)
        3
        >>> arg_minimum(-1,4,9)
        1
        >>> arg_minimum(19,4,9)
        2
        """    
    if a<b and a<c:
        res=1
    elif b<a and b<c:
        res=2
    else:
        res=3
    return res
# Décommenter et compléter la signature donnée puis faire la suite
#def conseil_voiture(nb_jours, nb_km):
    """
    
        Précondition :
        Exemple(s) :
        >>>
"""


####################
# Impression à tarif dégressif
####################

# Décommenter et compléter la signature donnée puis faire la suite
#def nombre_exemplaires

# Décommenter et compléter la signature donnée puis faire la suite
#def montant_facture

####################
# Roulette
####################

#def calcul_gain(bille, pari, mise
