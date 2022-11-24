'''
7. Reverse Integer | Medium
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
-----------------------------------------------------------------------------------------------------------------
One approach could be to convert the given integer to a string then convert it back to an int after reversing.

A better solution is to use pop and push, this is a log(n) time and O(1) space solution
'''


def reverseIntPopPush(x: int) -> int:
    res, sign = 0, 1
    INT_MAX, INT_MIN = 2 ** 31 - 1, -(2 ** 31)  # 2147483647, -2147483648

    # Since -3 % 10 == 7 and not -3 in python3, we need to ensure x is +ve
    # If x <= INM_MIN then converting it to +ve will result in integer overflow
    if x < 0:
        sign = -1

        if x <= INT_MIN:
            return 0
        
        x = -x

    while x:
        pop = x % 10
        x = x // 10

        if res > INT_MAX // 10 or (res == INT_MAX and pop > 7):
            return 0
        
        if res < INT_MIN // 10 or (res == INT_MIN and pop < -8):
            return 0
        
        res = res * 10 + pop

    return sign * res
