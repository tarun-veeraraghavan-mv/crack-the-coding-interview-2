order = {1: 1, 2: 2}

if 3 in order:
    print("True")
else:
    print("False")

max_key = 1
for key, val in order.items():
    if val > order[max_key]:
        max_key = key

print(max_key)