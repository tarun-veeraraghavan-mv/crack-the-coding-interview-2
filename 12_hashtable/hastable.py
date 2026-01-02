class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        # Custom hash method
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        hash = self.__hash(key=key)
        if self.data_map[hash] == None:
            self.data_map[hash] = []
        self.data_map[hash].append([key, value])

    def get_item(self, key):
        hash = self.__hash(key=key)
        if self.data_map[hash] is not None:
            for item in self.data_map[hash]:
                if item[0] == key:
                    return item
        return f"No item found for key: {key}"
    
    def keys(self):
        all_keys = []
        for i in self.data_map:
            if i is not None:
                for j in i:
                    all_keys.append(j[0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}: {val}")

my_hash_table = HashTable()
my_hash_table.set_item(key="nails", value=1000)
my_hash_table.set_item(key="lumber", value=1000)
my_hash_table.set_item(key="washers", value=1000)
print(my_hash_table.get_item(key="nails"))
print(my_hash_table.get_item(key="nail"))
print(my_hash_table.keys())
# my_hash_table.print_table()