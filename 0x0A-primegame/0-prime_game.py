#!/usr/bin/python3
"""Prime game problem"""


def isWinner(x, nums):
    """isWinner method"""
    def is_prime(num):
        """Check if num is prime"""
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def calculate_winner(n):
        """Calculate the actual winner"""
        prime_numbers = [i for i in range(2, n + 1) if is_prime(i)]
        if len(prime_numbers) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = calculate_winner(n)
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
