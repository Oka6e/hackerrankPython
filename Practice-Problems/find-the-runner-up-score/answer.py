def find_runner_up(arr):
    unique_arr = sorted(list(set(arr)))

    runner_up = unique_arr[-2]
    
    return runner_up


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(find_runner_up(arr))
