from typing import List
from datetime import datetime

'''
66. Plus One | Easy
You are given a large integer represented as an integer array digits, where each digits[i] is
the ith digit of the integer. The digits are ordered from most significant to least significant
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
------------------------------------------------------------------------------------------------

'''


def plusOne(digits: List[int]) -> List[int]:
    digits[-1], carry = (digits[-1] + 1) % 10, (digits[-1] + 1) // 10

    for i in range(len(digits) - 2, -1, -1):
        num = digits[i] + carry
        digits[i], carry = num % 10, num // 10
    
    if carry:
        digits = [carry] + digits
    
    return digits


print(isinstance(datetime.utcnow(), datetime))
print(datetime.utcnow())