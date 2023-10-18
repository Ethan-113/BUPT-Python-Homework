if __name__ == "__main__":
    sentence = str(input())
    with open('test.txt', 'w') as file:
        file.write(sentence)

    mode = str(input())
    sentence = str(input())
    if mode != 'r' and mode != 'x' and mode != 'x+':
        with open('test.txt', mode) as file:
            file.write(sentence)

    with open('test.txt', 'r') as file:
        file_content = file.read()

    print(file_content, end='')