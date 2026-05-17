""" 
Write a function, compress, that takes in a string as an argument. The function 
should return a compressed version of the string where consecutive occurrences of
 the same characters are compressed into the number of occurrences followed 
by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
"""

def compress(s: str) -> str:
    i = 0
    j = 0 
    final_result = []
    s += "!"
    
    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
            count = j - i
            if count == 1:
                final_result.append(s[i])
            else:
                final_result.append(str(count) + s[i])
            i = j
    return "".join(final_result)


