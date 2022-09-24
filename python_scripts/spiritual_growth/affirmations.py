import random

repeat_count = 5

with open('affirmations.txt') as f:
    afrm = random.choice([x.strip() for x in f.readlines() if x.strip()])

print(afrm)
print(f"Affirm by typing {repeat_count} times")
for i in range(repeat_count):
    input(f"{i+1}. ")
