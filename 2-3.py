def lru_cache(n, m, pages):
    cache = []
    load_count = 0

    for page in pages:
        if page not in cache:
            load_count += 1
            if len(cache) == n:
                cache.pop(0)
            cache.append(page)
        else:
            cache.remove(page)
            cache.append(page)

    return load_count, sorted(cache)

if __name__ == "__main__":
    n, m = map(int, input().split())
    pages = list(map(int, input().split()))

    load_count, recorded_pages = lru_cache(n, m, pages)

    print(load_count)
    print(" ".join(map(str, recorded_pages)))