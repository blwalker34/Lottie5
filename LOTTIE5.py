#LOTTIE

import random

print("LOTTIE Says Welcome!")
print("LOTTIE will select your winning Lotto 6-49 numbers for you")

count = 0
picks = []

def remove_duplicates(lst):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res

while count <= 5:
    pick = random.randint(1, 49)
    picks.append(pick)
    count += 1

my_picks = remove_duplicates(sorted(picks))

print(my_picks)
print("Good luck!")
