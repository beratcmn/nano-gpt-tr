def main():
    with open('data.md', 'r', encoding="UTF-8") as f:
        data = f.read()
        print(f"Length of text: {len(data)}")

        chars = sorted(list(set(data)))
        vocab_size = len(chars)
        print(f"Number of unique characters: {vocab_size}")
        print(chars)


if __name__ == '__main__':
    main()
