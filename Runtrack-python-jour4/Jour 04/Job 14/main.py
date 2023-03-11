def my_long_word(n, phrase):
    words = phrase.split()
    result = ''
    for word in words:
        is_long_word = True
        count = 0
        for c in word:
            if not c.isalpha():
                is_long_word = False
                break
            count += 1
        if is_long_word and count > n:
            result += word + ' '
    return result.strip()

texte = "La peur est le chemin vers le côté obscur. La peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance."
n = 3
resultat = my_long_word(n, texte)
print(resultat)
