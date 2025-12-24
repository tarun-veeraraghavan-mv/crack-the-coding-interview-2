"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale , pae - > true
pales , pale - > true
pale , bale - > true
pale , bake - > false
Hints: #23, #97, it 130
"""

def one_away(a: str, b: str):
    # if changes is more than 1, then it is False
    if abs(len(a) > len(b)) > 1:
        return False
    
    i, j = 0, 0
    difference = 0

    while i < len(a) and j < len(b):
        # if same chars increase pointer
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            # increase the difference as chars is not equal
            difference += 1
            if difference > 1:
                return False
            
            # if a longer than b increase first chars counter
            if len(a) > len(b):
                i += 1
            # if b longer than a increase first chars counter
            elif len(a) < len(b):
                j += 1
            # if both equal move both
            else:
                i += 1
                j += 1

    return True

print(one_away(a="abc", b="abcd"))
print(one_away(a="cde", b="cas"))