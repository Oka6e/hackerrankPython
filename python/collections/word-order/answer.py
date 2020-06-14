from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    n = int(input()) # number of words

    unique_dict = OrderedCounter(input() for i in range(n))
    
    print(len(unique_dict))
    print(*unique_dict.values())
