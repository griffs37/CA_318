from Node import Node
from string import ascii_lowercase

class WordGameNode(Node):
    def __init__(self, name, parent = None):
        # Ensure lowercase letters (no digits or special chars)
        for letter in name:
            assert letter in ascii_lowercase
        self.name = name
        self.parent = parent


    def __str__(self):
        return self.name

    def get_children(self):
        # all one letter mutations of the word
        child_words = []# Your code here
        i = 0
        for c in self.name:
            for x in range(ord("a"), ord("z") + 1):
                if c != chr(x):
                    wordlis = WordGameNode(self.name[:i] + chr(x) + self.name[i+1:])
                    child_words.append(wordlis)
            i += 1
        return child_words

    def get_path(self):
        # insert code here
        return path