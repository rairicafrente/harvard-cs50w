def announce(f) :
    def wrapper() :
        print("Running function f")
        f()
        print("Function f has completed")
    return wrapper

@announce
def hello() :
    print("This is the hello func")

hello()
