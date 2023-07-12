from Operations import Arithmetic_Operations
from Operations import Control_Operations
from Operations import IO_Operations
from Operations import LoadStore_Operations
import Memory
import gui
import sys
from PyQt6.QtWidgets import QApplication
import Loader

class UVSim:
  def __init__(self):
    self.output = ""
    self.is_active = True          #initialize the is_active indicator
    self.ip = 0                    #initializes the intruction pointer
    self.halt_status = False
    self.line = 1
    self.op_group = ""
    self.op_call = ""
    self.mem_loc = 0
    self.memory = Memory.Memory()
    self.app = QApplication(sys.argv)  # Open the QApp through MainWindow class with command line options
    self.window = gui.MainWindow(self)
    self.loader = Loader.Loader()

  def runSystem(self):
    self.halt_status = False
    while not self.halt_status:
      curr_word = str(self.memory.mem[self.ip]) #set curret word = to the word the IP is pointing to
      if curr_word[0] == "-": #if the first char is '-' then go to the next word
        self.ip += 1
        continue
      self.op_group = str(curr_word[1:2]) #split op code into type
      self.op_call = str(curr_word[2:3]) #split op code into operation of type
      self.mem_loc = int(curr_word[3:]) # get mem location from word
      if self.op_group == "1":
        IO_Operations.IO_Operations.pickOperation(self.op_call, self.mem_loc, self.memory, self)
      elif self.op_group == "2":
        LoadStore_Operations.LoadStore_Operations.pickOperation(self.op_call, self.mem_loc, self.memory)
      elif self.op_group == "3":
        Arithmetic_Operations.Arithmetic_Operations.pickOperation(self.op_call, self.mem_loc, self.memory)
      elif self.op_group == "4":
        Control_Operations.Control_Operations.pickOperation(self.op_call, self.mem_loc, self.memory, self)
      self.ip += 1     #go to the next word
      self.window.update_displays()

  def guiSetup(self):
    with open("style.css", "r") as file:    #opens file for css styles
        self.app.setStyleSheet(file.read())
    self.window.show()  # show main window
    sys.exit(self.app.exec())  # start event loop

  def runLoader(self, file_path):
    self.loader = Loader.Loader()  # initialize Loader every file load
    self.loader.load_file(file_path)
    self.memory.mem = self.loader.memory.mem  # prints memory after loading file

  def resetForNewFile(self):
    self.output = ""
    self.is_active = True          #initialize the is_active indicator
    self.ip = 0                    #initializes the intruction pointer
    self.halt_status = False
    self.line = 1
    self.op_group = ""
    self.op_call = ""
    self.mem_loc = 0
    self.memory = Memory.Memory()
    self.loader = Loader.Loader()
    self.window.update_displays()

  def resetForNewRun(self):
    self.output = ""
    self.is_active = True          #initialize the is_active indicator
    self.ip = 0                    #initializes the intruction pointer
    self.halt_status = False
    self.window.update_displays()
