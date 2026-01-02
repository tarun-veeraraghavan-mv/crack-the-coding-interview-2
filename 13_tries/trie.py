# good video boi: https://www.youtube.com/watch?v=y3qN18t-AhQ

class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                current_node.children[c] = Node()

            # shift current node pointer to the new node
            current_node = current_node.children[c]

        # After loop set the end of word to True
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                return False
            
            current_node = current_node.children[c]

        return current_node.is_end_of_word
    
    def starts_with(self, prefix):
        current_node = self.root

        for c in prefix:
            if c not in current_node.children:
                return False
            
            current_node = current_node.children[c]

        return True

    
