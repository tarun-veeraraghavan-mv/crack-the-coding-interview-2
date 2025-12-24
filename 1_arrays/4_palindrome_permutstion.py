"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation

is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tac t Coa
Output: Tru e (permutations : "tac o cat" , "atc o eta" , etc. )
Hints: #106, h 0134, § 136
"""

# Tip: A palindrome can have at most one character with an odd count and al others  
# must have even counts to be a permutation

def palindrome_permutation(sample: str):
    counts = {}

    for char in sample:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    odd_count = 0
    for key, val in counts.items():
        if val % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
            
    return True

print(palindrome_permutation(sample="tac t coa"))
print(palindrome_permutation(sample="abac"))

