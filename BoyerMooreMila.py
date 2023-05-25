#--------------------------------------------------------------------------------------------------------------------
#                                       Implémentation de l'algo naïf
#--------------------------------------------------------------------------------------------------------------------

"""L'algorithme de Boyer-Moore
Il utilise une heuristique basée sur les caractères du motif pour effectuer des sauts lors de la recherche,
ce qui réduit le nombre de comparaisons nécessaires.

L'idée derrière cet algo est de créer deux tableaux lors d'un prétraitement sur le texte.

Le tableau de décalage des caractères (bad character shift) indique la distance à laquelle un caractère dans le motif
peut être décalé lors d'un mismatch. Le tableau de décalage de préfixe (good suffix shift) indique la distance maximale
par laquelle le motif peut être décalé en cas de correspondance partielle.

Ces deux tableaux nous permettrons suivant le cas de mismatch de décaler le pattern de la distance la plus grande
possible lors d'un mismatch ou d'un find et donc de limiter grandement le nombre d'opérations inutiles.

Par exemple si nous avons trouvé le pattern nous pouvons décaler la fenêtre de comparaison vers la gauche en utilisant
le tableau de décalage de préfixe pour trouver la plus grande correspondance possible et donc éviter de comparer des
caractères dont nous savons déja s'ils sont égaux ou non.

De la même manière si nous avons un mismatch au tout début nous utilisons le tableau de décalage des caractères pour
sauter les caractères qui ne peuvent pas correspondre.

Dans le cas d'un mismatch en cours de mot, nous utilisons le tableau de décalage des caractères, cela nous permet
d'aligner le caractère du texte en comparaison avec la dernière occurrence correspondante dans le pattern.

Pour en savoir plus sur l'algorithme de Boyer-Moore, vous pouvez consulter cette page :
https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore
"""


#--------------------------------------------------------------------------------------------------------------------
#                                               SOUS FONCTION
#--------------------------------------------------------------------------------------------------------------------


"""Fonction qui permet de traduire une lettre en son index dans l'alphabet"""

def alphabet_index(alphabet, letter):
    val1 = alphabet.find(letter.upper())
    val2 = alphabet.find(letter.lower())
    if val1 > val2 :
        val = val1
    else :
        val = val2
    return val

#-------------------------TESTS-------------------------

#print(alphabet_index("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'A'))
# 0
#print( alphabet_index("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'c'))
#2
#print( alphabet_index("GCTB", 'B'))
#3


"""Fonction qui calcul la table suivant la regle du mauvais caractere"""
def table_bad_character(pattern, alphabet):
    ALPHABET_SIZE = len(alphabet)


    if (len(pattern) != 0 ) :
        R = [[-1] for a in range(ALPHABET_SIZE)] # le tableau de résultat
        alpha = [-1] * ALPHABET_SIZE # zone de memoire pour eviter de parcourir un trop grand nombre de fois le pattern

        # On parcours le pattern
        for i in range(len(pattern)):
            lettre = pattern[i]
            alpha[alphabet_index(alphabet, lettre)] = i # on inscrit la derniere occurence de chaque lettre
                                             # a sa position dans l'alphabet dans la zone memoire


            #on parcours un alpha
            for j in range(ALPHABET_SIZE):
                der_occ = alpha[j]
                R[j].append(der_occ)
                # on stocke les résultats intermédiaire dans R pour savoir la derniere
                # occurence de chaque caractere pour chaque position


        return R
    else :
        return [[]] * ALPHABET_SIZE# le tableau de résultat dans le cas ou le pattrn est vide

#-------------------------TESTS-------------------------

#print("table de mauvais charactere ABRACADABRA avec alphabet classique : ")
#print(table_bad_character ("ABRACADABRA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
#[[-1, 0, 0, 0, 3, 3, 5, 5, 7, 7, 7, 10], [-1, -1, 1, 1, 1, 1, 1, 1, 1, 8, 8, 8], [-1, -1, -1, -1, -1, 4, 4, 4, 4, 4, 4, 4], [-1, -1, -1, -1, -1, -1, -1, 6, 6, 6, 6, 6], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, 2, 2, 2, 2, 2, 2, 2, 9, 9], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

#print("table de mauvais charactere ABRACADABRA avec alphabet ABCDR : ")
#print(table_bad_character ("ABRACADABRA", "ABCDR"))
#[[-1, 0, 0, 0, 3, 3, 5, 5, 7, 7, 7, 10],
#[-1, -1, 1, 1, 1, 1, 1, 1, 1, 8, 8, 8],
#[-1, -1, -1, -1, -1, 4, 4, 4, 4, 4, 4, 4],
#[-1, -1, -1, -1, -1, -1, -1, 6, 6, 6, 6, 6],
#[-1, -1, -1, 2, 2, 2, 2, 2, 2, 2, 9, 9]]

