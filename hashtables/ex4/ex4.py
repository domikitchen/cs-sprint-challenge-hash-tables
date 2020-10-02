def has_negatives(a):
    """
    YOUR CODE HERE
    """
    list1 = {}
    list2 = []

    for n in a:
        if n < 0:
            list1[n] = 0
    
    for n in a:
        if (n * -1) in list1:
            list2.append(n)


    print(list1)
    print(list2)

    return list2


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
