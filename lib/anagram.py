# your code goes here!
class Anagram:

    def __init__(self, word):
        self.words = sorted([letter for letter in word])
        