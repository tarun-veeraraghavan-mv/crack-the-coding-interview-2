"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn Smit h 13
Output: "Mr%203ohn%20Smith"

The catch is to not create a new array and to do it in place.
"""

def urlify_1(string1: str, true_length: int):
    sample = string1.split(" ")
    print(sample)
    print("%20".join(sample))

def urlify_2(string1: str, true_length: int):
    string1.replace(" ", "%20")

urlify_1(string1="aaa bbb ccc ddd", true_length=12)

def loop_back(num: int):
    for i in range(num-1, -1, -1):
        print(i)

loop_back(5)