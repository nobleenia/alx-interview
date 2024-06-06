#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    # Initialize DP array with a high value
    # (greater than the maximum possible number of coins)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the DP array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'),
    # it means we cannot make the total with given coins
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    # Example usage
    print(makeChange([1, 2, 25], 37))  # Should return 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Should return -1
