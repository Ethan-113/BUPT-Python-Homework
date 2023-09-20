if __name__ == '__main__':
    numbers_fix = []
    integers_input = input()
    integers = [int(x) for x in integers_input.split()]

    integers_first = str(integers[0])
    integers_second = str(integers[1])
    len_first = len(integers_first)
    len_second = len(integers_second)

    for i in range(5):
        if i < len_first:
            numbers_fix.append(int(integers_first[i]))
        if i < len_second:
            numbers_fix.append(int(integers_second[i]))

    result = 0

    for digit in numbers_fix:
        result = result * 10 + digit

    print(result)