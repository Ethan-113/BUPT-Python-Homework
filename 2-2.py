if __name__ == "__main__":
    n = int(input())
    set_a = set(map(int, input().split()))

    m = int(input())
    set_b = set(map(int, input().split()))

    intersection = sorted(list(set_a.intersection(set_b)))
    union = sorted(list(set_a.union(set_b)))
    complement = sorted(list(set_a.difference(set_b)))

    print(" ".join(map(str, intersection)))
    print(" ".join(map(str, union)))
    print(" ".join(map(str, complement)))