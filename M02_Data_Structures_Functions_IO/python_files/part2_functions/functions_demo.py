"""Part 2: functions, defaults, returning tuples, scope and the mutable default trap.

Run:  python functions_demo.py
"""


# ======================================================================
# 1. Defining and calling
# ======================================================================

def fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


print(fahrenheit(21.5))       # 70.7
print(fahrenheit.__doc__)     # the docstring, retrieved at run time


# ======================================================================
# A function with no `return` gives back `None`
# ======================================================================

def report(value):
    print(f"Value is {value}")      # prints, but does not return anything


result = report(42)
print("result holds:", result)       # None


# ======================================================================
# 2. Default values and keyword arguments
# ======================================================================

def shipping_cost(weight_kg, zone, express=False):
    """Return a shipping cost. Zone 1 is cheaper; express adds 50%."""
    rate = 4.0 if zone == 1 else 6.5
    cost = weight_kg * rate
    return cost * 1.5 if express else cost


print(shipping_cost(2, 1))                        # positional:        8.0
print(shipping_cost(2, zone=3, express=True))     # keywords read well: 19.5


# ======================================================================
# 3. Returning more than one value
# ======================================================================

def extremes(values):
    """Return the smallest and largest value as a tuple."""
    return min(values), max(values)


low, high = extremes([4, 9, 1])
print(f"low={low}, high={high}")
print("What actually came back:", extremes([4, 9, 1]), type(extremes([4, 9, 1])))


# ======================================================================
# 4. Scope
# ======================================================================

total = 0


def add_one_broken():
    # "total += 1" means "total = total + 1". The assignment makes total
    # local to this function, so the read on the right-hand side finds a
    # local variable that has no value yet.
    total += 1
    return total


try:
    add_one_broken()
except UnboundLocalError as error:
    print("UnboundLocalError ->", error)


# ======================================================================
# The fix: pass it in, return it out
# ======================================================================

def add_one(value):
    """Return value plus one. Touches nothing outside itself."""
    return value + 1


total = 0
total = add_one(total)
total = add_one(total)
print("total:", total)


# ======================================================================
# 5. The mutable default argument trap
# ======================================================================

def add_wrong(item, bucket=[]):
    bucket.append(item)
    return bucket


print(add_wrong("a"))     # ['a']
print(add_wrong("b"))     # ['a', 'b']   the list from the first call is still there
print(add_wrong("c"))     # ['a', 'b', 'c']

def add_right(item, bucket=None):
    # None is immutable, so it is safe as a default.
    # A new list is created on every call that needs one.
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(add_right("a"))     # ['a']
print(add_right("b"))     # ['b']    independent, as intended
