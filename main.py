"""
Wes James, CS 2450, 2023
Sets up virtual machine and runs imported code
"""
def read(add):
    """Read a word from the keyboard into a specific location in memory"""
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
    out = mem[add]
    print(out)

def load(mem_load_location):
    #Load a word from a specific location in memory into the accumulator.
    global acc
    acc = mem[mem_load_location]
    
def store(mem_store_location):
    #Store a word from the accumulator into a specific location in memory.
    mem[mem_store_location] = acc    

def branch(add):
    """Branch to a specific location in memory"""
    global ip
    ip = int(add)    #set the instruction pointer to the memory address that was passed through

acc = 0     #initializes the accumulator
mem = []    #initializes the memory
ip = 0      #initializes the intruction pointer
line = 1
def main():
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
        #print(mem[-1])
        line += 1
    f.close()
    while ip < len(mem):            #runs the code
        curr_word = mem[ip]         #set curret word = to the word the IP is pointing to
        if curr_word[0] == "-":     #if the first char is '-' then go to the next word
            ip += 1
            continue
        op_code = curr_word[1:3]    #split op code and memory address into 2 variables
        mem_add = int(curr_word[3:])
        #print(op_code)
        #print(mem_add)
        if op_code == "10":     #read from keyboard into memory
            read(mem_add)
        elif op_code == "11":   #write from memory to screen
            write(mem_add)
        elif op_code == "20":   #Load a word from a specific location in memory into the accumulator.
            load(mem_add)
        elif op_code == "21":   #Store a word from the accumulator into a specific location in memory.
            store(mem_add)
        elif op_code == "40":   #branch to location in memory
            branch(mem_add)
            continue
        elif op_code == "41":   #branch if accumulator is negative
            if curr_word[0] == "-":
                branch(mem_add)
                continue
        elif op_code == "42":   #branch if the accumulator is zero
            if int(curr_word[1:]) == 0:
                branch(mem_add)
                continue
        elif op_code == "43":   #pause the program
            break

        ip += 1     #go to the next word
main()