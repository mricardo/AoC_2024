import re

# opcodes
ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

# registry
A = 0
B = 1
C = 2

def get_combo(operand, registers):
    if operand <= 3:
        return operand

    combo = {4: registers[A], 5: registers[B], 6: registers[C]}

    return combo[operand]

def run_program(ip, output, program, registers):
    opcode = program[ip]
    operand = program[ip + 1]    

    set_jump = False

    if opcode == ADV:        
        registers[A] >>= get_combo(operand, registers)
        
    if opcode == BXL:
        registers[B] ^= operand
            
    if opcode == BST:
        registers[B] = get_combo(operand, registers) % 8
        
    if opcode == JNZ and registers[A] != 0:
        ip = operand            
        set_jump = True

    if opcode == BXC:
        registers[B] ^= registers[C]
        
    if opcode == OUT:
        output.append(get_combo(operand, registers) % 8)
            
    if opcode == BDV:        
        registers[B] = registers[A] >> get_combo(operand, registers)
            
    if opcode == CDV:        
        registers[C] = registers[A]  >> get_combo(operand, registers)

    return ip + 2 if not set_jump else ip
    
def lowest_value_registerA(program, registers):    
    max_ip = len(program)        
    output = []
    register_A = 0

    # solution inspired from Reddit
    for i in reversed(range(len(program))):
        register_A <<= 3 # shift 3 bits to the left, since the VM only looks at the last 3 bits of A each time, that we expirement

        # we incrementally add more pieces of the program to iterate to possible values of register A
        while output != program[i:]:
            output = []
            ip = 0

            registers = [register_A, registers[B], registers[C]]
            
            while ip < max_ip:
                ip = run_program(ip, output, program, registers)         

            if output != program[i:]:
                register_A += 1

    return register_A

if __name__ == "__main__":
    filename = "Day17_test.txt"

    registers = [0, 0, 0]
    with open(filename, 'r') as f:
        registers[A] = int(re.search(r'(\d+)', f.readline()).group(1))
        registers[B] = int(re.search(r'(\d+)', f.readline()).group(1))
        registers[C] = int(re.search(r'(\d+)', f.readline()).group(1))

        print("Register A: ", registers[A], " Register B: ", registers[B], " Register C: ", registers[C])

        f.readline() # skip blank line
        
        program = re.search(r'((\d+,{0,1})+)', f.readline()).group(1)

        program = [int (p) for p in program.split(",")]

        print("Program: ", program)

        reg_A = lowest_value_registerA(program, registers)

        print("Minimum Value - Register A: ", reg_A)