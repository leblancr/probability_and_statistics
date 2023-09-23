from itertools import chain, combinations


def get_power_set(input_set):
    print('input_set:', input_set)
    print('len(input_set):', len(input_set))
    pwr_set = set({})
    print('pwr_set:', pwr_set)
    combs = list(chain.from_iterable(list(combinations(input_set, r) for r in range(len(input_set) + 1))))
    
    return combs
    
    
if __name__ == '__main__':
    input_set = {1, 2, 3, 4}
    pset = get_power_set(input_set)
    print('power set:', pset)
    