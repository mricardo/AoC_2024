# each towel has one more more stripes: white (w), blue(b), red(r), green(g)
# each design is a sequence of towels
# arrange towels into the designs

def check_valid_design(towels, design, memo):
    if design in memo:
        return memo[design]

    if not design:
        return 1
    
    total_valid_designs = 0

    for towel in towels:
        if design.startswith(towel):
            total_valid_designs += check_valid_design(towels, design[len(towel):], memo)

    memo[design] = total_valid_designs

    return total_valid_designs

with open("Day19/Day19_Input.txt", "r") as file:
    lines = [line.strip() for line in file]

towels = set(lines[0].split(", "))
designs = lines[2:]

total_valid_designs = 0
memo = {}
for design in designs:
    total_valid_designs += check_valid_design(towels, design, memo)

print("Total valid designs:", total_valid_designs)
