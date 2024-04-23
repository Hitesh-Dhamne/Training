def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(arg for arg in args)
        kwargs_values = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_values}")

        result = func(*args, **kwargs)

        return result
    return wrapper

@debug
def greet(name, greeting):
    print(f"{name}, {greeting}")

greet("soham", "hell")
