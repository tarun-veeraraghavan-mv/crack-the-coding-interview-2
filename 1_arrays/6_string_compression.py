"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints: #92, if 110
"""

def string_compression(sample: str):
    i = 0
    output = ""
    while i < len(sample):
        output += sample[i]
        j = i + 1
        repeat_count = 1
        while j < len(sample) and sample[i] == sample[j]:
            repeat_count += 1
            j += 1
        output += str(repeat_count)
        i = j

    if len(output) > len(sample):
        return sample
    
    return output
          

print(string_compression(sample="aaabbcccaad"))