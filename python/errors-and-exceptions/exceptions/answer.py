def zero_division_error_exception(number_of_test_cases):
    
    for i in range(T):
        a, b = input().split()
        
        try:
            print(int(a)//int(b))
        except ZeroDivisionError as z:
            print("Error Code:", z)
        except ValueError as v:
            print("Error Code:", v)

if __name__ == '__main__':
    T = int(input()) # number of test cases
    zero_division_error_exception(T)
