import random
from itertools import permutations 

# Naïve shuffle
def naive(cards):
    for i in range(len(cards)):
        n = random.randint(0, len(cards)-1)
        cards[i], cards[n] = cards[n], cards[i]
    return cards

# Fisher–Yates shuffle
def fisher_yates(cards):
    for i in range(len(cards)-1, 0, -1):
        n = random.randint(0, i)
        cards[i], cards[n] = cards[n], cards[i]
    return cards

# simulate 10^6 times
def shuffle_simulation(shuffle_func, times=1000000):
    cards = [1,2,3,4]
    perm = permutations(cards)
    perm_count = {}
    for p in perm:
        perm_count[p] = 0

    for _ in range(times):
        shuffled_cards = shuffle_func(cards.copy())
        perm_count[tuple(shuffled_cards)] += 1

    return perm_count

# output
naive_result = shuffle_simulation(naive)
fisher_yates_result = shuffle_simulation(fisher_yates)

print("Naive algorithm:")
for perm in naive_result:
    print(f"{perm}: {naive_result[perm]}")

print("\nFisher-Yates shuffle:")
for perm in fisher_yates_result:
    print(f"{perm}: {fisher_yates_result[perm]}")