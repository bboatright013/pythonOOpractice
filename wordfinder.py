"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """ reads a text document
        and returns then unmber of words eache on a sperate line
        that it read and then lets the user pick some
        at random
    """
    def __init__(self, text_file):
        """ constructor for the list of words from file 
        """

        self.words = []
        the_file = open(text_file, "r")
        for line in the_file:
            length = len(line) - 1
            return_string = line[0:length]
            self.words.append(return_string)
        print(f"{len(self.words)} words read")
    
    def random(self):
        num = randint(0, len(self.words)-1)
        return self.words[num]

class SpecialWordFinder(WordFinder):
    """  
    more advanced wordfinder
    that fileters blank 
    lines and comments
    """
    def __init__(self, text_file):
        super().__init__(text_file)
        tmp_list = []
        for x in range(0,len(self.words) - 1):
            if self.words[x] != "" and self.words[x] != "#":
                tmp_list.append(self.words[x])
        self.words = tmp_list.copy()
        print(f"{len(self.words)} words in list")

        



        
