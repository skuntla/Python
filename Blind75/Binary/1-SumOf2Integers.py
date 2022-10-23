'''Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5

2 = 10
3 = 11
'''

a = 7
b = 6


def binary(num):
    binary_num = ""
    while num>=1:
        binary_dig = num%2
        num = int(num/2)
        binary_num = str(binary_dig) + binary_num
    return binary_num

print(binary(89))



