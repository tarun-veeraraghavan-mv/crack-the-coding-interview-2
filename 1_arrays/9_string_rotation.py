"""
String Rotation; Assume you have a method isSubs t rin g which checks if one word is a substring
of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one
call to isSubs t rin g [e.g., "wate r bottle " is a rotation oP'erbottlewat"),
"""

def string_rotation(s1: str, s2: str):
    new_s1 = "".join(sorted(s1))
    new_s2 = "".join(sorted(s2))

    print(new_s1, new_s2)

    if new_s2 in new_s1:
        return True
    else:
        return False
    
print(string_rotation(s1="waterbottle", s2="oPerbottlewat"))