import random

class WordFinder():
    
    """Word Finder: finds random words from a dictionary.
    
        >>> wf = WordFinder("words.txt")
        235886 words read
    

    """

    def __init__(self, file):
        self.filename = file
        self.lines = self.read_file(self.filename)
        self.print_report(len(self.lines))

    def read_file(self, filename):
        
        """Read the file and populate a list with each line after stripping the newline"""
        
        self.file = open(filename, "r")
        self.lines = self.file.readlines()
        self.lines = [line.strip() for line in self.lines]
        return self.lines
    
    def print_report(self, num):

        """Print results"""

        print(f"{num} words read")

    def random(self):

        """Return a random word from the list of words"""

        random_num = random.randint(0, len(self.lines)) - 1
        return self.lines[random_num]
    
class SpecialWordFinder(WordFinder):

    """Subclass of WordFinder that discards commented ("#") and empty lines"""

    def __init__(self, file):

        """Get parent class"""
        super().__init__(file)

    def read_file(self, filename):
        self.lines = super().read_file(filename)
        self.lines = [word for word in self.lines if word != "" and not word.startswith("#")]
        return self.lines