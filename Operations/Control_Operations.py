class Control_Operations:
  def pickOperation(operation, memLoc, Memory, UVSim):
    if operation == "0":
      Control_Operations.branch(memLoc, Memory, UVSim)
    elif operation == "1":
      Control_Operations.branch_neg(memLoc, Memory, UVSim)
    elif operation == "2":
      Control_Operations.branch_zero(memLoc, Memory, UVSim)
    elif operation == "3":
      Control_Operations.halt(Memory, UVSim)
  
  def branch(add, Memory, UVSim):
    """Branch to a specific location in memory"""
    if add > (len(Memory.mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    UVSim.ip = int(add) - 1   #set the instruction pointer to the memory address that was passed through
    
  def branch_neg(add, Memory, UVSim):
    """Branch to a specific location in memory if accumulator is negative"""
    if add > (len(Memory.mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    if int(Memory.acc) < 0:
        UVSim.ip = int(add) - 1    #set the instruction pointer to the memory address that was passed through
  
  def branch_zero(add, Memory, UVSim):
    """Branch to a specific location in memory if accumulator is zero"""
    if add > (len(Memory.mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    if int(Memory.acc) == 0:
        UVSim.ip = int(add) - 1    #set the instruction pointer to the memory address that was passed through
  
  def halt(Memory, UVSim):
    """Pause the program"""
    UVSim.halt_status = True
    UVSim.output += ("halting...\n")

