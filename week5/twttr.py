def main():
    word = shorten(input("Input: ").strip())
    print(word)


def shorten(word):
    new_word = ""
    for ch in word:
        if ch in ['a', 'e', 'i', 'o', 'u', \
                  'A', 'E', 'I', 'O', 'U']:
            new_word += ""
        else:
            new_word += ch
    return new_word


if __name__ == "__main__":
    main()