# Just as int() turns things into integers & float() turns them into floats/decimal, bool() turns things into boolean
# All numbers are TRUE except 0
# All strings are TRUE except empty string

print(bool(1))
print(bool(0))
print(bool("sohail"))
print(bool(""))

# When '+' sign is placed btw boolean values, Python begins to treat them as integers
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (int(ketchup) + int(mustard) + int(onion)) == 1