class IO_Operations:
  def pickOperation(operation, memLoc, Memory, UVSim):
    if operation == "0":
      IO_Operations.read(memLoc, Memory, UVSim)
    if operation == "1":
      IO_Operations.write(memLoc, Memory)
     
  def read(add, Memory, UVSim):
    """Read a word from the keyboard into a specific location in memory"""
    UVSim.output += ("Input a word(+1234): \n")
    UVSim.window.updateConsoleDisplay()
    UVSim.window.wait_for_button()

    if add > len(Memory.mem) -1:
        raise IndexError("Can't access memory at index " + str(add))
    user_in =  UVSim.window.user_input
    print(user_in)
    if (len(user_in) == 4 and user_in.isdigit()):   #if word is not == 5 chars redo
        Memory.mem[add] = str(user_in)
    elif (len(user_in) == 5 and (user_in[0] == '-' or (user_in[0] == '+')) and user_in[1:].isdigit):
        Memory.mem[add] = str(user_in)
    else:    #error here
        print("incorrect length")
        return 1
        # IO_Operations.read(add, Memory)   #TypeError: IO_Operations.read() missing 1 required positional argument: 'Memory' when incorrect length
        # return
 
  def write(add, Memory):
    """Write a word from a specific location in memory to screen"""
    if add > len(Memory.mem) -1:
        raise IndexError("Can't access memory at index " + str(add))
    out = Memory.mem[add]
    # UVSim.output += (str(out) + "\n")
    print(out)
   
    return out


