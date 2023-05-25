# VISI401

Bonjour à tous,

Je me présente je suis Mila DESMET, je suis élève en L2 CMI informatique. 

Ce projet contient le code que j'ai produit dans le cadre de la matière intitulée : bibliographie scientifique (VISI401_CMI).
Le sujet de ce projet est : La recherche de chaîne de caractère dans d'autres chaines de caractère.

Durant ce projet, j'ai pu découvrir plusieurs algorithmes de recherche de pattern dans des chaines de caractères.
Vous allez pouvoir ici en retrouver plusieurs. 

## La méthode naïve

Pour bien commencer et comprendre l'utilité des algorithmes suivant rien de mieux que de commencer par la méthode naïve.
Même si dans beaucoup de cas elle est très peu efficace il faut parfois la garder sous le coude, car sa simplicité d'implémentation mais surtout le fait qu'elle ne requière aucun prétraitement peu dans certains cas en faire la solution la plus efficace.
Ceci est souvent le cas pour rechercher un pattern dans un texte "court".

Pour le tester : 
Allez dans le fichier main.py
Remplissez la liste de patterns à chercher dans la variable patterns
Remplissez le texte dans lequel chercher dans la variable texte
Entrez le nombre 1 dans la variable choix_algo
Lançez l'exécution du fichier

Pour en savoir un peu plus sur le code rendez-vous dans le fichier : Naive.py

Pour en savoir plus sur l'algorithme visitez cette page : 
https://pixees.fr/informatiquelycee/n_site/nsi_term_algo_boyer.html (Seulement au début)


## La méthode Rabin-Karp

Similaire à la méthode naïve la méthode Rabin-Karp augmente son efficacité en utilisant un système de calcul de hachage.

L'idée est de calculer la valeur de hachage (hash) du motif recherché, puis parcourir le texte en utilisant une fenêtre glissante de la même longueur que le motif, en calculant le hash de cette fenêtre à chaque glissement.
Pour chaque position, nous comparons la valeur de hachage de la fenêtre avec la valeur de hachage du motif et nous effectuons des opérations de comparaison de caractères seulement si les valeurs de hachage sont identiques.

Cette technique permet donc de limiter le nombre d'opérations de comparaison inutiles. Même si elle est plus efficace que la méthode naïve en générale, elle reste bien moins efficace que les méthodes suivantes.

Pour le tester : 
Allez dans le fichier main.py
Remplissez la liste de patterns à chercher dans la variable patterns
Remplissez le texte dans lequel chercher dans la variable texte
Entrez le nombre 2 dans la variable choix_algo
Lançez l'exécution du fichier

Pour en savoir un peu plus sur le code rendez-vous dans le fichier : RobinKarp.py

Pour en savoir plus sur l'algorithme visitez cette page : 
https://fr.wikipedia.org/wiki/Algorithme_de_Rabin-Karp

## La méthode Knuth Morris Pratt

La méthode KMP se base sur un prétraitement du pattern recherché.
L'objectif comme beaucoup d'autres algorithmes présentés ici est d'éviter les comparaisons inutiles.

Le prétraitement est simple, il suffit de créer un tableau de la longueur du pattern recherché.
Dans chaque, ieme case nous entrons la taille du plus grand suffixe qui est aussi préfixe du ieme préfixe du pattern.
Par exemple pour ONIONS on a [0,0,0,1,2,0]

En cas de mismatch en jeme position dans le pattern nous pouvons avancer la fenêtre de comparaison du nombre dans la j-1eme
case de notre tableau et de ne pas retourner au début, mais de bien reprendre au meme caractère du texte où nous en étions.

Cette table est en fait la table Good Suffix de l'algorithme Boyer-Moore

Pour le tester : 
Allez dans le fichier main.py
Remplissez la liste de patterns à chercher dans la variable patterns
Remplissez le texte dans lequel chercher dans la variable texte
Entrez le nombre 3 dans la variable choix_algo
Lançez l'exécution du fichier

