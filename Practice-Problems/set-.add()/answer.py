def count_unique_stamps(N):
    unique_stamps = set()
    for i in range(N):
        unique_stamps.add(input())
    return len(unique_stamps)

if __name__ == '__main__':
    N = int(input())
    print(count_unique_stamps(N))
