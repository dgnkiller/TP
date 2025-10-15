# L1 MI S1 - Prog - ch 7 itérables et indexation
# Fichier support pour activité boucles imbriquées
# oct 2024

def calcule_produit_cartesien1(liste:list[int], chaine:str) -> list[str]:
    """Renvoie une liste composée de l'association des éléments de la liste avec ceux de la chaine

    Précondition : /
    """
    res = []
    for entier in liste:
        for carac in chaine:
            res.append(str(entier) + carac)
    return res

def calcule_produit_cartesien2(liste : list[int], chaine : str ) -> list[str]:
    """Renvoie une liste composée de l'association des éléments de la liste avec ceux de la chaine

    Précondition : / 
    """
    res = []
    for carac in chaine:
        for entier in liste:
            res.append(str(entier) + carac)
    return res

        
