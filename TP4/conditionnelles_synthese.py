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
ELECTRIQUE_JOUR=100
ELECTRIQUE_KM=0.01
DIESEL_JOUR=60
DIESEL_KM=0.1
ESSENCE_JOUR=50
ESSENCE_KM=0.4

def cout_location(nb_jours:int, nb_km:int|float, energie:str)->int|float:
    """  renvoie le coût total de la location

    Précondition : aucune
    Exemple(s) :
    $$$ cout_location(1,400,'diesel')
    100
    $$$ cout_location(2,50,'essence')
    approx(120.5,1)
    $$$ cout_location(1,1000,'electrique')
    110
    """
    if energie=='electrique':
        prix_jour=ELECTRIQUE_JOUR
        prix_km=ELECTRIQUE_KM
    elif energie=='diesel':
        prix_jour=DIESEL_JOUR
        prix_km=DIESEL_KM
    else:
        prix_jour=ESSENCE_JOUR
        prix_km=ESSENCE_KM
    return (prix_jour*nb_jours)+(prix_km*nb_km)

# Décommenter et compléter la signature donnée puis faire la suite
def arg_minimum(a:int,b:int,c:int)->int:
    """ envoie 1 si 𝑎 est le plus petit
    des 3 nombres, 2 si c’est 𝑏 et 3 si c’est 𝑐 

    Précondition : /
    Exemple(s) :
    $$$ arg_minimum(2,6,9)
    1
    $$$ arg_minimum(4,-1,9)
    2
    $$$ arg_minimum(12,45,9)
    3
    """
    if a<b and a<c:
        res=1
    elif b<a and b<c:
        res=2
    else:
        res=3
    return res 

# Décommenter et compléter la signature donnée puis faire la suite
def conseil_voiture(nb_jours:int, nb_km)->str:
    """ renvoie 'electrique' si le véhicule électrique est le moins cher, 'diesel' si
    c’est le véhicule diesel ou 'essence' si c’est le véhicule à essence.

    Précondition :/
    Exemple(s) :
    $$$ conseil_voiture(1,400)
    'diesel'
    $$$ conseil_voiture(1,1000)
    'electrique'
    
    """
    prix_diesel=cout_location(nb_jours,nb_km,'diesel')
    prix_essence=cout_location(nb_jours,nb_km,'essence')
    prix_electrique=cout_location(nb_jours,nb_km,'electrique')
    
    meilleur_prix=arg_minimum(prix_diesel,prix_essence,prix_electrique)
    if meilleur_prix==1:
        res='diesel'
    elif meilleur_prix==2:
        res='essence'
    else:
        res='electrique'
    return res 
    
    
    

####################
# Impression à tarif dégressif
####################

# Décommenter et compléter la signature donnée puis faire la suite
def millier_sup(n:int)->int:
    """ renvoie l'arrondie de n au millier superieur

    Précondition : /
    Exemple(s) :
    $$$ millier_sup(2000)
    2000
    $$$ millier_sup(3100)
    4000
    $$$ millier_sup(12700)
    13000
    """
    if n%1000==0:
        res= n
    else:
        res=((n//1000)+1)*1000
    return res


def nombre_exemplaires(nb_flyers:int)->int:
    """ envoie le
    nombre d’exemplaires qui seront réellement commandé

    Précondition :
    Exemple(s) :
    $$$ nombre_exemplaires(400)
    500
    $$$ nombre_exemplaires(500)
    500
    $$$ nombre_exemplaires(2540)
    3000
    $$$ nombre_exemplaires(5000)
    5000
    """
    if nb_flyers < 100:
        res=100
    elif nb_flyers>=101 and nb_flyers<=500:
        res=500
    elif nb_flyers>=501 and nb_flyers<=1000:
        res=1000
    else:
        res=millier_sup(nb_flyers)
    return res
        

# Décommenter et compléter la signature donnée puis faire la suite
def montant_facture(nb_flyers:int)->int|float:
    """ renvoie le prix à payer pour ces flyer

    Précondition :
    Exemple(s) :
    $$$ montant_facture(400)
    approx(45,1)
    $$$ montant_facture(56)
    approx(30,1)
    montant_facture(679)
    approix(50,1)
    
    
    """
    total_flyers= nombre_exemplaires(nb_flyers)
    if total_flyers == 100:
        prix_unit=0.30
    elif total_flyers==500:
        prix_unit=0.09
    elif total_flyers==1000:
        prix_unit=0.05
    else:
        prix_unit=0.03
    return total_flyers*prix_unit

####################
# Roulette
####################
    #def calcul_gain(bille, pari, mise

