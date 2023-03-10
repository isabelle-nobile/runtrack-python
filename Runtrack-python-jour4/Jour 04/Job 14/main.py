def my_long_word(n, string):
    words = string.split()
    longs_words = []
    for word in words:
        if len(word) > n:
            longs_words.append(word)
    return " ".join(longs_words)

# exemple de chaine de charactères
string = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
n = 3
result = my_long_word(n, string)
print("Les mots plus longs que", n, "sont :", result)
