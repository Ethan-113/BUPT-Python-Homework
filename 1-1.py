def half(num):
    if num % 2 == 0:
        return int(num / 2)
    else:
        return int((num + 1) / 2)


if __name__ == '__main__':
    num_min = 0
    num_class = int(input())

    numbers_input = input()
    integers_input = [int(x) for x in numbers_input.split()]

    integers_sorted = sorted(integers_input)

    class_half = half(num_class)

    for i in range(class_half):
        num_min = num_min + half(integers_sorted[i])

    print(num_min)