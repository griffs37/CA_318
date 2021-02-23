#
#   In this exercise, find the most value the greedy algorithm finds
#
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