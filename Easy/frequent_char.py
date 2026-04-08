""" 
Write a function, most_frequent_char, that takes in a string as an argument. 
The function should return the most frequent character of the string. 
If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.

"""


def most_frequent_char(s):
    char_count = {} 

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)

    max_val = 0
    max_val_key = ""
    for key in char_count.keys():
        if char_count[key] > max_val:
            max_val = char_count[key]
            max_val_key = key
    return max_val_key
        
    
print(most_frequent_char('bookeeper')) #

print(most_frequent_char("fitufido"))

print(most_frequent_char('mississippi'))