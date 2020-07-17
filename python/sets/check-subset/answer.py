def check_subset(set_1, set_2):
    return set_1.issubset(set_2)
    
if __name__ == '__main__':
    T = int(input()) # Number of test cases
    
    for i in range(T):
        num_A = int(input()) # Number of elements in Set A
        set_A = set(map(int, input().split())) # Set A

        num_B = int(input()) # Number of elements in Set B
        set_B = set(map(int, input().split())) # Set B

        print(check_subset(set_A, set_B))
