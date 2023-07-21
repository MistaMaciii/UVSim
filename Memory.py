class Memory:
  def __init__(self):
    self.acc = 0                   #initializes the accumulator
    self.mem_limit = 100
    self.mem = ["+0000"] * self.mem_limit     #initializes the memory