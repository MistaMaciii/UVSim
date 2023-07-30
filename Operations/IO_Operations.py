class IO_Operations:
  def pickOperation(operation, memLoc, Memory, UVSim):
    if operation == "0":
      IO_Operations.read(memLoc, Memory, UVSim)
    if operation == "1":
      IO_Operations.write(memLoc, Memory, UVSim)
     
  def read(add, Memory, UVSim):
    """Read a word from the keyboard into a specific location in memory"""
    UVSim.output += ("Input a word(+1234): \n")
    UVSim.window.updateConsoleDisplay()
    UVSim.window.wait_for_button()
    user_in =  UVSim.window.user_input
    UVSim.window.input_line.clear()
    UVSim.window.input_line.clearFocus()
    if add > len(Memory.mem) -1:
        raise IndexError("Can't access memory at index " + str(add))
    if (len(user_in) == 6 and user_in.isdigit()):   #if word is not == 5 chars redo
        Memory.mem[add] = str(user_in)
    elif (len(user_in) == 7 and (user_in[0] == '-' or (user_in[0] == '+')) and user_in[1:].isdigit):
        Memory.mem[add] = str(user_in)
    else:    #error here
        UVSim.output += ("Invalid length try again.\n")
        UVSim.window.updateConsoleDisplay()
        IO_Operations.read(add, Memory, UVSim)
 
  def write(add, Memory, UVSim):
    """Write a word from a specific location in memory to screen"""
    if add > len(Memory.mem) -1:
        raise IndexError("Can't access memory at index " + str(add))
    UVSim.output += str(Memory.mem[add]) + "\n"
    # UVSim.output += (str(out) + "\n")


