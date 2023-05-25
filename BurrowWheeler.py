#--------------------------------------------------------------------------------------------------------------------
#                                       Implémentation de Burrow-Wheeler
#--------------------------------------------------------------------------------------------------------------------

"""
L'algorithme de recherche de motifs avec la transformation de Burrows-Wheeler (BWT) est basé sur la propriété selon
laquelle les caractères identiques sont regroupés dans la dernière colonne de la matrice triée. Elle utilise le même
prétraitement que la compression de Burrow Wheeler.

L'algorithme de recherche de motifs avec la transformation de Burrows-Wheeler peut être une méthode efficace pour
la recherche de motifs dans un texte. Cependant, il nécessite la préparation préalable de la transformation de
Burrows-Wheeler, qui peut être coûteuse en termes de temps et de mémoire.

Pour en savoir plus allez voir ce document : https://pdfs.semanticscholar.org/03ba/de7ab5a6ff7a007780d0a366a946bd640868.pdf
"""

#--------------------------------------------------------------------------------------------------------------------
#                                            SOUS FONCTIONS
#--------------------------------------------------------------------------------------------------------------------

# Give all the rotations in a text
def rotations(text):
    textX2 = (text + "$") * 2
    res = []
    tailleText = len(text)
    for i in range (len(text) +1) :
        res += [textX2[i:i+tailleText+1]]
    return res
#-------------------------TESTS-------------------------
#print(rotations("Mila"))
#['Mila$', 'ila$M', 'la$Mi', 'a$Mil', '$Mila']


#print(rotations("CECIESTUNTEST"))
#['CECIESTUNTEST$', 'ECIESTUNTEST$C', 'CIESTUNTEST$CE', 'IESTUNTEST$CEC', 'ESTUNTEST$CECI', 'STUNTEST$CECIE', 'TUNTEST$CECIES', 'UNTEST$CECIEST', 'NTEST$CECIESTU', 'TEST$CECIESTUN', 'EST$CECIESTUNT', 'ST$CECIESTUNTE', 'T$CECIESTUNTES', '$CECIESTUNTEST']







def tri(text) :
    return sorted(rotations(text.upper()))

#-------------------------TESTS-------------------------
#print(tri("Mila"))
#['$MILA', 'A$MIL', 'ILA$M', 'LA$MI', 'MILA$']

#print(tri("Bonbon"))
#['$BONBON', 'BON$BON', 'BONBON$', 'N$BONBO', 'NBON$BO', 'ON$BONB', 'ONBON$B']

#print(tri("AAA"))
#['$AAA', 'A$AA', 'AA$A', 'AAA$']










def recup_derniers(text):
    res = ""
    for rotation in tri(text):
        res = rotation[-1] + res #prend le dernier charactere d'une chaine
    return res

#-------------------------TESTS-------------------------
#print(recup_derniers("Mila"))
#$IMLA
#print(recup_derniers("Etre ou ne pas etre telle est la queston des plus grands etres de cette planete"))
#LQOEEEES ETSEEEUDAETTTG     TA AOPELP  C  $NU DRTTRTNRLDN   PLRLEEASEEEUTSSSENSE







def affiche(text):
    res = []
    for rotation in tri(text):
        res += [[rotation[-1], rotation[0:len(rotation)-1]]]
    return res

#-------------------------TESTS-------------------------
#print(affiche("Mila"))
#[['A', '$MIL'], ['L', 'A$MI'], ['M', 'ILA$'], ['I', 'LA$M'], ['$', 'MILA']]









def tableau_occurence(text):
    res = {}
    for lettre in recup_derniers(text):
        if (not lettre in res):
            res[lettre] = 1
        else :
            res[lettre] = res[lettre] + 1

    return res
#-------------------------TESTS-------------------------

#print(tableau_occurence("MilaMiMila"))
#{'A': 2, 'L': 2, 'M': 3, 'I': 3, '$': 1}








def suffix_array(string):
    return(list(sorted(range(len(string)), key=lambda i:string[i:])))

#-------------------------TESTS-------------------------
#print(suffix_array("apple"))
#[0, 4, 3, 2, 1]






