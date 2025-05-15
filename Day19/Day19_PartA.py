# each towel has one more more stripes: white (w), blue(b), red(r), green(g)
# each design is a sequence of towels
# arrange towels into the designs

def check_valid_design(towels, design):
    if not design:
        return True
    
    for towel in towels:
        if design.startswith(towel) and check_valid_design(towels, design[len(towel):]):
            return True
    
    return False

with open("Day19/Day19_Input.txt", "r") as file:
    lines = [line.strip() for line in file]

towels = set(lines[0].split(", "))
designs = lines[2:]

total_valid_designs = sum(check_valid_design(towels, design) for design in designs)

print("Total valid designs:", total_valid_designs)