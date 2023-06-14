from Operations import Arithmetic_Operations
from Operations import Control_Operations
from Operations import IO_Operations
from Operations import LoadStore_Operations

class UVSim:
  def __init__(self):
    self.acc = 0     #initializes the accumulator
    self.mem = ["-0000"] * 100   #initializes the memory
    self.ip = 0      #initializes the intruction pointer
    self.halt_status = False
    self.line = 1

  def loadFile(self):
    file = input("What is your file name?: ")   #gets file name from user
    f = open(file, "r", encoding="utf8")        #opens file
    for x in f:
      if x in ("-99999"):
        f.close()
        break           #if word is -99999, stop reading and close the file
      word = x[0:-1]      #set word to one smaller than word length to remove newline
      if len(word) != 5:   #if word is longer than 5 chars throw an error
        raise ValueError("incorrect input format on line " + str(self.line))
      if (word[0] != '+') and (word[0] != '-'):   #if word doesn't start with + or - throw an error
        raise ValueError("incorrect input format on line " + str(self.line))
      self.mem[self.line - 1] = word     #add the word to memory at line minus 1
      self.line += 1
    f.close()

  def runSystem(self):
    while self.ip < len(self.mem):
      curr_word = str(self.mem[self.ip]) #set curret word = to the word the IP is pointing to
      if curr_word[0] == "-": #if the first char is '-' then go to the next word
        self.ip += 1
        continue
      op_group = str(curr_word[1:2]) #split op code into type
      op_call = str(curr_word[2:3]) #split op code into operation of type
      mem_loc = int(curr_word[3:]) # get mem location from word
      if op_group == "1":
        IO_Operations.IO_Operations.pickOperation(op_call, mem_loc, self)
      elif op_group == "2":
        LoadStore_Operations.LoadStore_Operations.pickOperation(op_call, mem_loc, self)
      elif op_group == "3":
        Arithmetic_Operations.Arithmetic_Operations.pickOperation(op_call, mem_loc, self)
      elif op_group == "4":
        Control_Operations.Control_Operations.pickOperation(op_call, mem_loc, self)
        if self.halt_status == True: break
      self.ip += 1     #go to the next word
