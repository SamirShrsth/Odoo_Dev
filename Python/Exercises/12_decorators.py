# decorators = provides additional functionality to another function
#              function that extends the behaviour of another function

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You added sprinkles.")
        func(*args, **kwargs)
    return wrapper
def add_scoop(func):
    def wrapper(*args, **kwargs):
        print(f"You added another scoop of {kwargs['flavor']}.")
        func(*args, **kwargs)
    return wrapper

@add_scoop
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} Ice Cream")
    
get_ice_cream(flavor = "Chocolate")