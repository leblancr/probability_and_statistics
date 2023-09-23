from itertools import chain, combinations
import numpy as np


def get_power_set(input_set):
    print('input_set:', input_set)
    print('len(input_set):', len(input_set))
    pwr_set = set({})
    print('pwr_set:', pwr_set)
    combs = list(chain.from_iterable(list(combinations(input_set, r) for r in range(len(input_set) + 1))))
    
    return combs
    
    
if __name__ == '__main__':
    # input_set = {1, 2, 3, 4}
    # pset = get_power_set(input_set)
    # print('power set:', pset)

    omg = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    a = set(np.arange(0, 10, 2))
    b = set(np.arange(1, 9, 3))
    print('a:', a)
    print('b:', b)
    print('a.union(b):', a.union(b))
    print('b.union(a):', b.union(a))
    print('a.intersection(b):', a.intersection(b))
    print('b.intersection(a):', b.intersection(a))
    print('a.difference(b):', a.difference(b))
    print('b.difference(a):', b.difference(a))

    print('omg:', omg)
    print('a_compliment: (without a)', omg.difference(a))  # without a
    print('b_compliment: (without b)', omg.difference(b))  # without b
    print('-----')
    print(f"a.union(b) compliment: {omg.difference(a.union(b))} "
          "(everything without a and b)", )  # a.union(b) compliment
    print('a_compl.intersection(b_compl):', omg.difference(a).intersection(omg.difference(b))),
    print('intersection of two sets')
    print('everything without a in common with everything without b')
    print('-----')
    print(f"a.intersection(b) compliment: {omg.difference(a.intersection(b))} "
          "(everything without a and b common)", )  # a.union(b) compliment
    print('a_compl.union(b_compl):', omg.difference(a).union(omg.difference(b))),
    print('a_compl:', omg.difference(a)),
    print('b_compl:', omg.difference(b)),
    print('union of two sets')
    print('everything without a and everything without b')
    