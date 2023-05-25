#--------------------------------------------------------------------------------------------------------------------
#                       BIENVENUE DANS LE FICHIER PRINCIPAL
#--------------------------------------------------------------------------------------------------------------------

# Si vous voulez tester simplement sans vous plonger dans le code les différents algorithmes que j'ai codé, vous êtes au bon endroit.


#---------------------Ne vous occupez pas de cette partie--------------------------
from Naive import *
from RobinKarp import *
from KMP import *
from BoyerMooreMila import *
from Suffix import *
from BurrowWheeler import *
from AhoCorasick import *
import time
import re


#---------------------!!!!!PARTIE A REMPLIR!!!!!!--------------------------

#Remplissez la liste de patterns à chercher comme l'exemple ci dessous
patterns = ["test", "le", "t"]

#Remplissez le texte dans lequel chercher comme l'exemple ci dessous
texte = "Ceci est un test, ce n'est pas le plus evident"

#Choisissez l'algo à utiliser (entier entre 1 et 7)
"""
1: Naif
2: RabinKarp
3: KMP
4: Boyer Moore
5: Arbre des Suffixes
6: Burrow Wheeler
7: Aho Corasick
"""
choix_algo = 4

#---------------------Ne touchez à rien ici--------------------------

def function_principale_recherche (patterns, texte, choix_algo):

    if (choix_algo == 1):
        print("Vous avez choisi la méthode naïve")
        for i in range(0, len(patterns)) :

            start_time = time.perf_counter()
            res = algo_naif(patterns[i], texte)

            end_time = time.perf_counter()

            print("Le pattern " + patterns[i]+" est trouvé au positions suivantes : ")

            for j in range(0, len(res)):
                print("         - "+ str(res[j]))

            execution_time = end_time - start_time
            print("Le temps d'exécution de cette recherche a été de", execution_time, "secondes.")

    if (choix_algo == 2):
        print("Vous avez choisi l'algo RabinKarp")
        # len de l'alphabet
        d= len(set(texte))
        for i in range(0, len(patterns)):

            print("--------Recherche du pattern " + patterns[i] + " -----------------")

            start_time = time.perf_counter()
            robinKarpSearch(patterns[i], texte, 7, d)
            end_time = time.perf_counter()

            execution_time = end_time - start_time
            print("Le temps d'exécution de cette recherche a été de", execution_time, "secondes.")

    if (choix_algo == 3):
        print("Vous avez choisi l'algo KMP")
        for i in range(0, len(patterns)) :

            start_time = time.perf_counter()
            res = recherche_KMP(patterns[i], texte)
            end_time = time.perf_counter()

            print("Le pattern " + patterns[i]+" est trouvé au positions suivantes : ")

            for j in range(0, len(res)):
                print("         - "+ str(res[j]))

            execution_time = end_time - start_time
            print("Le temps d'exécution de cette recherche a été de", execution_time, "secondes.")

    if (choix_algo == 4):
        print("Vous avez choisi l'algo Boyer Moore")
        alphabet = ''.join(set(texte))

        for i in range(0, len(patterns)) :

            start_time = time.perf_counter()
            res = boyer_moore_search(texte, patterns[i], alphabet)
            end_time = time.perf_counter()

            print("Le pattern " + patterns[i]+" est trouvé au positions suivantes : ")

            for j in range(0, len(res)):
                print("         - "+ str(res[j]))

            execution_time = end_time - start_time
            print("Le temps d'exécution de cette recherche a été de", execution_time, "secondes.")

    if (choix_algo == 5):
        print("Vous avez choisi l'algo des Suffixes")


        start_time = time.perf_counter()
        res = recherche_suffixes( texte, patterns)
        end_time = time.perf_counter()

        for i in range(0, len(patterns)):
            print("Le pattern " + patterns[i]+" est trouvé au positions suivantes : ")

            for j in range(0, len(res[i])):
                print("         - "+ str(res[i][j]))

        execution_time = end_time - start_time
        print("Le temps d'exécution de cette recherche a été de", execution_time, "secondes.")

    if (choix_algo == 6):
        print("Vous avez choisi l'algo de Burrow Wheeler")


        start_time = time.perf_counter()
        res = find_patterns_BW( texte, patterns)
        end_time = time.perf_counter()

        for i in range(0, len(patterns)):
            print("Le pattern " + patterns[i]+" est trouvé au positions suivantes : ")

            for j in range(0, len(res[i])):
                print("         - "+ str(res[i][j]))

        execution_time = end_time - start_time
        print("Le temps d'exécution de cette recherche a été de", execution_time, "secondes.")

    if (choix_algo == 7):
        print("Vous avez choisi l'algo de Aho Corasick")
        print("Attention les indices sont ceux dans une chaine sans charactere spéciaux et sans espace")
        texte_propre = re.sub(r'[^a-zA-Z0-9]', '', texte)
        start_time = time.perf_counter()
        res = searchCorasicnb_mots(patterns, texte_propre)
        end_time = time.perf_counter()

        execution_time = end_time - start_time
        print("Le temps d'exécution de cette recherche a été de", execution_time, "secondes.")


# -----------------------Lancez l'execution---------------------------------


function_principale_recherche (patterns, texte, choix_algo)
