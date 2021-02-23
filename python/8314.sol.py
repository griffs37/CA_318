#
#   In this exercise, find the smallest number of coins to make up the specified amount
#    using dynamic programming.
#
#   return the memo that you create as a result
#
import math

def dp_make_change(amount, coins):
   assert amount >= 0
   # Initialise memo to be infinity for each of amount + 1 values
   memo = [math.inf] * (amount + 1)
   # Base Case
   memo[0] = 0
   # We reverse the coin list so we can iterate through it backwards
   coins.reverse()
   memolen = len(memo)
   for i in range(1, memolen):
       for coin in coins:
           memo[i] = min([memo[i], memo[i - coin] + 1])
   return memo
#
#   normally, you would return memo[amount] at this point, but in this exercise, you just return the memo.
#