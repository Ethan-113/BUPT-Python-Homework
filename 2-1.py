def main():
    number = int(input())
    dog_to_cat = {}

    for _ in range(number):
        cat_word, dog_word = input().split()
        dog_to_cat[dog_word] = cat_word

    document = []
    while True:
        line = input()
        if line == 'dog':
            break
        document.append(line)

    translated = []
    for word in document:
        if word in dog_to_cat:
            translated.append(dog_to_cat[word])
        else:
            translated.append('dog')

    print('\n'.join(translated))

if __name__ == "__main__":
    main()