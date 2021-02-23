def read_dictionary(filename, length):
    
    # your code here
    words = []
    for line in open(filename):
        word = line.strip()
        if valid_words(word) and len(word) == length:
            words.append(word)
    return words # a list of the words in the dictionary which comprise only lower case letters and are of the correct lengt

def valid_words(words):
    return words.isalpha() and words.islower()