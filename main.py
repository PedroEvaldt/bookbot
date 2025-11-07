def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def count_word(content):
    words = content.split()
    return len(words)

def main():
    frank_content = get_book_text("books/frankenstein.txt")
    frank_word_count = count_word(frank_content)
    print(f"Found {frank_word_count} total words")
    return 0

if __name__ == "__main__":
    main()

