import sys

def subtract(levels):
    return [levels[i] - levels[i-1] for i in range(1, len(levels))]

def test_level(adjacent_levels):
    sign = adjacent_levels[0] > 0
    
    same_sign = all((num > 0) == sign for num in adjacent_levels)
    not_zero = all(num != 0 for num in adjacent_levels)
    max_three = all(abs(num) <= 3 for num in adjacent_levels)

    return same_sign and not_zero and max_three

if __name__ == "__main__":
    filename = "input_2.txt"

    with open(filename, 'r') as f:
        lines = f.readlines()
    
    safe_levels = 0
    for line in lines:
        levels = [int(c) for c in line.strip().split()]

        test_levels = levels[:]

        for i in range(len(levels)+1):
            adjacent_levels = subtract(test_levels)

            if test_level(adjacent_levels):
                safe_levels += 1
                break

            test_levels = levels[:i] + levels[i+1:]
    
    print(safe_levels)
