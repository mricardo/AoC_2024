import re

def calculate_combo(operand, registerA, registerB, registerC):
    if operand <= 3:
        return operand

    combo = {4: registerA, 5: registerB, 6: registerC}
    return combo[operand]

def run_program(program, registerA, registerB, registerC):
    total_instructions = len(program)
    instruction_pointer = 0

    output = []

    while (instruction_pointer < total_instructions):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        # adv
        if opcode == 0:
            numerator = registerA
            denominator = 2 ** calculate_combo(operand, registerA, registerB, registerC)
            registerA = int(numerator / denominator)
        
        # bxl
        if opcode == 1:
            registerB = registerB ^ operand
        
        # bst
        if opcode == 2:
            registerB = calculate_combo(operand, registerA, registerB, registerC) % 8
        
        # jnz
        if opcode == 3 and registerA != 0:
            instruction_pointer = operand
            continue
    
        # bxc
        if opcode == 4:
            registerB = registerB ^ registerC
        
        # out
        if opcode == 5:
            output.append(calculate_combo(operand, registerA, registerB, registerC) % 8)
        
        # bdv
        if opcode == 6:
            numerator = registerA
            denominator = 2 ** calculate_combo(operand, registerA, registerB, registerC)
            registerB = int(numerator / denominator)
        
        # cdv
        if opcode == 7:
            numerator = registerA
            denominator = 2 ** calculate_combo(operand, registerA, registerB, registerC)
            registerC = int(numerator / denominator)
        
        instruction_pointer += 2

    print ("Register A: ", registerA, " RegisterB: ", registerB, " Register C: ", registerC)
    print(",".join(map(str, output)))
    
if __name__ == "__main__":
    filename = "Day17_test.txt"

    with open(filename, 'r') as f:
        registerA = int(re.search(r'(\d+)', f.readline()).group(1))
        registerB = int(re.search(r'(\d+)', f.readline()).group(1))
        registerC = int(re.search(r'(\d+)', f.readline()).group(1))

        print("Register A: ", registerA, " Register B: ", registerB, " Register C: ", registerC)

        f.readline() # blank line
        
        program = re.search(r'((\d+,{0,1})+)', f.readline()).group(1)

        program = [int (p) for p in program.split(",")]

        print("Program: ", program)

        run_program(program, registerA, registerB, registerC)
