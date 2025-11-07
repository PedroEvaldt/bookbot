texto = "um texto qualquer"

char_dict = {c.lower() : 0 for c in texto}
for c in texto:
    c.lower()
    char_dict[c] += 1
print(char_dict)