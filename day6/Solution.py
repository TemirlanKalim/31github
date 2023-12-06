class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      # Edge case: if the array has fewer than 2 days, the profit is 0
      if len(prices) < 2:
          return 0
      
      # Initialize profit
      profit = 0
      
      # Iterate through the prices starting from the second day
      for i in range(1, len(prices)):
          # Calculate the difference between the current and previous day's prices
          price_difference = prices[i] - prices[i - 1]
          
          # If the price difference is positive, add it to the profit
          if price_difference > 0:
              profit += price_difference
      
      return profit
