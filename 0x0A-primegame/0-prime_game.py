#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    """Return a list of primes up to n using the Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

def simulate_game(n, primes):
    """Simulate the game and determine the winner for a single round."""
    game_state = [True] * (n + 1)
    players = ["Maria", "Ben"]
    current_player = 0  # Maria starts first

    while True:
        move_made = False
        for prime in primes:
            if prime > n:
                break
            if game_state[prime]:
                move_made = True
                for multiple in range(prime, n + 1, prime):
                    game_state[multiple] = False
                current_player = 1 - current_player
                break
        if not move_made:
            break

    # The player who couldn't make a move loses, so the other player wins
    return players[1 - current_player]

def isWinner(x, nums):
    """Determine who won the most rounds."""
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n, primes)
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

