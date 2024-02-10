# map()

numbers = [1, 2, 3]

def double(a): # we can use a lambda func instead:
    return a * 2 # double = lambda a : a * 2

result = map(double, numbers) # result = map(lambda a : a * 2, numbers)

print(list(result)) # [2, 4, 6]