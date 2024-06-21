# Decorators
# a function that takes another function as an argument and extends its functionality

# like if we want to add a cover to a phone
# just to decorate it

def add_cover(func):
    def wrapper():
        print("Adding cover to the phone")
        func()
        print("Cover added")
    return wrapper

@add_cover
def make_phone():
    print("Making phone")

make_phone()