def return_list():
    liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
    liste_arrondie = [round(x) for x in liste_nombres]
    liste_triee = sorted(liste_arrondie)
    print(liste_triee)

return_list()
