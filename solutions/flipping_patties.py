# Difficulty: 2.4
# Url: https://open.kattis.com/problems/flippingpatties
import math
from collections import defaultdict

class Order:
    def __init__(self, arg_list):
        self.serve_time = int(arg_list[1])
        self.flip_time = int(arg_list[1]) - int(arg_list[0])
        self.start_time = int(arg_list[1]) - int((2 * arg_list[0]))

def main(): 
    num_orders = int(input())

    orders = []
    for _ in range(num_orders):
        orders.append(Order(input().split()))

    # Because the timings on the orders are set in stone, we can count up how many hands are needed at each second. 
    actions = defaultdict(int) # int() returns 0, which is the default val we want
    for o in orders:
        actions[o.serve_time] += 1
        actions[o.flip_time] += 1
        actions[o.start_time] += 1

    print(math.ceil((max(list(actions.values())) / 2))) # The second defining the maximum number of hands will set the bar for number of needed chefs.

if __name__=="__main__":
    main()