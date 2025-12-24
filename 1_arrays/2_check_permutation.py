"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

"""
Sorting
"""
def check_permutation_1(string1: str, string2: str):
    if (len(string1) != len(string2)):
        return False

    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    if sorted_string1 == sorted_string2:
        return True
    
    return False

"""
Using a hash map
"""
def check_permutation_2(string1: str, string2: str):
    map1 = {}
    map2 = {}

    for char in string1:
        if char in map1:
            map1[char] += 1
        else:
            map1[char] = 1

    for char in string2:
        if char in map2:
            map2[char] += 1
        else:
            map2[char] = 1

    return map1 == map2

res1 = check_permutation_1("abc","abc")
res2 = check_permutation_1("cbab","aabc")

res3 = check_permutation_2("abc","abc")
res4 = check_permutation_2("cbab","aabc")

print(res1)
print(res2)