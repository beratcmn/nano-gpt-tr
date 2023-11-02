def main():
    with open('data.md', 'r') as f:
        data = f.read()
        print(len(data))


if __name__ == '__main__':
    main()
