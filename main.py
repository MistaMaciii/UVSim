"""
Wes James, CS 2450, 2023
Sets up virtual machine and runs imported code
"""
def read(add):
    """Read a word from the keyboard into a specific location in memory"""
    user_in = input("Input a word(+1234): ")
    user_in = user_in[0:5]
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
    
acc = 0     #initializes the accumulator
mem = []    #initializes the memory
ip = 0      #initializes the intruction pointer
file = input("What is your file name?: ")   #gets file name from user
f = open(file, "r", encoding="utf8")        #opens file
for x in f:
    word = x[0:6]
    if word in ("-99999", "\n"):
        f.close()
        break           #if word is -99999, or an empty line, stop reading and close the file
    word = word[0:5]    #else set the word to the frist 5 characters
    mem.append(word)    #append the word to memory
    #print(mem[-1])
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
    elif op_code == "20":     #Load a word from a specific location in memory into the accumulator.
        load(mem_add)
    elif op_code == "21":   #Store a word from the accumulator into a specific location in memory.
        store(mem_add)
    ip += 1     #go to the next word
