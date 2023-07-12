import Memory
class Loader:
    def __init__(self):
        self.memory = Memory.Memory()     #initializes the memory
        self.line = 1
        self.output = ""
    def load_file(self, path):
        file = path                                 #grab file from path: pyqt6 widget --> windows dialog box
        try:
            with open(file, "r", encoding="utf8") as f:       #opens file
                for x in f:
                    word = x[0:-1] 
                    if word == "":
                        self.memory.mem[self.line - 1] = word     #add the word to memory at line minus 1
                        self.line += 1
                        continue         #set word to one smaller than word length to remove newline
                    if len(word) != 5:      #if word is longer than 5 chars throw an error
                        raise ValueError("incorrect input format on line " + str(self.line))
                    if (word[0] != '+') and (word[0] != '-'):   #if word doesn't start with + or - throw an error
                        raise ValueError("incorrect input format on line " + str(self.line))
                    

                    self.memory.mem[self.line - 1] = word     #add the word to memory at line minus 1
                    self.line += 1
        except FileNotFoundError:
            self.output += "No file selected. Please select a file\n"
        return self.memory.mem