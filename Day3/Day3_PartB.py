import re

if __name__ == "__main__":
    filename = "input_3.txt"

    pattern = "mul\((\d{1,3})\,(\d{1,3})\)"

    total = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        joined_line = ''.join(line.strip() for line in lines)

        for match in re.finditer(pattern,joined_line):
            end_index = match.end()
                
            idx_do = joined_line.rfind("do()", 0, end_index)
            idx_dont = joined_line.rfind("don't()", 0, end_index)

            if idx_do >= idx_dont:
                d1, d2 = match.groups()
                total += int(d1) * int(d2)

    print(total)


