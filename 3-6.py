import math

def add(one, two):
    result = [0, 0, 0]
    result[0] = one[0] + two[0]
    result[1] = one[1] + two[1]
    result[2] = one[2] + two[2]
    return result

def sub(one, two):
    result = [0, 0, 0]
    result[0] = one[0] - two[0]
    result[1] = one[1] - two[1]
    result[2] = one[2] - two[2]
    return result

def mul(one, num):
    result = [0, 0, 0]
    result[0] = one[0] * num
    result[1] = one[1] * num
    result[2] = one[2] * num
    return result

def div(one, num):
    result = [0, 0, 0]
    result[0] = "{:.2f}".format(one[0] / num)
    result[1] = "{:.2f}".format(one[1] / num)
    result[2] = "{:.2f}".format(one[2] / num)
    return result

def get_length(one):
    number = one[0]**2 + one[1]**2 + one[2]**2
    square_root = math.sqrt(number)
    result = "{:.2f}".format(square_root)
    return result

if __name__ == "__main__":
    numbers = input()
    first = [int(x) for x in numbers.split()]
    numbers = input()
    second = [int(x) for x in numbers.split()]

    mode = input()
    if mode == 'add':
        res = add(first, second)
        data = " ".join(map(str, res))
        print(data)
    if mode == 'sub':
        res = sub(first, second)
        data = " ".join(map(str, res))
        print(data)
    if mode == "div":
        num = int(input())
        res = div(first, num)
        data = " ".join(map(str, res))
        print(data)
    if mode == "mul":
        num = int(input())
        res = mul(first, num)
        data = " ".join(map(str, res))
        print(data)
    if mode == "get_length":
        res = get_length(first)
        print(res)