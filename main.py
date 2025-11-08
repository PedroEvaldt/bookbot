from stats import count_word
from stats import count_characters
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    file_path = "books/frankenstein.txt"
    frank_content = get_book_text(file_path)
    frank_word_count = count_word(frank_content)
    frank_char_count_dict = count_characters(frank_content)
    list_dict = sort_dict(frank_char_count_dict)
    list_dict_formated = []
    for d in list_dict:
        if d["char"].isalpha():
            list_dict_formated.append(f"{d['char']}: {d['num']}")
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {frank_word_count} total words
--------- Character Count -------
{("\n").join(list_dict_formated)}
============= END ===============""")
    
    return 0

if __name__ == "__main__":
    main()

