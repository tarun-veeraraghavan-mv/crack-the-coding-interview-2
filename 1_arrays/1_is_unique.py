"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

"""
Brute force
"""
def is_unique1(string: str):
    string_length = len(string)
    # double for loop
    for i in range(string_length):
        for j in range(i+1, string_length):
            if string[i] == string[j]:
                return False
            
    return True

"""
If can use a data structure, the hash set will be the correct one
"""
def is_unique2(string: str):
    # create a new set
    chars = set()
    for ch in string:
        # if char in the set add it in the set
        if ch not in chars:
            chars.add(ch)
        else:
        # if already present in the set return False
            return False
        
    return True
          

"""
By sorting
"""
def is_unique3(string: str):
    # sort the given string
    sorted_string = sorted(string)
    print(f"Sorted string is: {sorted_string}")

    # loop through and check if any adjacent strings are the same
    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i+1]:
            return False

    return True

res1 = is_unique1("abc")
res2 = is_unique1("abcbc")

res3 = is_unique2("abc")
res4 = is_unique2("abcbc")

res5 = is_unique3("abc")
res6 = is_unique3("abcbc")

print(res1)
print(res2)

print(res3)
print(res4)

print(res5)
print(res6)