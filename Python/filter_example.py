# filter()

numbers = [1, 2, 3]

def isEven(n): # we can use a lambda func instead:
    return n % 2 == 0 # isEven = lambda n : n % 2 == 0

result = filter(isEven, numbers) # result = filter(lambda n : n % 2 == 0, numbers)

print(list(result)) # [2]