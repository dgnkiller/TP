# Compléter ici (noms, groupe, contenu fichier, date)
# DJEGNON Yves
# MI 12
# TP4
#
# Ne pas supprimer cette ligne. <trace>conditionnelles_simples.py</trace>


####################
# Des conditionnelles de toute sorte
####################

# Décommenter et compléter la signature donnée puis faire la suite
def maximum_sem4(x:int,y:int)-> int:
    """ renvoie le plus grand des parametres

    Précondition : aucune
    Exemple(s) :
    $$$ maximum_sem4(2,7)
    7
    $$$ maximum_sem4(3,1)
    3
    $$$ maximum_sem4(3,3)
    3
    """
    
    if x>y:
        res=x
    else:
        res=y
    return res

# Décommenter et compléter la signature donnée puis faire la suite
def compare_sem4(x:int, y:int)->int:
    """ renvoie -1 si x
est strictement inférieur à y, 1 si x est strictement supérieur à y et 0 si les 2 valeurs sont égale

    Précondition :
    Exemple(s) :
    $$$ compare_sem4(1,1)
    0
    $$$ compare_sem4(1,2)
    -1
    $$$ compare_sem4(2,1)
    1
    """
    if x<y:
        res=-1
    elif x>y:
        res= 1
    else:
        res=0
    return res

# Décommenter et compléter la signature donnée puis faire la suite
def minimum3_sem4(x:int,y:int,z:int)->int:
    """ renvoie le minimum des 3 parametres 

    Précondition :aucune
    Exemple(s) :
    $$$ minimum3_sem4(1,2,3)
    1
    $$$ minimum3_sem4(6,0,3)
    0
    $$$ minimum3_sem4(5,5,8)
    5
    """
    if x<=y and x<=z:
        res=x
    elif y<=x and y<=z:
        res=y
    else:
        res=z
    return res

# Décommenter et compléter la signature donnée puis faire la suite
ADMIS= 'ADM'
AJOURNE='AJ'
ENJAMB='AJAC'

def resultat_annee(BCC1_S1:bool, BCC2_S1:bool, BCC1_S2:bool, BCC2_S2:bool)->str:
    """ renvoie une chaîne qui peut être :
    • "ADM" dans le cas où les 4 BCC sont validés ou, à défaut,
    • "AJAC" dans le cas où les BCC1 des 2 semestres ont été validés, ou , à défaut,
    • une chaîne qui commence par "AJ", suivi d’un texte qui indique que les notes des BCC validés peuvent être
    conservées.

    Précondition : aucune
    Exemple(s) :
    $$$ resultat_annee(True, True, True, True)
    "ADM"
    $$$ resultat_annee(True, False, True, True)
    "AJAC"
    $$$ resultat_annee(False, False, False, False)
    "AJ"
    $$$ resultat_annee(True, False, False, False)
    "AJ\\nVous gardez votre note du BCC1 du S1"
    $$$ resultat_annee(True, False, False, True)
    ""'AJ\nVous gardez votre note du BCC1 du S1\nVous gardez votre note du BCC2 du S1'
    """
    texte= "\nVous gardez votre note du BCC"

    if BCC1_S1 and BCC2_S1 and BCC1_S2 and BCC2_S2 :
        res= ADMIS
    elif BCC1_S1 and BCC1_S2:
        res= ENJAMB
    else:
        res=AJOURNE
        if BCC1_S1:
            res= res + texte+ '1 du S1'
        if BCC2_S1:
            res=res+ texte+ '2 du S1'
        if BCC1_S2:
            res= res + texte + '1 du S1'
        if BCC2_S2:
            res= res + texte + '2 du S1'
    return res
        
        
    
        