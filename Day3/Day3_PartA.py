import re

if __name__ == "__main__":
    filename = "input_3.txt"

    pattern = "mul\((\d{1,3})\,(\d{1,3})\)"

    total = 0
    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            matches = re.findall(pattern, line)

            for d1, d2 in matches:
                total += int(d1) * int(d2)
    
    print(total)