import Memory
import re
class Loader:
    def __init__(self):
        self.memory = Memory.Memory()     #initializes the memory
        self.line = 1
        self.output = ""
        self.pattern = r'^[+-]?[0-9]+$'
    def load_file(self, path):
        file = path                                 #grab file from path: pyqt6 widget --> windows dialog box
        try:
            with open(file, "r", encoding="utf8") as f:       #opens file
                for x in f:
                    word = x[0:-1] #set word to one smaller than word length to remove newline
                    if self.line == 100: #on last line there wont be newline
                        word = x[:]
                    if re.match(self.pattern, word) is None:
                        self.output += "Incorrect input format on line " + str(self.line) + "\n"
                    if len(word) != 5:      #if word is longer than 5 chars throw an error
                        self.output += "Incorrect input format on line " + str(self.line) + "\n"
                    self.memory.mem[self.line - 1] = word     #add the word to memory at line minus 1
                    self.line += 1
        except FileNotFoundError:
            self.output += "No file selected. Please select a file\n"
        return self.memory.mem