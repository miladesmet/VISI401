def algo_naif(pattern, texte):
    #Tableau de résultats
    occurences = []

    #compteur parcourants la chaine de caractere
    for i in range(0, len(texte) - len(pattern)+1):
        trouve = True

        #compteur parcourant la longueur du pattern
        for j in range(0, len(pattern)):

            # On repere un misatch
            if texte[i+j] != pattern[j]:
                trouve = False

        #si aucun de mismatch trouvé c'est qu'on a trouvé une occurence
        if trouve :
            print("Trouvé!")
            print(i)
            occurences.append(i)

    return occurences


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

print(algo_naif(pattern, texte_cinquieme_element))