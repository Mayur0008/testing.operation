def a(c, d):
    return c - d  # subtraction function


def b(c, d):
    return c * d  # multiplication function

def operation(x, y):
    subtraction = a(x,y)
    multiplication = b(x,y)
    print(f"the sub of{x} and {y}is: {subtraction}")
    print(f"the multi of{x} and {y}is: {multiplication}")

operation(7,5)

