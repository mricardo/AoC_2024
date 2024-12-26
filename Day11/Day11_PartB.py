from itertools import count
from logging import root
from os import remove
import sys
import copy

def apply_rules(stone):   
    if stone == '0':
        return ['1']      
    elif len(stone) % 2 == 0:
        half = int(len(stone) / 2)                   
        return [str(int(stone[0:half])), str(int(stone[half:]))]
    
    return [str(int(stone) * 2024)]
    
    
def run_blinkings(root_node, blinkings):
    count_map = {root_node: 1}  
    current_blink = 0

    while (current_blink < blinkings):
        next_count_map = {}
        for stone, count in count_map.items():
            for new_stone in apply_rules(stone):
                next_count_map[new_stone] = next_count_map.get(new_stone, 0) + count 
        count_map = next_count_map
        current_blink += 1

    return sum(count_map.values())

if __name__ == "__main__":
    filename = "Day11_test.txt"

    blinkings = None
    if len(sys.argv) > 1:
        blinkings = int(sys.argv[1])

    if blinkings is None:
        blinkings = 6
    
    print("Blinkings: ", blinkings)

    with open(filename, 'r') as f:
        line = f.readline().split()

        stones = list(line)

        print("Stones: ", stones)
    
    total_stones = 0
    for s in stones:
        total_stones += run_blinkings(str(s), blinkings)
    print("Total stones: ", total_stones)