"""
UVSim - Simple Virtual Machine 
Elena Mitchell, Justin Peeples, Mac Snow, Wes James
Utah Valley University
"""
def read(add):
    """Read a word from the keyboard into a specific location in memory"""
    if add > len(mem) -1:
        raise IndexError("Can't access memory at index " + str(add))
    user_in = input("Input a word(+1234): ")
    if len(user_in) != 5:   #if word is not == 5 chars redo
        print("incorrect length")
        read(add)
        return
    if (user_in[0] != '+') and (user_in[0] != '-'):   #if word doesn't start with + or - redo
        print("needs a + or - at beginning")
        read(add)
        return
    mem[add] = user_in
def write(add):
    """Write a word from a specific location in memory to screen"""
    if add > len(mem) -1:
        raise IndexError("Can't access memory at index " + str(add))
    out = mem[add]
    print(out)
    return out
def load(mem_load_location):
    #Load a word from a specific location in memory into the accumulator.
    global acc
    acc = mem[mem_load_location]
    
def store(mem_store_location):
    #Store a word from the accumulator into a specific location in memory.
    mem[mem_store_location] = acc  
    
def addit(add):
    global acc
    word_inmem = mem[add]   #the word in memory at the specified location
    addit_res = (int(word_inmem) + int(acc)) #adds the int of the word in mem and the word in the accumulator where the result is then stored
    while addit_res <-9999:
        addit_res = addit_res + 10000
    while addit_res >9999:
        addit_res = addit_res - 10000
    acc = addit_res #stores result in accumulator
    
def sub(add):
    global acc
    word_inmem = mem[add]
    sub_res = ( int(acc) - int(word_inmem)) #subtracts the int of the word in mem from the word in the accumulator where the result is then stTestored
    while sub_res <-9999:
        sub_res = sub_res + 10000
    while sub_res >9999:
        sub_res = sub_res - 10000
    acc = sub_res

def div(add):
    global acc
    word_inmem = mem[add]
    if word_inmem == "0000":
        raise ZeroDivisionError("Value in accumulator cannot be divided by zero value at index " + str(add))
    div_res = ( int(acc) // int(word_inmem)) #floor divides the word in the accumulator by the int of the word in mem where the result is then stored
    while div_res <-9999:
        div_res = div_res + 10000
    while div_res >9999:
        div_res = div_res - 10000
    acc = div_res

def mult(add):
    global acc
    word_inmem = mem[add]
    mult_res = (int(word_inmem) * int(acc)) #multiplies the int of the word in mem and the word in the accumulator where the result is then stored
    while mult_res <-9999:
        mult_res = mult_res + 10000
    while mult_res >9999:
        mult_res = mult_res - 10000
    acc = mult_res

def branch(add):
    """Branch to a specific location in memory"""
    if add > (len(mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    global ip
    ip = int(add) - 1   #set the instruction pointer to the memory address that was passed through

def branch_neg(add):
    """Branch to a specific location in memory if accumulator is negative"""
    if add > (len(mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    global ip
    global acc
    if acc < 0:
        ip = int(add) - 1    #set the instruction pointer to the memory address that was passed through

def branch_zero(add):
    """Branch to a specific location in memory if accumulator is zero"""
    if add > (len(mem)-1):
        raise IndexError("Can't access memory at index " + str(add))
    global ip
    global acc
    if acc == 0:
        ip = int(add) - 1    #set the instruction pointer to the memory address that was passed through
    
def halt():
    global halt_status
    halt_status = True
    print("halting...")

acc = 0     #initializes the accumulator
mem = []    #initializes the memory
ip = 0      #initializes the intruction pointer
halt_status = False

line = 1
if __name__ == '__main__':
    file = input("What is your file name?: ")   #gets file name from user
    f = open(file, "r", encoding="utf8")        #opens file
    for x in f:
        if x in ("-99999"):
            f.close()
            break           #if word is -99999, stop reading and close the file

        word = x[0:-1]      #set word to one smaller than word length to remove newline
        if len(word) != 5:   #if word is longer than 5 chars throw an error
            raise ValueError("incorrect input format on line " + str(line))

        if (word[0] != '+') and (word[0] != '-'):   #if word doesn't start with + or - throw an error
            raise ValueError("incorrect input format on line " + str(line))

        mem.append(word)    #append the word to memory
        line += 1
    f.close()
    while ip < len(mem):            #runs the code
        curr_word = mem[ip]         #set curret word = to the word the IP is pointing to
        if curr_word[0] == "-":     #if the first char is '-' then go to the next word
            ip += 1
            continue
        op_code = curr_word[1:3]    #split op code and memory address into 2 variables
        mem_add = int(curr_word[3:])
        if op_code == "10":     #read from keyboard into memory
            read(mem_add)
        elif op_code == "11":   #write from memory to screen
            write(mem_add)
        elif op_code == "20":   #Load a word from a specific location in memory into the accumulator.
            load(mem_add)
        elif op_code == "21":   #Store a word from the accumulator into a specific location in memory.
            store(mem_add)
        elif op_code == "30":     #Add a word from a specific location in memory to the word in the accumulator
            addit(mem_add)
        elif op_code == "31":   #Subtract a word from a specific location in memory from the word in the accumulator
            sub(mem_add)
        elif op_code == "32":     #Divide the word in the accumulator by a word from a specific location in memory
            div(mem_add)
        elif op_code == "33":   #multiply a word from a specific location in memory to the word in the accumulator 
            mult(mem_add)
        elif op_code == "40":   #branch to location in memory
            branch(mem_add)
        elif op_code == "41":   #branch if accumulator is negative
            branch_neg(mem_add)
        elif op_code == "42":   #branch if the accumulator is zero
            branch_zero(mem_add)
        elif op_code == "43":   #pause the program
            halt()
            if halt_status == True: break
        ip += 1     #go to the next word
