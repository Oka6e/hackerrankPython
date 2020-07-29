import re

def k_in_S_indices(S, k):
    pattern = re.compile(k)
    m = pattern.search(S)
    if not m:
        print((-1, -1))
    while m:
        start_index = m.start()
        end_index = m.end() - 1
        print((start_index, end_index))
        m = pattern.search(S, m.start() + 1) 

if __name__ == '__main__':
    S = input() 
    k = input()
    
    k_in_S_indices(S, k)
