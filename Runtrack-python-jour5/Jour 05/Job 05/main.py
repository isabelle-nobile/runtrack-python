def calculate_distance(marches, hauteur):
    hauteur_totale = marches * hauteur * 2 
    distance = hauteur_totale * 5 * 7 / 100
    return round(distance, 2)

print("Pour {} marches de {} cm, le gardien parcours {} m par semaine.".format(40, 16, calculate_distance(40, 16)))
