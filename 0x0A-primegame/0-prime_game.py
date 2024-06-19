#!/usr/bin/python3
"""
0-prime_game module
"""

def sieve(n):
    """ Generate a list of prime numbers up to n using the Sieve of Eratosthenes. """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]

def isWinner(x, nums):
    """
    Determine the winner of the prime game after x rounds.
    
    Args:
    x (int): Number of rounds.
    nums (list of int): List containing the 'n' value for each round.
    
    Returns:
    str: Name of the player that won the most rounds, or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve(max_n)
    
    # Create a list to record the winner for each n
    win_for_n = [0] * (max_n + 1)

    for i in range(2, max_n + 1):
        # Determine the winner for current i
        moves = 0
        for prime in primes:
            if prime > i:
                break
            if win_for_n[i - prime] == 0:
                moves += 1
        win_for_n[i] = 1 if moves % 2 == 1 else 0  # Maria wins if moves are odd, else Ben wins
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if win_for_n[n] == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
