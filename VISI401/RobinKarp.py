#--------------------------------------------------------------------------------------------------------------------
#                                       Implémentation de l'algo Rabin Karp
#--------------------------------------------------------------------------------------------------------------------

"""Similaire à la méthode naïve la méthode Rabin-Karp augmente son efficacité en utilisant un système de calcul de hachage.

L'idée est de calculer la valeur de hachage (hash) du motif recherché, puis parcourir le texte en utilisant une fenêtre
glissante de la même longueur que le motif, en calculant le hash de cette fenêtre à chaque glissement.
Pour chaque position, nous comparons la valeur de hachage de la fenêtre avec la valeur de hachage du motif et nous
effectuons des opérations de comparaison de caractères seulement si les valeurs de hachage sont identiques.

Cette technique permet donc de limiter le nombre d'opérations de comparaison inutiles.
Même si elle est plus efficace que la méthode naïve en générale, elle reste bien moins efficace que d'autres.

Pour en savoir plus sur l'algorithme visitez cette page : https://fr.wikipedia.org/wiki/Algorithme_de_Rabin-Karp
"""

#--------------------------------------------------------------------------------------------------------------------
#                                            FONCTION PRINCIPALE
#--------------------------------------------------------------------------------------------------------------------


# La fonction de recherche prend en entrée le motif à chercher, le texte où chercher le motif, et un nombre premier q.
# d est la taille de l'alphabet
# q est un nombre premier utile pour le hashage
#La methode de calcule de hash des sous-chaînes est la méthode de Horner
def robinKarpSearch(pattern, text, q, d):
    #On déclare les variables 
    len_pattern = len(pattern)    # La longueur du motif
    len_text = len(text)       # La longueur du texte
    hash_motif = 0               # Le hash du motif
    hash_sous_chaine = 0               # Le hash de la sous-chaîne de texte courante
    h = 1               # La valeur de la plus grande puissance de d qui est inférieure à q

    # les pointeurs de position
    i = 0
    j = 0

    #On calcule le hash du motif 
    for i in range(len_pattern):
        hash_motif = (d*hash_motif + ord(pattern[i])) % q   # ord() retourne la valeur ASCII du caractère
       
    # On calcule la valeur de la plus grande puissance de d qui est inférieure à q
    for i in range(len_pattern-1):
        h = (h*d) % q

    #la valeur de h est utilisée pour "éliminer" le premier caractère de la 
    #sous-chaîne de texte courante lors du calcul de son hash. Ce qui est utile 
    #lors du calcul du hash de la sous-chaîne suivante : on doit soustraire le 
    #produit de la première lettre de la sous-chaîne courante par la valeur de la 
    #plus grande puissance de d qui est inférieure à q (multipliée par le code ASCII de la lettre),
    # puis ajouter le code ASCII de la lettre qui suit dans la sous-chaîne courante, multiplié par d^(m-1). 
    # Calcul du hash du motif et de la première sous-chaîne de texte

    #On calcul le hash de la premiere sous-chaine
    for i in range(len_pattern):
         hash_sous_chaine = (d*hash_sous_chaine + ord(text[i])) % q
    
    # On parcours chaque position du texte 
    for i in range(len_text-len_pattern+1):
        # Si les hashs des motifs sont égaux, peut etre qu'on a trouvé le pattern
        # Pour le savoir on va comparer caractère par caractère
        if hash_motif == hash_sous_chaine:  

            # initialisation du pointeur et de la condition d'arret
            j = 0
            tout_est_bon = True

            # on parcours la sous chaine et on verifie qu'elle correspond bien au pattern

            while (tout_est_bon & (j<(len_pattern))):
                tout_est_bon = (text[i+j] == pattern[j])
                j+=1

            
            #on a trouvé une ccurence du pattern on l'indique à l'utilisateur
            if tout_est_bon:
                print("Le patern est trouvé à la position :  " + str(i))

         # Si ce n'est pas la dernière sous-chaîne de texte, calculer le hash de la prochaine sous-chaîne
        if i < len_text-len_pattern: 
            # On utilise la bidouille avec d pour ne pas à avoir à recalculer tout le hashage 
            hash_sous_chaine = (d*(hash_sous_chaine-ord(text[i])*h) + ord(text[i+len_pattern])) % q

            if hash_sous_chaine < 0:
                hash_sous_chaine = hash_sous_chaine+q





#-------------------------------------------------TESTS-----------------------------------------------------------------
text = "ABCCDDAEFG"
pattern = "CDD"
q = 13
d = 10   # La taille de l'alphabet, dans ce cas-ci les chiffres 0 à 9.
#robinKarpSearch(pattern, text, q, d)
#Le patern est trouvé à la position :  3




text = "abbabababbababbabababababbabbabbbbbbbbababababbababbabababababbababababaaabbabbabababababbabbbabbabbababbabbabababababababbababbabbaababbbbab"
pattern = "abba"
q = 101
d = 2   # La taille de l'alphabet, dans ce cas-ci les chiffres 0 à 9.
#robinKarpSearch(pattern, text, q, d)

"""Le patern est trouvé à la position :  0
Le patern est trouvé à la position :  7
Le patern est trouvé à la position :  12
Le patern est trouvé à la position :  23
Le patern est trouvé à la position :  26
Le patern est trouvé à la position :  44
Le patern est trouvé à la position :  49
Le patern est trouvé à la position :  60
Le patern est trouvé à la position :  73
Le patern est trouvé à la position :  76
Le patern est trouvé à la position :  87
Le patern est trouvé à la position :  94
Le patern est trouvé à la position :  97
Le patern est trouvé à la position :  102
Le patern est trouvé à la position :  105
Le patern est trouvé à la position :  120
Le patern est trouvé à la position :  125
Le patern est trouvé à la position :  128"""




text = "Ceci est un test un test sers a tester si un algorithme marche si un test marche cela est bien mais on ne peut conclure de la validité de l algo qu apres avoir fait tous les tests limites fin du test"
pattern = "test"
q = 7
d = 26   # La taille de l'alphabet, dans ce cas-ci les chiffres 0 à 9.
#robinKarpSearch(pattern, text, q, d)
"""Le patern est trouvé à la position :  12
Le patern est trouvé à la position :  20
Le patern est trouvé à la position :  32
Le patern est trouvé à la position :  69
Le patern est trouvé à la position :  174
Le patern est trouvé à la position :  195"""