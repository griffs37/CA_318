def make_sum(total, coins):
	# Total is the sum that you have to make and the coins list contains the values of the coins.
	# The coins will be sorted in descending order.
	
	# Place your code here
	greedy_coin_list = [0] * len(coins) # We create a list of zeros the same length as the coins list we read in
	i = 0
	while total > 0: 					# While the total is less than 0
		while i < len(coins): 			# and while i is within the bounds of the coins list
			if coins[i] <= total: 	# if the number at position i is less than or equal to our total
				greedy_coin_list[i] += 1 # We add 1 to that position in our greedy coin list as it means we will use that coin once
				total -= coins[i] 		# We then subtract that value from the total
			else:					# else the number at position i is greater than the total
				i += 1 					# We increment i to check the next coin in the list
	return(greedy_coin_list)

# Test cases used for local testing
#print(make_sum(12, [5,2,1]))
#print(make_sum(157, [7,3,2,1]))