# Decorators @ -> allow to modify the behaviour of a func without modifying the func itself

def longtime(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    return wrapper

@longtime
def hello():
    print('hello')

hello()