Pour en savoir un peu plus sur le code rendez-vous dans le fichier : KMP.py

Pour en savoir plus sur l'algorithme de Boyer-Moore, vous pouvez consulter cette page :
https://www.techno-science.net/glossaire-definition/Algorithme-de-Knuth-Morris-Pratt.html#:~:text=L'algorithme%20de%20Knuth%2DMorris%2DPratt%20(souvent%20abr%C3%A9g%C3%A9,P%20dans%20un%20texte%20S.

## L'algorithme de Boyer-Moore

Il utilise une heuristique basée sur les caractères du motif pour effectuer des sauts lors de la recherche, ce qui réduit le nombre de comparaisons nécessaires.

L'idée derrière cet algo est de créer deux tableaux lors d'un prétraitement sur le texte.

Le tableau de décalage des caractères (bad character shift) indique la distance à laquelle un caractère dans le motif peut être décalé lors d'un mismatch.
Le tableau de décalage de préfixe (good suffix shift) indique la distance maximale par laquelle le motif peut être décalé en cas de correspondance partielle.

Ces deux tableaux nous permettrons suivant le cas de mismatch de décaler le pattern de la distance la plus grande possible lors d'un mismatch ou d'un find et donc de limiter grandement le nombre d'opérations inutiles. 


Par exemple si nous avons trouvé le pattern nous pouvons décaler la fenêtre de comparaison vers la gauche en utilisant le tableau de décalage de préfixe pour trouver la plus grande correspondance possible et donc éviter de comparer des caractères dont nous savons déja s'ils sont égaux ou non.

De la même manière si nous avons un mismatch au tout début nous utilisons le tableau de décalage des caractères pour sauter les caractères qui ne peuvent pas correspondre.

Dans le cas d'un mismatch en cours de mot, nous utilisons le tableau de décalage des caractères, cela nous permet d'aligner le caractère du texte en comparaison avec la dernière occurrence correspondante dans le pattern. 


Pour le tester : 
Allez dans le fichier main.py
Remplissez la liste de patterns à chercher dans la variable patterns
Remplissez le texte dans lequel chercher dans la variable texte
Entrez le nombre 4 dans la variable choix_algo
Lançez l'exécution du fichier

Pour en savoir un peu plus sur le code rendez-vous dans le fichier : BoyerMooreMila.py

Pour en savoir plus sur l'algorithme de Boyer-Moore, vous pouvez consulter cette page :
https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore

## L'algorithme des suffixe

L'algorithme des suffixes fonctionne en effectuant un prétraitement sur le texte et non pas sur le(s) pattern(s).

L'idée est de prendre tous les suffixes possibles d'un texte est de les "assembler" dans un abre binaire. 

Dans ce cas si un schéma vaut mieux que mille mots, pour comprendre la construction et l'utilisation de cet arbre je vous invite à visiter le document suivant : http://www-desir.lip6.fr/~herpsonc/uploads/Arbres-de-Suffixes-Suffix-Tree-Construction-Herpson2008.pdf

Cette méthode peut être assez lourde en termes de prétraitement si le texte est long, mais ce temps qui reste linéaire est largement récompensé du fait qu'une foit que l'arbre est construit la recherche d'un pattern est d'une complexité linéaire à la taille de ce pattern seulement, la taille du texte n'intervient donc plus dans la recherche.

Pour le tester : 
Allez dans le fichier main.py
Remplissez la liste de patterns à chercher dans la variable patterns
Remplissez le texte dans lequel chercher dans la variable texte
Entrez le nombre 5 dans la variable choix_algo
Lançez l'exécution du fichier

Pour en savoir un peu plus sur le code rendez-vous dans le fichier : Suffix.py

## L'algorithme de Burrow Wheeler

L'algorithme de recherche de motifs avec la transformation de Burrows-Wheeler (BWT) est basé sur la propriété selon laquelle les caractères identiques sont regroupés dans la dernière colonne de la matrice triée. 
Elle utilise le même prétraitement que la compression de Burrow Wheeler.

