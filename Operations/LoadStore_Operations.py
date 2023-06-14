class LoadStore_Operations:
  def pickOperation(operation, memLoc, UVSim):
    if operation == "0":
      LoadStore_Operations.load(memLoc, UVSim)
    elif operation == "1":
      LoadStore_Operations.store(memLoc, UVSim)
    
  def load(mem_load_location, UVSim):
    #Load a word from a specific location in memory into the accumulator.
    #global acc
    UVSim.acc = UVSim.mem[mem_load_location]
  
  def store(mem_store_location, UVSim):
    #Store a word from the accumulator into a specific location in memory.
    UVSim.mem[mem_store_location] = UVSim.acc
    

