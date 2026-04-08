""" 
Write a function, anagrams, that takes in two strings as arguments.
The function should return a boolean indicating whether or not the strings are anagrams. 
Anagrams are strings that contain the same characters, but in any order.    
"""

def anagrams(first_word, second_word):
    first_word_count = {}
    second_word_count = {}
    
    for element in first_word:
        if element in first_word_count:
            first_word_count[element] += 1
        else:
            first_word_count[element] = 1
    
    for element in second_word:
        if element in second_word_count:
            second_word_count[element] += 1
        else:
            second_word_count[element] = 1
        
    if first_word_count == second_word_count:
        return True
    else:
        return False


print(anagrams('restful', 'fluster')) # -> True

anagrams('cats', 'tocs') # -> False

anagrams('elbow', 'below') # -> True

anagrams('pp', 'oo') # -> false