L'algorithme de recherche de motifs avec la transformation de BurrowsWheeler peut être une méthode efficace pour la recherche de motifs dans un texte. Cependant, il nécessite la préparation préalable de la transformation de Burrows-Wheeler, qui peut être coûteuse en termes de temps et de mémoire.

Pour le tester : 
Allez dans le fichier main.py
Remplissez la liste de patterns à chercher dans la variable patterns
Remplissez le texte dans lequel chercher dans la variable texte
Entrez le nombre 6 dans la variable choix_algo
Lançez l'exécution du fichier

Pour en savoir plus allez voir ce document : https://pdfs.semanticscholar.org/03ba/de7ab5a6ff7a007780d0a366a946bd640868.pdf

## L'algorithme Aho Corasick

L'algorithme d'Aho-Corasick est pour sa part efficace lorsque nous voulons chercher plusieurs patterns dans un même texte. 
Le prétraitement ressemble à celui de l'arbre des suffixes à l'exception que celui-ci est construit non pas avec les suffixes, mais avec les différents patterns. Des chemins sont aussi ajoutés, pour que en cas de mismatch on ne revienne pas au début de l'arbre, mais au noeud le plus profond possible déjà vérifié. Ceci permet de vérifier autant de patterns que l'on souhaite en ne passant qu'une seule et même fois sur le texte.   

Pour en savoir plus sur l'algorithme Aho-Corasick, vous pouvez consulter cette page :
https://fr.wikipedia.org/wiki/Algorithme_d%27Aho-Corasick

Pour le tester : 
Allez dans le fichier main.py
Remplissez la liste de patterns à chercher dans la variable patterns
Remplissez le texte dans lequel chercher dans la variable texte
Entrez le nombre 7 dans la variable choix_algo
Lançez l'exécution du fichier


# Testez mes fonctions 

Pour tester mes fonctions : 
- Allez dans le fichier main.py
- Remplissez la liste de patterns à chercher dans la variable patterns
- Remplissez le texte dans lequel chercher dans la variable texte
  - Entrez le nombre correspondant à l'algo que vous souhaitez tester dans la variable choix_algo (entier entre 1 et 7)
  """
  1: Naif
  2: RabinKarp
  3: KMP
  4: Boyer Moore
  5: Arbre des Suffixes
  6: Burrow Wheeler
  7: Aho Corasick
  """
- Lançez l'exécution du fichier

Le programme vous donnera les occurrences des chaque pattern et le temps d'exécution de l'algo choisis.


# Conclusion

En conclusion, ce projet m'a permis de découvrir et d'implémenter plusieurs algorithmes de recherche de motifs dans des chaînes de caractères. Chaque algorithme a ses propres avantages et inconvénients en termes d'efficacité et de complexité. La méthode naïve, bien que simple, peut être utile dans certains cas particuliers où le prétraitement n'est pas nécessaire. 
Les algorithmes tels que Rabin-Karp, Knuth-Morris-Pratt (KMP), Boyer-Moore, et Aho-Corasick offrent des améliorations significatives en termes d'efficacité grâce à des techniques de prétraitement et de sauts intelligents.

Le prétraitement des motifs ou du texte, ainsi que l'utilisation de tables et de structures de données spécifiques, permettent d'éviter les comparaisons inutiles et de réduire le nombre d'opérations nécessaires lors de la recherche de motifs. Cependant, il convient de noter que ces prétraitements peuvent également nécessiter un coût supplémentaire en termes de temps et de mémoire.

Chaque algorithme présenté dans ce projet a ses propres cas d'utilisation et limites. Il est donc important de choisir l'algorithme approprié en fonction des contraintes spécifiques du problème.

J'espère que ce projet vous a permis de mieux comprendre les différentes méthodes de recherche de motifs dans des chaines de caractere et vous a donné envie d'explorer et d'en découvrir d'autre (Il y en a plein d'autres, des astucieux comme des laborieux)

Je vous remercie de l'intérêt que vous portez à mon travail.

Bonne exploration ! 