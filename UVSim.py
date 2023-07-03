from Operations import Arithmetic_Operations
from Operations import Control_Operations
from Operations import IO_Operations
from Operations import LoadStore_Operations
import Memory

class UVSim:
  def __init__(self):
    self.output = ""
    self.is_active = True          #initialize the is_active indicator
    self.ip = 0                    #initializes the intruction pointer
    self.halt_status = False
    self.line = 1
    self.memory = Memory.Memory()

  def loadFile(self, path):
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
          self.memory.mem[self.line - 1] = word     #add the word to memory at line minus 1
          self.line += 1
    except FileNotFoundError:
      self.output += "No file selected. Please select a file\n"
      

  def runSystem(self, user_input):
    self.ip = 0             #if the system resets, re initialize to 0
    self.halt_status = False
    while self.ip < len(self.memory.mem):
      curr_word = str(self.memory.mem[self.ip]) #set curret word = to the word the IP is pointing to
      if curr_word[0] == "-": #if the first char is '-' then go to the next word
        self.ip += 1
        continue
      op_group = str(curr_word[1:2]) #split op code into type
      op_call = str(curr_word[2:3]) #split op code into operation of type
      mem_loc = int(curr_word[3:]) # get mem location from word
      if op_group == "1":
        IO_Operations.IO_Operations.pickOperation(op_call, mem_loc, self.memory, user_input)
      elif op_group == "2":
        LoadStore_Operations.LoadStore_Operations.pickOperation(op_call, mem_loc, self.memory)
      elif op_group == "3":
        Arithmetic_Operations.Arithmetic_Operations.pickOperation(op_call, mem_loc, self.memory)
      elif op_group == "4":
        Control_Operations.Control_Operations.pickOperation(op_call, mem_loc, self.memory)
        if self.halt_status == True: break
      self.ip += 1     #go to the next word
    self.is_active = False    #set is_active to false after system has been run
    self.halt_status = False  #reset halt_status
