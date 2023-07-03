class LoadStore_Operations:
  def pickOperation(operation, memLoc, Memory):
    if operation == "0":
      LoadStore_Operations.load(memLoc, Memory)
    elif operation == "1":
      LoadStore_Operations.store(memLoc, Memory)
    
  def load(mem_load_location, Memory):
    #Load a word from a specific location in memory into the accumulator.
    #global acc
    Memory.acc = Memory.mem[mem_load_location]
  
  def store(mem_store_location, Memory):
    #Store a word from the accumulator into a specific location in memory.
    Memory.mem[mem_store_location] = Memory.acc
    

