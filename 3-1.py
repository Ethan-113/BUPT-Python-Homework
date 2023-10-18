import re

if __name__ == "__main__":
    format_in = input()
    format = [int(x) for x in format_in.split()]

    first = eval(input())

    second = eval(input())

    final = []
    flag = 0
    for r in range(format[0]):
        array = []
        for c in range(format[1]):
            array.append(first[r][c]+second[r][c])
        final.append(array)

    toString = str(final)
    toString = toString.replace(' ','')
    print(toString)