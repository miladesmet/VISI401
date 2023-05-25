#--------------------------------------------------------------------------------------------------------------------
#                                       Implémentation de l'arbre des suffixes
#--------------------------------------------------------------------------------------------------------------------

"""L'algorithme des suffixes fonctionne en effectuant un prétraitement sur le texte et non pas sur le(s) pattern(s).

L'idée est de prendre tous les suffixes possibles d'un texte est de les "assembler" dans un abre binaire.

Dans ce cas si un schéma vaut mieux que mille mots, pour comprendre la construction et l'utilisation de cet arbre
je vous invite à visiter le document suivant : http://www-desir.lip6.fr/~herpsonc/uploads/Arbres-de-Suffixes-Suffix-Tree-Construction-Herpson2008.pdf

Cette méthode peut être assez lourde en termes de prétraitement si le texte est long, mais ce temps qui reste linéaire
est largement récompensé du fait qu'une foit que l'arbre est construit la recherche d'un pattern est d'une complexité
linéaire à la taille de ce pattern seulement, la taille du texte n'intervient donc plus dans la recherche.
"""

#--------------------------------------------------------------------------------------------------------------------
#                                            SOUS FONCTIONS
#--------------------------------------------------------------------------------------------------------------------

# Un noeud = {"lettres": "abb", "enfants": [Unnoeud, Unnoeud, Unnoeud]}

def create_noeud(lettres):
    return {"lettres": lettres , "enfants" : []}

#-----Test-----
b = create_noeud("b")
#print(b)
#{'lettres': 'b', 'enfants': []}

a = create_noeud("a")
#print(a)
#{'lettres': 'a', 'enfants': []}



def ajoute_enfant(noeudParent, noeudEnfant):
    noeudParent["enfants"].append(noeudEnfant)
    return noeudParent

#-----Test-----
ab = ajoute_enfant(a, b)
#print(ab);
#{'lettres': 'a', 'enfants': [{'lettres': 'b', 'enfants': []}]}



def creation_fin_arbre(chaine, pos):
    chaine_int = chaine

    petit_arbre = create_noeud(chaine[len(chaine)-1])
    ajoute_enfant(petit_arbre, pos)
    chaine_int = chaine[:len(chaine)-1]

    while(len(chaine_int) > 0 ):
        dernier_char = chaine_int[len(chaine_int)-1]
        chaine_int = chaine_int[:len(chaine_int) - 1]
        petit_arbre = ajoute_enfant(create_noeud(dernier_char), petit_arbre)

    return petit_arbre
#-----Test-----
mila = creation_fin_arbre("mila", 3)
#print(mila)
#{'lettres': 'm', 'enfants': [{'lettres': 'i', 'enfants': [{'lettres': 'l', 'enfants': [{'lettres': 'a', 'enfants': [3]}]}]}]}


def pos_lettre_dans_fils (noeud, lettre):
    enfants = noeud["enfants"]
    # Dans un premier temps on stocke dans une chaine de charactere toute les premieres lettres des enfants
    toute_lettre = ""
    for i in range(0, len(enfants)):
        enfant_actuel = enfants[i]
        if not isinstance(enfant_actuel, int) :
            lettres_actuelle = enfant_actuel['lettres']
            prem_lettre_actuelle = lettres_actuelle[0]
            toute_lettre = toute_lettre + prem_lettre_actuelle

    # On retourne la position de notre lettre dans la chaine de charactere crée soit le numéro de l'enfants ayant cette lettre
    return toute_lettre.find(lettre)
    # retournera -1 si aucun enfant à cette lettre

#-----Test-----
#print(pos_lettre_dans_fils(mila, 'i'))


def rattachement_suffixe_arbre (suffixe,pos, arbre) :

    # si on a déja placé tout notre suffixe
    if (len(suffixe) == 0 ):
        arbre = ajoute_enfant(arbre, pos)
        return arbre
    else :
        premier_lettre_suffixe = suffixe[0]

        pos_enfant_suiv = pos_lettre_dans_fils(arbre, premier_lettre_suffixe )
        # Si on a plus la suite
        if pos_enfant_suiv == -1 :
            arbre = ajoute_enfant(arbre, creation_fin_arbre(suffixe, pos))
            return arbre
        # Si on a la suite du moins la prochaine lettre
        else :
            arbre["enfants"][pos_enfant_suiv] = rattachement_suffixe_arbre(suffixe[1:], pos, arbre["enfants"][pos_enfant_suiv])
            return arbre

#----TEST----
lmila = ajoute_enfant(create_noeud(""), mila)

milaya = rattachement_suffixe_arbre ("milaya",1, lmila)
#print(milaya)
#{'lettres': '', 'enfants': [{'lettres': 'm', 'enfants': [{'lettres': 'i', 'enfants': [{'lettres': 'l', 'enfants': [{'lettres': 'a', 'enfants': [3, {'lettres': 'y', 'enfants': [{'lettres': 'a', 'enfants': [1]}]}]}]}]}]}]}



def creation_arbre(texte):
    arbre = create_noeud("")
    suffixe_actuel = texte
    compteur_pos = 0


    while (len(suffixe_actuel) > 0) :
        arbre = rattachement_suffixe_arbre (suffixe_actuel, compteur_pos, arbre)

        # on met a jour le suffixe d'apres et le compteur
        suffixe_actuel = suffixe_actuel[1 : len(suffixe_actuel)]
        compteur_pos = compteur_pos + 1

    return arbre

