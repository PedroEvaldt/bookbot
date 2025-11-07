from stats import count_word

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    frank_content = get_book_text("books/frankenstein.txt")
    frank_word_count = count_word(frank_content)
    print(f"Found {frank_word_count} total words")
    return 0

if __name__ == "__main__":
    main()

