def trier_liste_croissant(liste):
    for i in range(len(liste)):
        for j in range(i+1, len(liste)):
            if liste[i] > liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
    return liste

# exemple d'une liste
L = [34, 16, 428, 319, 9]
L_triee = trier_liste_croissant(L)
print(L_triee)
