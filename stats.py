def count_word(content):
    words = content.split()
    return len(words)

def count_characters(content):
    char_dict = {c.lower(): 0 for c in content}
    for c in content:
        c = c.lower()
        char_dict[c] += 1

    return char_dict