def bwt_from_suffix(string):
    #On recupere le suffixe array
    s_array = suffix_array(string)
    # on init le resultat
    res = ""
    # on recupere chaque lettre correspondante
    for i in s_array:
       res = res + string[i-1]
    return res

#-------------------------TESTS-------------------------

#print(bwt_from_suffix('apple'))
# elppa








def lf_mapping(bwt):

    alphabet = set(bwt) # recupere l'alphabet
    res = {} # initialisation du resultat

    # Mise à 0 pour toutes les lettres
    for letter in alphabet :
        res[letter] = [0]

    # on met la premiere lettre à 1 car elle est dans le premier suffixe
    res[bwt[0]] = [1]

    # on boucle sur les lettres du mot hors première lettre
    for letter in bwt[1:]:
        #pour chaque suffixe et chaque lettre on compte le nb d'occurence de la lettre
        for lettre, tabLettre in res.items():
            tabLettre.append(tabLettre[-1] + (lettre == letter))
    return (res)

#-------------------------TESTS-------------------------

#print(lf_mapping('apple'))
#{'e': [0, 0, 0, 0, 1],   -- il y a un e que dans le plus long suffixe
# 'l': [0, 0, 0, 1, 1],
# 'a': [1, 1, 1, 1, 1],
# 'p': [0, 1, 2, 2, 2]}   -- il y a un a dans tout les suffixes
# a ap app appl appla


# Counter est une bibliotheque qui va nous etre tres utile car elle
# permet de compter le nombre d'aparition d'un objet très facilement
# Exemple
# List as argument to Counter
#words_list = ['Cat', 'Dog', 'Horse', 'Dog']
#counter = Counter(words_list)
#print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})
from collections import Counter


def count_occurences(string):

    #Initialisation du compteur et du resultat
    count = 0
    result = {}

    # recupération de l'alphabet
    alphabet = set(string)


    # init du compteur
    c = Counter(string)
    # Ex pour apple :Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})

    #Pour chaque lettre de l'alphabet on recuperer
    # le nombre d'occurences et on le met dans res
    for letter in sorted(alphabet):
        result[letter] = count
        count += c[letter]
    return result


#-------------------------TESTS-------------------------

#print(count_occurences("apple"))
#{‘a’: 0, ‘e’: 1, ‘l’: 2, ‘p’: 3}





def update(begin, end, letter, lf_map, counts):

    beginning = counts[letter] + lf_map[letter][begin - 1] + 1
    ending = counts[letter] + lf_map[letter][end]
    return (beginning, ending)










def generate_all(input_string, eos="$"):

    letters = set(input_string) # recupere l'alphabet

    # si le marker de fin de chaine est dans le mot on l'enleve
    # et on refait l'alphabet
    if (eos in letters) :
        input_string = input_string.replace(eos, "")
        letters = set(input_string)

    # On recupere le compteur d'occurence
    counts = count_occurences(input_string)

    # on remet le caractere de fin
    # exemple avec apple : apple -> apple$
    input_string = "".join([input_string, eos])

    #on recupere le suffixe array
    s_array = suffix_array(input_string)

    # on recupere la dernierecolonne
    bwt = bwt_from_suffix(input_string)

    # on recupere le lf mapping
    lf_map = lf_mapping(bwt)

    # on repete le dernier element et on rajoute un zero a la fin de chaque ligne
    # exemple avec apple :
    # {'p': [0, 0, 0, 1, 2, 2], 'a': [0, 0, 0, 0, 0, 1], ....}
    # {'p': [0, 0, 0, 1, 2, 2, 2, 0], 'a': [0, 0, 0, 0, 0, 1, 1, 0], ...}
    #
    for i, j in lf_map.items():
        j.extend([j[-1], 0])

    return letters, bwt, lf_map, counts, s_array

#-------------------------TESTS-------------------------

