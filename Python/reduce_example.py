# reduce()
from functools import reduce

expenses = [
    ('Dinner', 80),
    ('Car Repair', 120)
]

#sum = 0
#for expense in expenses:
#    sum += expense[1]

sum = reduce(lambda a, b : a[1] + b[1], expenses)

print(sum)