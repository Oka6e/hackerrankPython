def ui_hash(integer_list):
    int_tup = tuple(integer_list)
    return hash(int_tup)

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(ui_hash(integer_list))
