# Compléter ici (noms, groupe, contenu fichier, date)
# DJEGNON Yves
#GP12
#PROG TP8
#22/10/2025
# Ne pas supprimer cette ligne. <trace>range.py</trace>

# Décommenter et compléter la signature donnée puis faire la suite
def compte_motif(motif:str,chaine:str)->int:
    """ envoie le nombre d’occurrences de motif dans texte

    Précondition :/ 
    Exemple(s) :
    $$$ compte_motif('la', 'la vitre est sale, lave-la vite')
    3
    $$$ compte_motif('te', 'la vitre est sale, lave-la vite')
    1
    $$$ compte_motif('politesse', 'la vitre est sale, lave-la vite')
    0
    """
    res=0
    lg=len(motif)
    for i in range(len(chaine)):
        if chaine[i:i+lg]==motif:
            res=res+1
    return res
    
    

# Décommenter et compléter la signature donnée puis faire la suite
def indice_maximum(liste:list[int])->int:
    """ renvoie l’indice du maximum d’une liste d’entiers non vide et tous différents.

    Précondition : /
    Exemple(s) :
    $$$ indice_maximum([-12, 3, 0])
    1
    """
    res=0
    l=liste[0]
    for i in range(1, len(liste)):
        if liste[i]>l:
            res=res+i
            l=liste[i]
    return res
    

# Décommenter et compléter la signature donnée puis faire la suite
def moyenne_ponderee(lnotes:list[int], lcoeff:list[int])->int:
    """ envoie la moyenne pondérée des notes par ces coefficients

    Précondition : /
    Exemple(s) :
    $$$ moyenne_ponderee([12, 15, 20], [1, 2, 3])
    17
    """
    l=0
    for i in range(len(lnotes)):
        res=(lnotes[i]*lcoeff[i]//sum(lcoeff))
        l=l+res
    return l
        
    

#################
### Addition binaire
#################
# Décommenter et compléter la signature donnée puis faire la suite
def addition_digit(digit1:str, digit2:str, retenue:str)->tuple:
    """ renvoie le couple (retenue, unité) résultant de leur addition

    Précondition : /
    Exemple(s) :
    $$$ addition_digit('1', '1', '0')
    ('1', '0')
    """
    s=int(digit1)+int(digit2)+int(retenue)
    if s==0 or s==2:
        unite=0
    else:
        unite=1
    if s>0 and s!=1:
        retenue=1
    else:
        retenue=0
    return (str(retenue),str(unite))
    

# Décommenter et compléter la signature donnée puis faire la suite
def addition(ch1:str, ch2:str)->str:
    """ envoie la  somme des parametres en binaire
    Précondition :/ 
    Exemple(s) :
    $$$ addition('0011', '1110')
    '10001'
    """
    res=''
    retenue=0
    for i in range(-1, -len(ch1)-1, -1):
        retenue,unite =addition_digit(ch1[i], ch2[i], retenue)
        res=unite + res
    res=retenue + res
    return res    

#################
## Plutôt parcours en parallèle ou plutôt for imbriqués ?
#################

# Décommenter et compléter la signature donnée puis faire la suite
def determine(lmots:list[str], ldeterminants:list[str])->list[str]:
    """ envoie les listes des compositions possibles, séparées par une espace.

    Précondition : /
    Exemple(s) :
    $$$ determine(['mot', 'chat', 'verre'], ['le', 'un'])
    ['le mot', 'un mot', 'le chat', 'un chat', 'le verre', 'un verre'] 
    """
    res=[]
    sh=''
    for i in lmots:
        for det in ldeterminants:
            sh=sh+det+' '+i
            res.append(sh)
            sh=''
    return res
    

# Décommenter et compléter la signature donnée puis faire la suite
def supprime(lchaines:list[str], carac:str)->list[str]:
    """ renvoie une nouvelle liste dans laquelle les occurrences du caractère ont été supprimées des chaînes

    Précondition : /
    Exemple(s) :
    $$$ supprime(['le', 'chat', 'miaule'], 'a')
    ['le', 'cht', 'miule']
    """
    res=[]
    sh=''
    for elem in lchaines:
        
        for i in elem:
            if i!=carac:
                sh=sh+i
        res.append(sh)
        sh=''
    return res
    
                
    

# Décommenter et compléter la signature donnée puis faire la suite
def filtre(liste:list[int], lvrai:bool)->list[int]:
    """envoie une nouvelle liste ne gardant que les entiers correspondant à un booléen valant True.

    Précondition : /
    Exemple(s) :
    $$$ filtre([1, 2, 4], [True, False, True])
    [1, 4]
    """
    res=[]
    for i in range(len(liste)):
        if lvrai[i]:
            res.append(liste[i])
    return res
    

