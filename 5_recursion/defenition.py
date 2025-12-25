# Recursion: function that calls itself. Has a base case and the function call

def factorial(num: int):
    if num == 1:
        return 1
    return num * factorial(num=num-1)