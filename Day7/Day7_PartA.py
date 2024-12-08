import re
import itertools

def run_combinations(test_value, numbers):
    total_operators = len(numbers) - 1

    operators = [['+', '*'].copy() for _ in range(total_operators)]

    permuted_operators = itertools.product(*operators)

    idx = 1
    value = numbers[0]
    
    for p in permuted_operators:
        for o in p:
            if o == '+':
                value += (numbers[idx])
            if o == '*':
                value *= (numbers[idx])

            if idx + 1 > len(numbers):
                break

            idx += 1        

        if value == test_value:
            return value
        
        idx = 1
        value = numbers[0]
    
    return -1

if __name__ == "__main__":
    filename = "Day7_input.txt"

    with open(filename, 'r') as f:
        lines = f.readlines()

        total_calibration = 0
        for line in lines:
            line = line.strip()
            idx = line.index(":")
            
            test_value = int(line[:idx])
            numbers = line[idx+1:].split()
            numbers = [int(n) for n in numbers]

            result = run_combinations(test_value, numbers)
            if result != -1:
                total_calibration += result

        print(total_calibration)