#print("table de mauvais charactere ABACDE avec alphabet ABCDE : ")
#print(table_bad_character ("ABACDE", "ABCDE"))
#[[-1, 0, 0, 2, 2, 2, 2],
 #[-1, -1, 1, 1, 1, 1, 1],
 #[-1, -1, -1, -1, 3, 3, 3],
 #[-1, -1, -1, -1, -1, 4, 4],
 #[-1, -1, -1, -1, -1, -1, 5]]


"""Fonction qui cree une table qui indique les longueurs des plus grands suffixes commun entre Pattern[:i] et Pattern """

def longueurs_suffixes_communs(pattern):
    len_pattern = len(pattern)
    suffixe_D = len_pattern - 1 #index utilisé pour suivre l'extrémité droite du plus grand suffixe commun courant.

    res = [0] * len_pattern # on crée le tableau resultat
    res[len_pattern - 1] = len_pattern # on replis la derniere place car forcement le pattern vaut le pattern

    for i in range(len_pattern - 2, -1, -1):

        #vérifie si P[i:] se chevauche avec le plus grand suffixe commun courant
        if i > suffixe_D and res[i + len_pattern - 1 - f] != i - suffixe_D:
            #la longueur minimale entre la longueur du chevauchement et la longueur du plus grand suffixe commun courant.
            res[i] = min(res[i + len_pattern - 1 - f], i - suffixe_D)
        else:
            suffixe_D = min(i, suffixe_D)

            f = i # stocker l'indice correspondant à la fin de la sous-chaîne P[i:]


            #tant que les lettres correspondent on essaye encore une lettre
            while suffixe_D >= 0 and pattern[suffixe_D] == pattern[suffixe_D + len_pattern - 1 - f]:
                suffixe_D = suffixe_D - 1

            # quand ca s'est arreter c'est quon a trouver le bord du bon suffixe
            # on met la longueure du bon suffixe dans le tableau resultat
            res[i] = f - suffixe_D
    return res

#-------------------------TESTS-------------------------


#print(longueurs_suffixes_communs("ABRACADABRA"))
#[1, 0, 0, 4, 0, 1, 0, 1, 0, 0, 11]

#print(longueurs_suffixes_communs("TEST"))
#[1, 0, 0, 4]

#print(longueurs_suffixes_communs("aababa"))
#[1, 1, 0, 3, 0, 6]



""" Fonction qui renvoie un tableau avec les decalages du à la regle des bons suffixe"""
def table_bons_suffixes(pattern):

    len_pattern = len(pattern)

    lsc = longueurs_suffixes_communs(pattern)

    # initialisation de la table resultat
    res = [len_pattern] * len_pattern

    i = 0
    for j in range(len_pattern - 1, -1, -1):
        if lsc[j] == j + 1: # soit P[j+1:] est un suffixe de P.
            while i < len_pattern - 1 - j:
                if res[i] == len_pattern:   # signifie qu'il n'est pas encore à jour
                    res[i] = len_pattern - 1 - j
                i = i + 1
    for j in range(0, len_pattern - 1):
        res[len_pattern - 1 - lsc[j]] = len_pattern - 1 - j
    return res


#--------------------------------------------------------------------------------------------------------------------
#                                            FONCTION PRINCIPALE
#--------------------------------------------------------------------------------------------------------------------

"""Fonction qui renvoie les position auquelles sont trouvées le pattern dans le texte"""
def boyer_moore_search(texte, pattern, alphabet):

    #pretraitement
    table_bons_suff = table_bons_suffixes(pattern)
    table_mauvais_car = table_bad_character(pattern, alphabet )

    #init des variables
    len_Text = len(texte)
    len_P = len(pattern)

    #initialisation du resultat
    res = []
    j = 0 # on commence qu debut du texte

    while j <= len_Text - len_P: # soit tant que on a encore assez de place pour que le motif rentre
        i = len_P - 1 # on initialise le curseur de comparaison i
        while i >= 0 and (pattern[i].upper() == texte[i + j] or pattern[i].lower() == texte[i + j]): # tant que les caracteres correspondent
            i = i - 1 # on deplace le curseur à gauche
        if i < 0:# si on est sortie du while avec un i <0 c'est quon a trouvé une occurence
            res.append(j) # on l'ajoute au resultat
            j = j + table_bons_suff[0] # on se décale de ce qui faut
        else: # si on est srtie avant c'est qu'il y a eu un mismatch
            #on regarde qu'elle regle est plus avantageuse et on se décale
            j = j + max(table_bons_suff[i],
                        table_mauvais_car[alphabet_index(alphabet, texte[i + j])][i] - len_P + 1 + i)
    return res

#-------- TESTS -----------
#print(boyer_moore_search('Je suis un test je ne marche pas toujours mais je suis la ', "je", "abcdefghijklmnopqrstuvwxyz"))
#[0, 16, 47]