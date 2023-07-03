class Loader:
    def __init__(self):
        self.mem = ["-0000"] * 100     #initializes the memory
        self.line = 1
        self.output = ""
    def load_file(self, path):
        file = path                                 #grab file from path: pyqt6 widget --> windows dialog box
        try:
            with open(file, "r", encoding="utf8") as f:       #opens file
                for x in f:
                    if x in ("-99999"):
                        f.close()
                        break                 #if word is -99999, stop reading and close the file
                    word = x[0:-1]          #set word to one smaller than word length to remove newline
                    if len(word) != 5:      #if word is longer than 5 chars throw an error
                        raise ValueError("incorrect input format on line " + str(self.line))
                    if (word[0] != '+') and (word[0] != '-'):   #if word doesn't start with + or - throw an error
                        raise ValueError("incorrect input format on line " + str(self.line))
                    self.mem[self.line - 1] = word     #add the word to memory at line minus 1
                    self.line += 1
        except FileNotFoundError:
            self.output += "No file selected. Please select a file\n"
        return self.mem
