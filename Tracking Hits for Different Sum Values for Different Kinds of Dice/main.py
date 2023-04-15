from itertools import product


def reg_sum_hits(n, s):
    dict_ = {}
    for i in product(list(range(1, s+1)), repeat=n):
        dict_[sum(i)] = dict_.get(sum(i), 0) + 1
    result = [[i, j] for i, j in dict_.items()]
    return result


if __name__ == '__main__':
    reg_sum_hits(3, 4)
