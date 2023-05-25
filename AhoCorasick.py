#--------------------------------------------------------------------------------------------------------------------
#                                       Implémentation de l'algo Aho-Corasick
#--------------------------------------------------------------------------------------------------------------------


"""L'algorithme d'Aho-Corasick est pour sa part efficace lorsque nous voulons chercher plusieurs patterns dans un même texte. Le prétraitement ressemble à celui de l'arbre des suffixes à l'exception que celui-ci est construit non pas avec les suffixes, mais avec les différents patterns. Des chemins sont aussi ajoutés, pour que en cas de mismatch on ne revienne pas au début de l'arbre, mais au noeud le plus profond possible déjà vérifié. Ceci permet de vérifier autant de patterns que l'on souhaite en ne passant qu'une seule et même fois sur le texte.

Pour en savoir plus sur l'algorithme Aho-Corasick, vous pouvez consulter cette page : https://fr.wikipedia.org/wiki/Algorithme_d%27Aho-Corasick
# Code inspiré (même si différent) du code de Manvi Saxena
"""

#--------------------------------------------------------------------------------------------------------------------
#                                            SOUS FONCTIONS
#--------------------------------------------------------------------------------------------------------------------

from collections import defaultdict


class ahocorasick:

    def __init__(self, words):

        self.max_states = sum([len(word) for word in words])
        self.max_characters = 26
        #les fin de patterns recherchés
        self.out = [0] * (self.max_states + 1)
        #les route d'erreures
        self.fail = [-1] * (self.max_states + 1)
        #les enfants
        self.goto = [[-1] * self.max_characters for _ in range(self.max_states + 1)]

        #on convertit tous les patterns en minuscule pour eviter les mismatch
        for i in range(len(words)):
            words[i] = words[i].lower()

        #on stocke les patterns à chercher dans l'objet
        self.words = words
        # on fabrique l'automate et on le stocke
        self.states_count = self.__build_matching_machine()

    def __build_matching_machine(self):

        # On recupere le nombre de pattern à regarder
        nb_mots = len(self.words)

        states = 1

        for i in range(nb_mots):
            #on recupere le mot actuel
            word = self.words[i]
            # on se place à la racine de l'abre de probabilité
            current_state = 0
            #Pour chaque lettre du mot actuelle on essaie d'avancer dans l'arbre
            for character in word:
                ch = ord(character) - 97
                # Si o trouve la lettre on s'enfonce dans l'arbre
                if self.goto[current_state][ch] == -1:
                    self.goto[current_state][ch] = states
                    states += 1

                current_state = self.goto[current_state][ch]
            self.out[current_state] |= (1 << i)

        queue = []

        for ch in range(self.max_characters):
            if self.goto[0][ch] == -1:
                self.goto[0][ch] = 0
            if self.goto[0][ch] != 0:
                self.fail[self.goto[0][ch]] = 0
                queue.append(self.goto[0][ch])



        while queue:
            state = queue.pop(0)
            for ch in range(self.max_characters):
                if self.goto[state][ch] != -1:
                    failure = self.fail[state]
                    while self.goto[failure][ch] == -1:
                        failure = self.fail[failure]

                    failure = self.goto[failure][ch]
                    self.fail[self.goto[state][ch]] = failure
                    self.out[self.goto[state][ch]] |= self.out[failure]
                    queue.append(self.goto[state][ch])

        return states

    def __find_next_state(self, current_state, next_input):
        answer = current_state
        ch = ord(next_input) - 97
        while self.goto[answer][ch] == -1:
            answer = self.fail[answer]

        return self.goto[answer][ch]

    def search_words(self, text):
        #On met le texte en minuscule pour éviter les erreurs
        text = text.lower()

        #on initialise l'etat de départ
        current_state = 0

        # on initialise le résultata
        result = defaultdict(list)


        for i in range(len(text)):
            current_state = self.__find_next_state(current_state, text[i])

            if self.out[current_state] == 0: continue

            for j in range(len(self.words)):
                if (self.out[current_state] & (1 << j)) > 0:
                    word = self.words[j]
                    result[word].append(i - len(word) + 1)

        return result


#--------------------------------------------------------------------------------------------------------------------
#                                            FONCTION PRINCIPALE
#--------------------------------------------------------------------------------------------------------------------

def searchCorasicnb_mots (words, text):
    model = ahocorasick(words)

    result = model.search_words(text)

    for word in result:
        for i in result[word]:
            print("Le mot ", word, "apparait à l'indice : ", i)

#------TESTS-------------------
words = ["me", "meet", "the", "hello"]
text = "memeethellomethe"
#searchCorasicnb_mots(words, text)
"""Le mot  me apparait à l'indice :  0
Le mot  me apparait à l'indice :  2
Le mot  me apparait à l'indice :  11
Le mot  meet apparait à l'indice :  2
Le mot  the apparait à l'indice :  5
Le mot  the apparait à l'indice :  13
Le mot  hello apparait à l'indice :  6"""

words = ["test", "le", "t"]
text = "Ceciestuntestcenestpaslepluevident"
#searchCorasicnb_mots(words, text)