class Control_Operations:
  def pickOperation(operation, memLoc, UVSim):
    if operation == "0":
      Control_Operations.branch(memLoc, UVSim)
    elif operation == "1":
      Control_Operations.branch_neg(memLoc, UVSim)
    elif operation == "2":
      Control_Operations.branch_zero(memLoc, UVSim)
    elif operation == "3":
      Control_Operations.halt(UVSim)
  
  def branch(add, UVSim):
    """Branch to a specific location in memory"""
    if add > (len(UVSim.mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    UVSim.ip = int(add) - 1   #set the instruction pointer to the memory address that was passed through
    
  def branch_neg(add, UVSim):
    """Branch to a specific location in memory if accumulator is negative"""
    if add > (len(UVSim.mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    if UVSim.acc < 0:
        UVSim.ip = int(add) - 1    #set the instruction pointer to the memory address that was passed through
  
  def branch_zero(add, UVSim):
    """Branch to a specific location in memory if accumulator is zero"""
    if add > (len(UVSim.mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    if UVSim.acc == 0:
        UVSim.ip = int(add) - 1    #set the instruction pointer to the memory address that was passed through
  
  def halt(UVSim):
    """Pause the program"""
    UVSim.halt_status = True
    UVSim.output += ("halting...\n")
    print("halting...")

