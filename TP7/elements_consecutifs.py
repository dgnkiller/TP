# L1 MI S1 - Prog - ch 7 itérables et indexation
# Fichier support pour activité 
# oct 2024, revu oct 25


def mystere_7(liste: list[int]) -> list[int]:
    """ à_remplacer_par_ce_que_fait_la_fonction

     Précondition : /
    Exemple(s) :
    $$$ mystere_7([1, 2, 1, 2])
    []
    $$$ mystere_7([1, 1, 2, 1, 3, 3, 2, 2, 2, 2, 1])
    [1, 3, 2, 2, 2]
    $$$ mystere_7([])
    []
    $$$ mystere_7([1])
    []
    """
    res = []
    if len(liste) > 0:
        
        elem_prec = liste[0]
        for elem in liste[1:]:
            if elem == elem_prec: 
                res.append(elem)
            elem_prec = elem 
    return res
