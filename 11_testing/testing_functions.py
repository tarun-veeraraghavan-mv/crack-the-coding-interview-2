# Function to test
def get_temp(temp: int) -> str:
    if temp > 20:
        return "hot"
    else:
        return "cold"
  
def add(a: int, b: int) -> int:
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
