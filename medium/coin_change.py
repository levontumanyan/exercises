"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""

def coin_change(coins, amount):
    # Initialize dp array with amount + 1
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    # Iterate through all amounts from 1 to amount
    for i in range(1, amount + 1):
        # For each coin value
        for coin in coins:
            # If the coin value is less than or equal to the current amount
            if coin <= i:
                # Update the dp value for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the dp value for the amount is still amount + 1, return -1
    if dp[amount] == amount + 1:
        return -1

    # Otherwise, return the dp value for the amount
    return dp, dp[amount]

print(coin_change([1, 2, 3], 12))
