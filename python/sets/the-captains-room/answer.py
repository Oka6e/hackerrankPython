def capt_room(num_members, room_nums):
    rooms = set()
    rooms_no_capt = set()
    for i in room_nums:
        if i not in rooms:
            rooms.add(i)
        else:
            rooms_no_capt.add(i)
    return (rooms - rooms_no_capt).pop()

if __name__ == '__main__':
    K = int(input()) # Number of members per group
    r = map(int, input().split()) # room numbers

    print(capt_room(K, r))
