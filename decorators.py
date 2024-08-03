def announce(f):
    def wrapper():
        print(f"About to run the function: {f.__name__}")
        f()
        print("Done with the function")
    return wrapper


@announce
def hello():
    print("Hello world!")

hello()