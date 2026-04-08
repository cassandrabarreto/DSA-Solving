""" 
Write a function, fizz_buzz, that takes in a number n as an argument. 
The function should return a list containing numbers
from 1 to n, replacing certain numbers according to the following rules:

if the number is divisible by 3, make the element "fizz"
if the number is divisible by 5, make the element "buzz"
if the number is divisible by 3 and 5, make the element "fizzbuzz"
"""

def fizzbuzz(num):
    result = []
    for i in range(1, num):
        if i % 3 == 0 and i% 5 == 0:
            i = "fizzbuzz"
            result.append(i)
            continue
        if  i% 5 == 0:
            i = "buzz"
            result.append(i)
            continue
        if  i% 3 == 0:
            i = "fizz"
            result.append(i)
            continue
        result.append(i)
    return result
    
print(fizzbuzz(11))