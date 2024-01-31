import random

lottery_numbers = sorted(random.sample(range(1, 50), 6))
print("Your Lottery Ticket Numbers:", *lottery_numbers)