#print(generate_all("apple", eos="$"))
#({'p', 'l', 'e', 'a'},
# 'e$lppa',
# {'p': [0, 0, 0, 1, 2, 2, 2, 0],
#   'a': [0, 0, 0, 0, 0, 1, 1, 0],
#   'l': [0, 0, 1, 1, 1, 1, 1, 0],
#   'e': [1, 1, 1, 1, 1, 1, 1, 0],
#   '$': [0, 1, 1, 1, 1, 1, 1, 0]},
# {'a': 0, 'e': 1, 'l': 2, 'p': 3},
# [5, 0, 4, 3, 2, 1])




def find_without_pretraitement (search_string, input_string,  letters, bwt, lf_map, count, s_array ):
    # initialisation du tableau resultat
    results = []

    # Nous ajoutons la class fuzzy qui va nous simplifier la suite
    class Fuzzy(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    fuz = [Fuzzy(search_string=search_string, begin=0, end=len(bwt) - 1)]

    while len(fuz) > 0:

        # enleve le dernier element et le récupere
        p = fuz.pop()
        # prend le patern sans la derniere lettre
        search_string = p.search_string[:-1]

        # prend la derniere lettre du pattern
        last = p.search_string[-1]

        letter = last

        # recalcul de l'intervale de recherche
        begin, end = update(p.begin, p.end, letter, lf_map, count)

        # verifie qu'on n'a pas dépasser
        if begin <= end:

            if len(search_string) == 0:
                # on a finit on recupere le resultat
                results.extend(s_array[begin: end + 1])
            else:
                # on a trouvé on ajoute au fuzzy
                fuz.append(Fuzzy(search_string=search_string, begin=begin, end=end))

    return sorted(set(results))


#--------------------------------------------------------------------------------------------------------------------
#                                            FONCTION PRINCIPALE
#--------------------------------------------------------------------------------------------------------------------


def find(search_string, input_string):

    #initialisation du tableau resultat
    results = []

    # gestion d'un pattern vide
    if len(search_string) == 0:
        return("Vous recherchez un pattern vide")


    # recup de tout les prétraitements
    bwt_data = generate_all(input_string)
    letters, bwt, lf_map, count, s_array = bwt_data

    # Gestion d'un texte vide
    if len(letters) == 0:
        return("Vous cherchez dans une chaine vide ")

    # gestion d'une recherche ou toutes les lettre du pattern ne sont pas dans le texte
    if not set(search_string) <= letters:
        return []


    # Nous ajoutons la class fuzzy qui va nous simplifier la suite
    class Fuzzy(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    fuz = [Fuzzy(search_string=search_string, begin=0, end=len(bwt) - 1)]

    while len(fuz) > 0:

        # enleve le dernier element et le récupere
        p = fuz.pop()
        # prend le patern sans la derniere lettre
        search_string = p.search_string[:-1]

        # prend la derniere lettre du pattern
        last = p.search_string[-1]


        letter = last

        # recalcul de l'intervale de recherche
        begin, end = update(p.begin, p.end, letter, lf_map, count)

        # verifie qu'on n'a pas dépasser
        if begin <= end:

            if len(search_string) == 0:
                # on a finit on recupere le resultat
                results.extend(s_array[begin : end + 1])
            else:
                # on a trouvé on ajoute au fuzzy
                fuz.append(Fuzzy(search_string=search_string, begin=begin,end=end))

    return sorted(set(results))


#print(find("app", 'applehvuapvgvappleple'))
# [0, 13]
#print(find("p", 'niednionpnfppapabep ahehdapfpapa aeh ha pdh fap'))
# [8, 11, 12, 14, 18, 26, 28, 30, 40, 46]



"""Fonction qui pour renvoit un tableau de tableau avec toutes les occurence de chaque ieme pattern dans le texte"""

def find_patterns_BW(texte, patterns):

    res = []
    # recup de tout les prétraitements
    bwt_data = generate_all(texte)
    letters, bwt, lf_map, count, s_array = bwt_data

    for i in range(0, len(patterns)):
        res += [find_without_pretraitement(patterns[i], texte, letters, bwt, lf_map, count, s_array)]
    return res

#print(find_patterns_BW("Ceci est un test, ce n'est pas le plus evident", ["test", "le", "t"]))
#[[12], [31], [7, 12, 15, 25, 45]]