#!/usr/bin/python3
""" Solving prime game problem """


def isWinner(x, nums):
    """A method that checks for the winner"""
    # Check for invalid input cases
    if not nums or x < 1:
        return None

    # Find the maximum number among all rounds
    max_num = max(nums)

    # Create a list to mark prime numbers using a Boolean approach
    prime_nums = [True for _ in range(max(max_num + 1, 2))]

    # Use a sieve-like algorithm to mark non-prime numbers
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not prime_nums[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            prime_nums[j] = False

    # Mark 0 and 1 as non-prime
    prime_nums[0] = prime_nums[1] = False

    # Calculate a cumulative count of prime numbers up to each index
    y = 0

    for i in range(len(prime_nums)):
        if prime_nums[i]:
            y += 1
        prime_nums[i] = y

    # Initialize a counter for player 1 (Maria)
    player_1 = 0

    # Count the number of prime numbers chosen by player 1 in each round
    for x in nums:
        player_1 += prime_nums[x] % 2 == 1

    # Determine the winner based on the number of prime numbers chosen
    if player_1 * 2 == len(nums):
        return None  # It's a tie
    if player_1 * 2 > len(nums):
        return "Maria"  # Maria wins if she chose more prime numbers

    return "Ben"  # Ben wins if he chose more prime numbers
