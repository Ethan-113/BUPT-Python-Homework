def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    below = int(input())
    prime = []

    for i in range(below):
        if is_prime(i+1):
            prime.append(int(i + 1))

    for i in range(len(prime) - 1):
        print(prime[i], end=" ")

    print(prime[len(prime)-1], end="")