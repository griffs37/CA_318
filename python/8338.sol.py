#
#   In this exercise, find the most value you can get from items which you will fit into a knapsack
#    using dynamic programming.
#
#   return the memo that you create as a result
#
import math

def dp_knapsack(initial_capacity, items):
   assert initial_capacity >= 0
   # Initialise memo to be - infinity for each of capacity + 1 values
   memo = [-math.inf] * (initial_capacity+1) # Had a BUG here ... initially + infinity
   memo[0] = 0
   # Insert code here
   for i in range(1, len(memo)):
       # we call our greedy knapsack function
       memo[i] = ks_greedy(i, items)
   return memo

def ks_greedy(initial_capacity, items):
   assert initial_capacity >= 0
   total_value = 0
   items.sort(key=getV, reverse=True)
   
   for i in items:
       while initial_capacity >= i.weight:
           total_value += i.value
           initial_capacity -= i.weight
   
   return total_value
   
   
def getV(item):
    return item.value/item.weight

#
#   normally, you would return memo[capacity] at this point, but in this exercise, you just return the memo.
#