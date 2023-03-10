def supprimer_doublon():
    # Créer la liste avec des doublons
    L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    L_sans_doublons = list(set(L))
    print(L_sans_doublons)


supprimer_doublon()