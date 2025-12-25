"""
String Rotation; Assume you have a method isSubs t rin g which checks if one word is a substring
of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one
call to isSubs t rin g [e.g., "wate r bottle " is a rotation oP'erbottlewat"),
"""

# Logic: if a string is the rotation of another string then the s2 will be 
# present in s1 + s1

def string_rotation(s1: str, s2: str):
    # if lengths are not equal then they are not rotations
    if len(s1) != len(s2):
        return False
    
    combined_string = s1 + s1

    if s2 in combined_string:
        return True
    else:
        return False
    
print(string_rotation(s1="waterbottle", s2="oPerbottlewat"))