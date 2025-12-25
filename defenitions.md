## Defenitions

1. Permutation: Rearrangement of charecters, If 2 strings have the same charecters, with the same count but in a different
   order then one is a permutation of another

Example: 'abc' -> 'bca', 'aabb' -> baab' or 'abba'

## Checks you need to do for different data types

Thinking of edge cases is the difference between a "Junior" and a "Senior" developer. The trick is to stop thinking about how the code works and start thinking about how to break it.

You don't have to be a genius; you just need a Checklist. Every time you see a data structure, run these "stress tests" in your head:

1. The "Numbers" Stress Test
   If the problem involves math or counting (like URLify or Sum Lists), check:

Zero/Empty: What if the string is "" or the number is 0?

The Single: What if there is only 1 character or 1 node?

The Maximums: What if the numbers are huge (causing an overflow)?

Negatives: Does the logic break if a number is -5?

2. The "Linked List" Stress Test
   Linked lists are the "kings" of edge cases because of those None (null) pointers.

The Empty List: l1 is None. Does your code crash on l1.val? (This is why we use if l1: v1 = l1.val else: 0).

Different Lengths: What if l1 has 5 nodes but l2 has only 1?

The Final Carry: This is the most famous one. Does your code forget the last carry?

Example: 9 + 1. If your code output is 0 instead of 0 -> 1, you missed the "Final Carry" edge case.

3. The "String & Array" Stress Test
   Empty/Null: Always check if the input is None or "".

All Spaces: For URLify, what if the string is just " "?

No Spaces: What if the string has zero spaces? Does your new_index math still work?

The Boundary: If you are looping from 0 to N-1, check the very first and very last index. Usually, bugs hide at the edges (indices 0 and len-1).
