"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn Smith    13
Output: "Mr%203ohn%20Smith"

The catch is to not create a new array and to do it in place.
"""

# Logic is Input is the string and the true_length which is somehting like 'Mr_John_Smith____' and 13.
# 13 is the Mr_John_Smith and the extra '____' is the spaces for the %20.
# Why the extra 4 space? Because 1 space should be replaced with '%20' meaning we need 2 extra chars
# For 2 space we need 4 more to accomodate the '20' string

def URLify(input: str, true_length: int):
    input = list(input)
    # count the number of spaces in the string within the true length. This will be used to 
    # calculate the end index of the string
    space_count = 0
    for i in range(true_length - 1):
        if input[i] == " ":
            space_count += 1

    # calculate the final string index 
    # true length from input, 2 from the '20' count , -1 as we will use this as an index
    new_index = true_length + (2 * space_count) - 1 

    # looping backward making it easier to make changes to the string
    # one pointer which goes backward from the true length 
    # another pointer in the end of the final string
    for i in range(true_length - 1, -1, -1):
        if input[i] != " ":
            # if not a space we simply put this in the back 
            input[new_index] = input[i]
            new_index -= 1
        else:
            # if input[i] == " ":
            input[new_index] = "%"
            input[new_index - 1] = "0"
            input[new_index - 2] = "2"
            new_index -= 3

    return "".join(input)

print(URLify(input="Mr John Smith    ", true_length=13))