import re

def apply_rules(l):   
    if l == 0:
        return [6,8]
    
    return [l - 1]

def run_simulation(root_node, total_days):
    count_map = {root_node: 1}  
    current_day = 0

    while (current_day < total_days):
        next_count_map = {}
        for lanternfish, count in count_map.items():
            for new_lanternfish in apply_rules(lanternfish):
                next_count_map[new_lanternfish] = next_count_map.get(new_lanternfish, 0) + count 
        count_map = next_count_map
        current_day += 1

    print("Count Map: ", count_map)
    return sum(count_map.values())
    
def simulate(total_days, lanternfish):
    total_lanternfish = 0
    for l in lanternfish:
        total_lanternfish += run_simulation(l, total_days)
    
    return total_lanternfish

if __name__ == "__main__":
    filename = "Day15_test.txt"

    line = ''
    with open(filename, 'r') as f:
        line = f.readline()

    matches = re.findall(r'\d+', line.strip())

    lanternfish = [int(m) for m in matches]
    print("Initial State: ", lanternfish)

    days = 256

    total = simulate(days, lanternfish)

    print("Total lanternfish: ", total)
