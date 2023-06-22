class IO_Operations:
  def pickOperation(operation, memLoc, UVSim):
    if operation == "0":
      IO_Operations.read(memLoc, UVSim)
    elif operation == "1":
      IO_Operations.write(memLoc, UVSim)
      
  def read(add, UVSim):
    """Read a word from the keyboard into a specific location in memory"""
    if add > len(UVSim.mem) -1:
        raise IndexError("Can't access memory at index " + str(add))
    user_in = input("Input a word(+1234): ")
    if (len(user_in) == 4 and user_in.isdigit()):   #if word is not == 5 chars redo
        UVSim.mem[add] = user_in
    elif (len(user_in) == 5 and (user_in[0] == '-' or (user_in[0] == '+')) and user_in[1:].isdigit):
        UVSim.mem[add] = user_in
    else:    
        print("incorrect length")
        IO_Operations.read(add)
        return
  
  def write(add, UVSim):
    """Write a word from a specific location in memory to screen"""
    if add > len(UVSim.mem) -1:
        raise IndexError("Can't access memory at index " + str(add))
    out = UVSim.mem[add]
    print(out)
    return out

