#!/usr/bin/python3
"""
A python function that choses a winner
"""


def isWinner(x, nums):
    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(n + 1) if is_prime[p]]

    def play_game(n, primes):
        prime_set = set(primes)
        moves = 0
        remaining = set(range(1, n + 1))

        for prime in primes:
            if prime in remaining:
                moves += 1
                multiples = set(range(prime, n + 1, prime))
                remaining -= multiples

        return "Maria" if moves % 2 == 1 else "Ben"

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
