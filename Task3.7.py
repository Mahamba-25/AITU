import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

rolls = 1000
totals = [0] * 11

for _ in range(rolls):
    total = roll_dice()
    totals[total - 2] += 1

print("Total   Simulated Percent")
print("-------------------------")

for i in range(11):
    total = i + 2
    simulated_percent = (totals[i] / rolls) * 100

    print(f"{total:5} {simulated_percent:15.2f}%")
