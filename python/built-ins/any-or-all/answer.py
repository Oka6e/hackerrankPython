def check_pos_and_any_palindrome(lst):
    return all(int(i) > 0 for i in lst) and any(j == j[::-1] for j in lst)

if __name__ == '__main__':
    N = int(input()) #Total Number of integer in list
    lst = input().split()

    print(check_pos_and_any_palindrome(lst))
