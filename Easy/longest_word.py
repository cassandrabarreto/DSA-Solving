
def longest_word(phrase):
    phrase_list = phrase.split()
    max_word = ""

    for word in phrase_list:
        if len(word) >= len(max_word):
            max_word = word
    return max_word


phrase = "have a nice day"

print(longest_word(phrase))