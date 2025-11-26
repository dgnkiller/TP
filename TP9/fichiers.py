def ligne(name:str)->list[str]:
    """ renvoie la liste des ligne du ficher name

    Précondition :
    Exemple(s) :
    $$$ 
    """
    f= open(name,'r')
    lignes_lues= f.readlines()
    return lignes_lues

def est_dans_liste(mot:str,liste:list)->bool:
    """ renvoie True ss’il existe un élément de la liste qui contient mot

    Précondition :
    Exemple(s) :
    $$$ est_dans_liste('cha',['chat','pacha'])
    True
    $$$ est_dans_liste('cha',['mangue','passe'])
    False
    """
    i=0
    res=False
    while i < len(liste) and not res:
        if mot in liste[i]:
            res=True
        i+=1
    return res
    
def est_dans_fichier(name:str,mot:str)->bool:
    """ renvoie True ss’il existe
        une ligne dans le fichier qui contient mot

    Précondition :
    Exemple(s) :
    $$$ 
    """
    l=ligne(name)
    return est_dans_liste(mot,l)



def ajout_fichier(ref:str,qte:int,prix:float,name:str):
    """ ajoute la ligne ref;qte;prix au fichier name 

    Précondition :
    Exemple(s) :
    $$$ 
    """
    liste=[ref,str(qte),str(prix)]
    ligne=';'.join(liste)+'\n'
    
    f=open(name,'a')
    f.write(ligne)
    f.close()
    
      