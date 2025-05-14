# 1. You are given a list of words. Write a Python function to find the longest compound word in the list. A compound word is defined as a word that can be formed by combining two or more shorter words in the list. You can assume that the list of words contains only lowercase alphabetical characters and does not contain duplicates.

# Example Output:
# "Catsdogcats


# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.

def word_break(word,st):
    if len(word)==0 or word in st:
        return True
    
    for i in range(1,len(word)):
        if word[:i] in st:
            if word_break(word[i:],st)==True:
                return True
    if len(word)>0:
        return False
    return True



words = ["cat", "cats", "", "dog", "hippopotamus", "rat", "ratcatdog"]

st=set(words)
print(word_break("catsdogckats",st))