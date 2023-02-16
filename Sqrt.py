'''
69. Sqrt(x) | Easy
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
------------------------------------------------------------------------------------------------
O(n) approach is to check all numbers between 2 and n / 2
O(log(n)) approach uses Newton's method
'''


def sqrt(num: int) -> int:
    x = num

    while True:
        root = 0.5 * (x + (num / x))

        if x == root:
            break

        x = root
    
    return int(root)