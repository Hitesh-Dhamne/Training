def decorate(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

@decorate
def print_name():
    print('soham')

print_name()