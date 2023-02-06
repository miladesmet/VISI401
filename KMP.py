
def lps_maker(pattern):
    lps = [0] * len(pattern)

    #gestion première lettre
    lps[0] = 0

    # init variables utiles
    M = len(pattern)
    i = 1
    compte = 0

    while i < M :
        # si la lettre regardée
        if pattern[i] == pattern[compte]:
            compte += 1
            lps[i] = compte
            i += 1
        else:
            if compte != 0:
                compte = lps[compte-1]
            else:
                lps[i] = 0
                i += 1


    return lps

def recherche_KMP(pattern, texte):

    # Calcul des constantes locales
    N = len(texte)
    M = len(pattern)

    #pres traitement calcul des suffixe préfixe
    lps = lps_maker(pattern)

    #Pointeurs de position
    i=0
    j=0

    #tableaux de résultats
    occurences = []
    #Boucle d'avancement

    while i< N-M+1 :

        if texte[i] == pattern[j]:
        #si les lettres qu'on regarde sont les memes on avance
            i += 1
            j += 1
        else:
        #si les lettres qu'on regarde sont différentes
            # si on etait au tout début du patern on avance dans le texte
            if j == 0 :
                i+=1
            #si on etait plus loins on remet j au point ou nous devons comparer
            else :
                j =lps[j-1]
        #si on a trouvé tout le pattern
        if j == M :
            print("Trouvé ! ")
            print(i-j)
            occurences.append(i-j)
            j = lps[j-1]
    return occurences



#-----------------------------------------------------------------------------------------------------------------------
#TESTS
#-----------------------------------------------------------------------------------------------------------------------


#print( lps_maker("kayak"))
#print(lps_maker("je ne pense pas je suis sure"))
#print(lps_maker("AABCBBABBCABCBCBAABCBABCBBAABCBBABBCABCBCBAACCABBBACBBCBBABBCBABCBCBABCAAABBCBCBABCBAABC"))

texte_cinquieme_element = "En 1914 dans un temple en Égypte, un archéologue fait une grande découverte sur un combat contre le Mal absolu." \
        " Mais à ce moment-là, une équipe extraterrestre arrive sur le lieu pour embarquer quatre pierres représentant quatre " \
        "éléments et un être de forme humanoïde, un cinquième élément. En repartant, ils annoncent qu'ils reviennent dans 300 ans" \
        " quand le mal reviendra.300 ans plus tard, alors que le Mal prend forme dans la galaxie, le vaisseau extraterrestre censé " \
        "rapporter les cinq éléments est attaqué. Seul le cinquième élément (qui est une femme au surnom de Leeloo) survit et, ramenée" \
        " à New York, rencontre par hasard le chauffeur de taxi Korben Dallas qui est un ancien militaire. Les deux " \
        "protagonistes retrouvent le gardien du temple égyptien, le prêtre Cornelius, et tous trois doivent partir sur " \
        "Phloston Paradise pour récupérer les pierres qui y* sont cachées. Mais ils doivent faire vite avant que Zorg ne " \
        "mette la main dessus pour le compte du Mal..."

pattern = "Mal"

#print(recherche_KMP(pattern, texte_cinquieme_element) )