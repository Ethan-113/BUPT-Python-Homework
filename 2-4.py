def insertion_sort(array):
    for i in range(1, len(array)):
        cur_index = i
        while array[cur_index-1] > array[cur_index] and cur_index-1 >= 0:
            array[cur_index], array[cur_index-1] = array[cur_index-1], array[cur_index]
            cur_index -= 1
        print(" ".join(map(str, array)))

if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    insertion_sort(elements)