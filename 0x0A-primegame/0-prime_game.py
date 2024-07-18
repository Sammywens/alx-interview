#!/usr/bin/python3
'''Prime Game
'''
from typing import List

def isWinner(x: int, nums: List[int]) -> str:
    ''' This function takes turns choosing a prime number
    from the set and removing that number and its multiples from the set.
    The player that cannot make a move loses the game
    '''
    
    def sieve_of_eratosthenes(max_n: int) -> List[int]:
        """ Return a list of primes up to max_n using Sieve of Eratosthenes. """
        if max_n < 2:
            return []
        is_prime = [True] * (max_n + 1)
        p = 2
        while (p * p <= max_n):
            if (is_prime[p] == True):
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, max_n + 1) if is_prime[p]]
        return prime_numbers
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    # Precompute can_win for all values up to max_n using the list of primes
    can_win = [False] * (max_n + 1)
    for i in range(2, max_n + 1):
        for prime in primes:
            if i - prime >= 0 and not can_win[i - prime]:
                can_win[i] = True
                break
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if can_win[n]:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

