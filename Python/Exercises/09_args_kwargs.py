# *args returns a tuple ()
# **kwargs returns a dict {key : value}

def get_info(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
        
    for key, value in kwargs.items():
        print(f"{key} : {value}")
# args: "Samir", "Shrestha" & **kwargs: "city = 'Kathmandu" & "country='Nepal"
get_info("Samir", "Shrestha", city="Kathmandu", country = "Nepal")