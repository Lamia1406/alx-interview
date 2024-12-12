#!/usr/bin/python3
""" This module determines the winner in a prime game"""


def sieve_of_eratosthenes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]


def simulate_game(n):
    """Simulate the game for a given n and return the winner."""
    primes = sieve_of_eratosthenes(n)
    available_numbers = set(range(1, n + 1))

    turn = 0
    while True:
        prime = None
        for p in primes:
            if p in available_numbers:
                prime = p
                break

        if prime is None:
            if turn == 0:
                return "Ben"
            else:
                return "Maria"

        for i in range(prime, n + 1, prime):
            available_numbers.discard(i)

        turn = 1 - turn


def isWinner(x, nums):
    """Simulate multiple rounds and return the name of the player
    who wins the most rounds."""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
