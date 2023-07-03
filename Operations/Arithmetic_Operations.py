class Arithmetic_Operations:
  def pickOperation(operation, memLoc, Memory):
    if operation == "0":
      Arithmetic_Operations.addit(memLoc, Memory)
    elif operation == "1":
      Arithmetic_Operations.sub(memLoc, Memory)
    elif operation == "2":
      Arithmetic_Operations.div(memLoc, Memory)
    elif operation == "3":
      Arithmetic_Operations.mult(memLoc, Memory)
  
  def addit(add, Memory):
    """Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)"""

    word_inmem = Memory.mem[add]   #the word in memory at the specified location
    addit_res = (int(word_inmem) + int(Memory.acc)) #adds the int of the word in mem and the word in the accumulator where the result is then stored
    while addit_res <-9999:
        addit_res = addit_res + 10000
    while addit_res >9999:
        addit_res = addit_res - 10000
    Memory.acc = addit_res #stores result in accumulator
  
  def sub(add, Memory):
    """Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)"""
    word_inmem = Memory.mem[add]
    sub_res = ( int(Memory.acc) - int(word_inmem)) #subtracts the int of the word in mem from the word in the accumulator where the result is then stTestored
    while sub_res <-9999:
        sub_res = sub_res + 10000
    while sub_res >9999:
        sub_res = sub_res - 10000
    Memory.acc = sub_res
  
  def div(add, Memory):
    """Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)."""
    word_inmem = Memory.mem[add]
    if word_inmem == "0000":
        raise ZeroDivisionError("Value in accumulator cannot be divided by zero value at index " + str(add))
    div_res = ( int(Memory.acc) // int(word_inmem)) #floor divides the word in the accumulator by the int of the word in mem where the result is then stored
    while div_res <-9999:
        div_res = div_res + 10000
    while div_res >9999:
        div_res = div_res - 10000
    Memory.acc = div_res
  
  def mult(add, Memory):
    """Multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)."""
    word_inmem = Memory.mem[add]
    mult_res = (int(word_inmem) * int(Memory.acc)) #multiplies the int of the word in mem and the word in the accumulator where the result is then stored
    while mult_res <-9999:
        mult_res = mult_res + 10000
    while mult_res >9999:
        mult_res = mult_res - 10000
    Memory.acc = mult_res
