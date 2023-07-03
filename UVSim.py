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
        IO_Operations.IO_Operations.pickOperation(op_call, mem_loc, self.memory, user_input, self)
      elif op_group == "2":
        LoadStore_Operations.LoadStore_Operations.pickOperation(op_call, mem_loc, self.memory)
      elif op_group == "3":
        Arithmetic_Operations.Arithmetic_Operations.pickOperation(op_call, mem_loc, self.memory)
      elif op_group == "4":
        Control_Operations.Control_Operations.pickOperation(op_call, mem_loc, self.memory, self)
        if self.halt_status == True: break
      self.ip += 1     #go to the next word
    self.is_active = False    #set is_active to false after system has been run
    self.halt_status = False  #reset halt_status
