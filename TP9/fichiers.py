def ligne_liste(name:str)->list[str]:
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
    l=ligne_liste(name)
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
    
def commande(name:str)->list[list]:
    """ renvoie une liste de liste représentant le contenu du fichie

    Précondition :
    Exemple(s) :
    $$$
    """
    l=[]
    with open(name,'r') as f:
        for ligne in f:
            new=ligne.strip()
            liste=new.split(';')
            ref=liste[0]
            qte=int(liste[1])
            prix=float(liste[2])
            l.append([ref,qte,prix])
            
    return l
            
def extraire_references(commandes:list[list])->list:
    """ renvoie la liste des references 

    Précondition : la liste qui represnte la commande doit etre
    constitue comme suit [[ref,qte,prix]...]
    Exemple(s) :
    $$$ extraire_references([['ref12a', 2, 2.50],['ref45', 1, 10.0],['ref99', 5, 1.20]])
    ['ref12a', 'ref45', 'ref99']
    """
    
    l=[]
    for elmt in commandes:
        l.append(elmt[0])
    return l
    
def est_ref_different(ref_list:list[str])->bool:
    """ renvoi true si toutes les ref de la liste sont differentes

    Précondition :
    Exemple(s) :
    $$$ est_ref_different(['ref12a', 'ref45', 'ref99'])
    True
    $$$ est_ref_different(['ref12', 'ref45', 'ref12'])
    False
    """
    n = len(ref_list)
    
    for i in range(n):
      
        for j in range(i + 1, n):
            if ref_list[i] == ref_list[j]:
                return False  
                
    return True
            
    
def est_ref_diff_in_commande(commandes:list[list])->bool:
    """renvoie true si toute les ref des contenue dans la commande sont differentes

    Précondition :
    Exemple(s) :
    $$$ est_ref_diff_in_commande([['ref12a', 2, 2.50],['ref45', 1, 10.0],['ref99', 5, 1.20]])
    True
    $$$ est_ref_diff_in_commande([['ref12a', 2, 2.50],['ref45', 1, 10.0],['ref12a', 5, 1.20]])
    False
    """
    liste_ref=extraire_references(commandes)
    return est_ref_different(liste_ref)


def calcul_montant(commandes:list[list])->float:
    """ renvoie le calcul du montant d'une commande

    Précondition :
    Exemple(s) :
    $$$ calcul_montant([["ref12a", 2, 2.50],["ref 45", 1, 10.0]])
    approx(15,0)
    $$$ calcul_montant([["stylo", 10, 1.20],["cahier", 2, 5.00],["sac", 1, 20.00]])
    approx(42,0)
    """
    total = 0
    
    for produit in commandes:
        qte = produit[1]
        prix = produit[2]
        total = total + (qte * prix)
        
    return total

def main():
    """ programme principal

    Précondition :
    Exemple(s) :
    $$$
    """
    name=input('Entrer le nom du fichier de la commande:')
    liste_commande=commande(name)
    if est_ref_diff_in_commande(liste_commande):
        montant=calcul_montant(liste_commande)
        print(f"Le montant de votre commande est de {montant}")
    else:
        print("Erreur : La commande contient des références en double (doublons).")
        print("Impossible de calculer le montant.")
    