#----TEST----
banana = creation_arbre("banana")
#print(banana )
"""
{'lettres': '', 'enfants': 
[{'lettres': 'b', 'enfants': 
[{'lettres': 'a', 'enfants': 
[{'lettres': 'n', 'enfants': 
[{'lettres': 'a', 'enfants':
 [{'lettres': 'n', 'enfants':
 [{'lettres': 'a', 'enfants': [0]}]}]}]}]}]}, 
{'lettres': 'a', 'enfants': 
[{'lettres': 'n', 'enfants':
 [{'lettres': 'a', 'enfants': 
[{'lettres': 'n', 'enfants':
 [{'lettres': 'a', 'enfants': [1]}]}, 
3]}]},
 5]}, 
{'lettres': 'n', 'enfants': 
[{'lettres': 'a', 'enfants': 
[{'lettres': 'n', 'enfants':
 		[{'lettres': 'a', 'enfants': [2]}]},
 4]}]}]}"""

def est_feuille(arbre):
    enfants = arbre["enfants"]
    return len(enfants) == 1 & isinstance(enfants[0], int)

#print(est_feuille(mila))
# false
#print(est_feuille(creation_fin_arbre("a",2)))
# true

def a_un_seul_arbre_enfant(arbre):
    enfants = arbre["enfants"]
    return len(enfants) == 1 & (not isinstance(enfants[0], int))
#print(a_un_seul_arbre_enfant(mila))
# true
#print(a_un_seul_arbre_enfant(creation_fin_arbre("a",2)))
# false
#print(a_un_seul_arbre_enfant(banana))
# true


def compression(arbre):
    if est_feuille(arbre):
        return arbre
    else:
        if not a_un_seul_arbre_enfant(arbre):
            enfants = arbre["enfants"]
            copie_arbre = create_noeud(arbre["lettres"])
            for i in range(0, len(enfants)):
                if isinstance(enfants[i], int) :
                    copie_arbre = ajoute_enfant(copie_arbre, enfants[i])
                else :
                    copie_arbre = ajoute_enfant(copie_arbre,  compression(enfants[i]) )
            return copie_arbre
        else :
            arbre["enfants"][0]["lettres"] = arbre["lettres"] + arbre["enfants"][0]["lettres"]
            return compression(arbre["enfants"][0])

banana_compressed = compression(banana)
#print(banana_compressed)

# {'lettres': '', 'enfants': [{'lettres': 'banana', 'enfants': [0]}, {'lettres': 'a', 'enfants': [{'lettres': 'na', 'enfants': [{'lettres': 'na', 'enfants': [1]}, 3]}, 5]}, {'lettres': 'na', 'enfants': [{'lettres': 'na', 'enfants': [2]}, 4]}]}

def tout_pos_noeud (noeud) :
    enfants = noeud["enfants"]
    res = []
    for i in range(0, len(enfants)):
        if isinstance(enfants[i], int) :
            res.append(enfants[i])
        else :
            res = res +(tout_pos_noeud (enfants[i]))
    return res


#print(tout_pos_noeud(banana))

def nombre_lettres_communes(chaine1, chaine2):
    n = 0
    while n < min(len(chaine1), len(chaine2)) and chaine1[n] == chaine2[n]:
        n += 1
    return n



def pos_enfant_suiv_compressed(noeud, pattern) :
    enfants = noeud["enfants"]
    res = [-1, 0]
    for i in range(0, len(enfants)):
        enfant_actuel = enfants[i]
        if not isinstance(enfant_actuel, int):
            lettres_actuelle = enfant_actuel['lettres']
            if nombre_lettres_communes(lettres_actuelle, pattern) != 0 :
                res = [i, nombre_lettres_communes(lettres_actuelle, pattern)]
    return res

#print(pos_enfant_suiv_compressed(milaya, "mila"))
#print(pos_enfant_suiv_compressed(banana_compressed, "bana"))

def recherche (arbre, pattern):
    # si on a déja placé tout notre pattern
    #print("Je passe ")
   # print("Arbre = ")
    #print(arbre)
   # print("Pattern = ")
   # print(pattern)

    if (len(pattern) == 0):
        return tout_pos_noeud(arbre)
    else:
        pos_enfant_suiv = pos_enfant_suiv_compressed(arbre, pattern)
       # print(pos_enfant_suiv)
        # Si on a plus la suite
        if pos_enfant_suiv[0] == -1:
            return [-1]
        # Si on a la suite du moins la prochaine lettre
        else:
            return recherche(arbre["enfants"][pos_enfant_suiv[0]], pattern[pos_enfant_suiv[1]:len(pattern)])


#print(recherche(banana_compressed, "ana"))
#[1, 3]

#--------------------------------------------------------------------------------------------------------------------
#                                            FONCTIONs PRINCIPALEs
#--------------------------------------------------------------------------------------------------------------------

"""Fonction qui pour renvoit un tableau avec toutes les occurence du pattern dans le texte"""
def recherche_suffixe( texte, pattern) :
    arbre = creation_arbre(texte)
    arbre_compressed = compression(arbre)
    return recherche(arbre_compressed, pattern)

#print(recherche_suffixe( "Ceci est un test il y aura d'autres tests mais celui ci est le premier test", "test"))
#[12, 36, 71]
#print(recherche_suffixe( "Ceci est un test il y aura d'autres tests mais celui ci est le premier test", "le"))
#[60]


"""Fonction qui pour renvoit un tableau de tableau avec toutes les occurence de chaque ieme pattern dans le texte"""
def recherche_suffixes( texte, patterns) :
    arbre = creation_arbre(texte)
    arbre_compressed = compression(arbre)

    res = []

    for i in range(0, len(patterns)):
        res += [recherche(arbre_compressed, patterns[i])]
    return res


#print(recherche_suffixes( "Ceci est un test il y aura d'autres tests mais celui ci est le premier test", ["test", "le"]))
#[[12, 36, 71], [60]]