from collections import OrderedDict

def supermarket_inventory(N):
    inventory = OrderedDict()
    for i in range(N):
        item_name, space, net_price = input().rpartition(' ')
        inventory[item_name] = inventory.get(item_name, 0) + int(net_price)
    for item_name, net_price in inventory.items():
        print(item_name, net_price)

if __name__ == '__main__':
    N = int(input()) # number of items

    supermarket_inventory(N)
