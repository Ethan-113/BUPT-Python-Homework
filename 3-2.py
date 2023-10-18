def verify_postorder(postorder):
    if not postorder:
        return True

    root_val = postorder[-1]
    i = 0
    while postorder[i] < root_val:
        i += 1

    for j in range(i, len(postorder) - 1):
        if postorder[j] < root_val:
            return False

    left_is_bst = verify_postorder(postorder[:i])
    right_is_bst = verify_postorder(postorder[i:-1])

    return left_is_bst and right_is_bst

if __name__ == "__main__":
    numbers = input()
    postorder = [int(x) for x in numbers.split()]
    res = verify_postorder(postorder)
    if res:
        print('true')
    else:
        print('false')