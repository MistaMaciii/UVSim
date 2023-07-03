class Control_Operations:
  def pickOperation(operation, memLoc, Memory, UVSim):
    if operation == "0":
      Control_Operations.branch(memLoc, Memory)
    elif operation == "1":
      Control_Operations.branch_neg(memLoc, Memory)
    elif operation == "2":
      Control_Operations.branch_zero(memLoc, Memory)
    elif operation == "3":
      Control_Operations.halt(Memory, UVSim)
  
  def branch(add, Memory):
    """Branch to a specific location in memory"""
    if add > (len(Memory.mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    Memory.ip = int(add) - 1   #set the instruction pointer to the memory address that was passed through
    
  def branch_neg(add, Memory):
    """Branch to a specific location in memory if accumulator is negative"""
    if add > (len(Memory.mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    if Memory.acc < 0:
        Memory.ip = int(add) - 1    #set the instruction pointer to the memory address that was passed through
  
  def branch_zero(add, Memory):
    """Branch to a specific location in memory if accumulator is zero"""
    if add > (len(Memory.mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    if Memory.acc == 0:
        Memory.ip = int(add) - 1    #set the instruction pointer to the memory address that was passed through
  
  def halt(Memory, UVSim):
    """Pause the program"""
    Memory.halt_status = True
    UVSim.output += ("halting...\n")
    print("halting...")

