class Memory:
  def __init__(self):
    self.mem_limit = 250
    self.acc = 0                   #initializes the accumulator
    self.mem = ["+0000"] * self.mem_limit     #initializes the memory