import sys

def subtract(levels):
    return [levels[i] - levels[i-1] for i in range(1, len(levels))]

if __name__ == "__main__":
    filename = "input_2.txt"

    with open(filename, 'r') as f:
        lines = f.readlines()
    
    safe_levels = 0
    for line in lines:
        levels = [int(c) for c in line.strip().split()]

        adjacent_levels = subtract(levels)
        
        sign = adjacent_levels[0] > 0
        
        same_sign = all((num > 0) == sign for num in adjacent_levels)
        not_zero = all(num != 0 for num in adjacent_levels)
        max_three = all(abs(num) <= 3 for num in adjacent_levels)

        safe_levels += 1 if same_sign and not_zero and max_three else 0
    
    print(safe_levels)
