#
#   Use this class definition to work from.
#   This way of reading the dictionary is quete messy.
#   It is done this way to make testing easier.
#
from Node import Node
from string import ascii_lowercase
from read_dictionary import read_dictionary

valid_words = None

def is_valid(words):
    return words.isalpha() and words.islower()

class WordGameNode(Node):
    def __init__(self, name, parent = None):
        # Ensure lowercase letters (no digits or special chars)
        for letter in name:
            assert letter in ascii_lowercase

        global valid_words
        if valid_words == None or len(valid_words) != len(name):
        # We only need to examine words which have the same length as our word (self.name)
            valid_words = read_dictionary("/etc/dictionaries-common/words", len(name))
        self.name = name
        self.parent = parent

    def __str__(self):
        return self.name

    def get_children(self):
        child_words = [] # your code here
        i = 0
        for l in self.name:
            for j in range(ord("a"), ord("z") + 1):
                if l != chr(j):
                    word = WordGameNode(self.name[:i] + chr(j) + self.name[i+1:])
                if word.name in valid_words:
                    child_words.append(word)
            i +=1
        
        return child_words # your code here

    def get_path(self):
      # insert code here
        return path