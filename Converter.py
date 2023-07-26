import Memory

class Converter:
    """creates an object to convert old code to new code"""
    def __init__(self):
        self.memory = Memory.Memory()
        self.mem_limit = self.memory.mem_limit
        self.mem = [""] * self.mem_limit     #initializes the memory
    def convert(self, old_mem):
        """coverts old 4 digit code into new 6 digit code"""
        i = 0

        while i < len(old_mem):
            old_str = old_mem[i]
            new_str = ""
            if old_str == "-9999":
                new_str = "-999999"
            else:
                if old_mem[i][0] == "-":
                    new_str += "-"
                else:
                    new_str += "+"
                new_str = new_str + "0" + old_str[1:3] + "0" + old_str[3:]
            self.mem[i] = new_str
            i+=1
        return self.mem
