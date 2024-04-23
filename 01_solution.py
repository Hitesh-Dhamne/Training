import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

'''@timer
def times(n):
    time.sleep(n)

times(2)'''

@timer
def greet(name):
    print(f'{name} Hello World!')

greet("soham")