#def Boyer_Moore(pattern, texte)

def table_bad_character (pattern):
    #init de la table
    table = dict()

    #init const locale
    M = len(pattern)

    #on parcourt tout le pattern
    for i in range(M):
        lettre = pattern[i]
        table[lettre] = max(1, M-i-1)

    #On ajoute le cas ou le caractere n'aparait jamais
    table["*"] = M
    return table

# TEST
print(table_bad_character ("TEST"))


def good_suffixe_table(pattern):









