import sys
import re

def print_puzzle(robots, wide, tall):
    puzzle = [[0 for _ in range(wide)] for _ in range(tall)]

    for r in robots:
        if puzzle[r[1]][r[0]] == 0:
            puzzle[r[1]][r[0]] = 1
        else:
            puzzle[r[1]][r[0]] += 1
    
    for p in puzzle:
        print(' '.join(p))

def run_simulation(robots, seconds, wide, tall):
    s = 0
    while s < seconds:
        
        r = 0
        while r < len(robots):
            px = robots[r][0]
            py = robots[r][1]
            vx = robots[r][2]
            vy = robots[r][3]

            new_px = (px + vx) % wide
            new_py = (py + vy) % tall

            robots[r] = (new_px, new_py, vx, vy)

            r += 1
        s += 1

def count_quadrants(robots, wide, tall):
    first_half_wide = int(wide / 2) - 1
    second_half_wide = wide / 2 if wide % 2 == 0 else int(wide / 2) + 1
    first_half_tall = int(tall / 2) - 1
    second_half_tall = tall / 2 if tall % 2 == 0 else int(tall / 2) + 1

    quadrant_1 = (0, first_half_wide, 0, first_half_tall)
    quadrant_2 = (second_half_wide, wide - 1, 0, first_half_tall)
    quadrant_3 = (0, first_half_wide, second_half_tall, tall-1)
    quadrant_4 = (second_half_wide, wide-1, second_half_tall, tall-1)

    quadrants = [quadrant_1, quadrant_2, quadrant_3, quadrant_4]
    robots_per_quadrant = {quadrant_1: 0, quadrant_2: 0, quadrant_3: 0, quadrant_4: 0}

    for r in robots:
        for q in quadrants:
            if r[0] >= q[0] and r[0] <= q[1] and \
               r[1] >= q[2] and r[1] <= q[3]:
                robots_per_quadrant[q] += 1
   
    safety_factor = 0
    for k,v in robots_per_quadrant.items():
        if safety_factor == 0:
            safety_factor = v
        else:
            safety_factor *= v
    
    return safety_factor

if __name__ == '__main__':
    filename = "Day14_test.txt"

    total_arguments = len(sys.argv)

    wide = 101
    tall = 103
    seconds = 100
    if total_arguments == 4:
        wide = int(sys.argv[1])
        tall = int(sys.argv[2])
        seconds = int(sys.argv[3])
    
    robots = []
    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            row = list(line.strip())

            matches = re.findall(r'-?\d+', line.strip())

            px = int(matches[0])
            py = int(matches[1])
            vx = int(matches[2])
            vy = int(matches[3])
            
            robots.append((px, py, vx, vy))
    
    run_simulation(robots, seconds, wide, tall)

    safety_factor = count_quadrants(robots, wide, tall)

    print("Safety factor: ", safety_factor)
