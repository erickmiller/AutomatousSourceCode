""" Say you have an array for which the ith element is the price of a given stock on day i."""
""" If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit."""

def maxProfit(prices):
	#sorted_prices, max_profit = adjusted_merge_sort(prices)
	max_profit = get_maxProfit(prices)
	return max_profit

# Use O(n)
def get_maxProfit(prices):
	min_so_far = float("inf")
	max_profit_so_far = 0
	for price in prices:
		if (price - min_so_far) > max_profit_so_far:
			max_profit_so_far = (price - min_so_far)
		if price < min_so_far:
			min_so_far = price
	return max_profit_so_far

# Use O(nlogn)
def adjusted_merge_sort(prices):
	length = len(prices)
	if length == 1:
		return prices, 0
	middle_idx = length/2
	first_part, second_part = prices[:middle_idx], prices[middle_idx:]
	first_sorted, first_max_profit = adjusted_merge_sort(first_part)
	second_sorted, second_max_profit = adjusted_merge_sort(second_part)
	max_profit = second_sorted[-1] - first_sorted[0]
	if max_profit < first_max_profit:
		max_profit = first_max_profit
	if max_profit < second_max_profit:
		max_profit = second_max_profit
	new_sorted = []
	i, j = 0, 0
	while i<len(first_sorted) and j<len(second_sorted):
		if first_sorted[i] < second_sorted[j]:
			new_sorted.append(first_sorted[i])
			i += 1
		else:
			new_sorted.append(second_sorted[j])
			j += 1
	while i < len(first_sorted):
		new_sorted.append(first_sorted[i])
		i += 1
	while j < len(second_sorted):
		new_sorted.append(second_sorted[j])
		j += 1
	return new_sorted, max_profit

if __name__ == '__main__':
	prices = [4, 5, 2, 10, 1, 3]
	print maxProfit(prices)
