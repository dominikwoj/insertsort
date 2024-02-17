def insert_sort(in_t):
    '''
    >>> insert_sort([])
    []
    >>> insert_sort([71])
    [71]
    >>> insert_sort([71, 65, 39, 38, 38, 19, 42, 85, 33])
    [19, 33, 38, 38, 39, 42, 65, 71, 85]
    '''
    if len(in_t) == 0:
        return []
    out_t = [in_t[0]]

    # print(in_t)
    for i in in_t[1:]:
        for j in range(0, len(out_t)):
            if i < out_t[j]:
                out_t.insert(j, i)
                break
            elif j + 1 == len(out_t):
                out_t.append(i)
    return out_t


# if __name__ == '__main__':
    # import doctest
    #
    # doctest.testmod()
    # import random
    #
    # print(insert_sort([random.randint(1, 100) for i in range(1, 10000)]))

