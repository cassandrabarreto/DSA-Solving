"""

Write a function, uncompress, that takes in a string as an argument. The input string will be formatted 
into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group is 
repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously 
mentioned pattern.
"""

def uncompress(s):
    # keep incrementing J until we find a character
    # i represents the start of the number portion
    # j represents the end of the number portion
    # set i equal to j
    # s[i:j] --> number portion
    i = 0
    j = 0
    numbers = "123456789"
    result = []

    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j
    return ''.join(result)





