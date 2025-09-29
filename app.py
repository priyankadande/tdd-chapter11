def add(a, b):
    """Simple addition function"""
    return a + b

def divide(a, b):
    """Division with error handling"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
