from turtle import pos, position


def search_radius(coord, all=False):    
    radius = []
    if coord[0] - 1 >= 0 or all:        
        radius.append((coord[0] - 1, coord[1]))
    
    if coord[0] + 1 < len(puzzle) or all:
        radius.append((coord[0] + 1, coord[1]))
    
    if coord[1] - 1 >= 0 or all:
        radius.append((coord[0], coord[1] - 1))
    
    if coord[1] + 1 < len(puzzle[0]) or all:        
        radius.append((coord[0], coord[1] + 1))
    
    return radius
    
def greedy_mark_region(current_symbol, current_region, current_position, pos_to_regions, regions_to_pos, puzzle):    
    radius = search_radius(current_position)

    unmapped_positions = []
    found_region = -1
    for r in radius:
        if puzzle[r[0]][r[1]] == current_symbol:
            if r in pos_to_regions:
                found_region = pos_to_regions[r]                
            else:            
                unmapped_positions.append(r)
    
    if found_region == -1:        
        current_region += 1
        found_region = current_region
        regions_to_pos[found_region] = []        
        
    pos_to_regions[current_position] = found_region
    if current_position not in regions_to_pos[found_region]:    
        regions_to_pos[found_region].append(current_position)

    for r in unmapped_positions:
        greedy_mark_region(current_symbol, current_region, r, pos_to_regions, regions_to_pos, puzzle)

def determine_perimeters(regions, puzzle):
    perimeters = {}
    perimeter_positions = {}
     
    for region, positions in regions.items():
        perimeters[region] = 0        
        perimeter_positions[region] = []
        symbol = puzzle[positions[0][0]][positions[0][1]]
        
        for p in positions:
            radius = search_radius(p)
            perimeter = 4 - len(radius)
        
            for r in radius:
                if puzzle[r[0]][r[1]] != symbol:
                    perimeter += 1                    

            if perimeter > 0:
                perimeters[region] += perimeter                
                perimeter_positions[region].append(p)              
                    
    return perimeters, perimeter_positions

def determine_regions(puzzle):
    pos_to_regions = {}
    regions_to_pos = {}
    count_region = 0
    
    i = 0
    while i < len(puzzle):
        j = 0        
        while j < len(puzzle[i]):
            coord = (i, j)           
            symbol = puzzle[i][j]
            if coord not in pos_to_regions:
                greedy_mark_region(symbol, count_region, coord, pos_to_regions, regions_to_pos, puzzle)           
            count_region = len(regions_to_pos)
            
            j += 1
        i += 1
    
    return regions_to_pos

def same_symbol(p, diagonal, puzzle):
    if diagonal[0] < 0 or diagonal[1] < 0:
        return False
    if diagonal[0] >= len(puzzle) or diagonal[1] >= len(puzzle[0]):
        return False

    symbol = puzzle[p[0]][p[1]]

    other_symbol = puzzle[diagonal[0]][diagonal[1]]

    return symbol == other_symbol

def not_all_in(check_p, positions):
    total = 0
    for p in check_p:
        if p not in positions:
            total += 1

    return total == len(check_p)

def is_all_in(check_p, positions):
    total = 0
    for p in check_p:
        if p in positions:
            total += 1

    return total == len(check_p)

def is_same_symbol(p, symbol, puzzle):
    if p[0] < 0 or p[1] < 0:
        return False
    
    if p[0] >= len(puzzle) or p[1] >= len(puzzle[0]):
        return False
    
    return puzzle[p[0]][p[1]] == symbol
  
def count_sides(positions):
    sides = 0 

    for p in positions:
        north = (p[0] - 1, p[1])
        north_east = (p[0] -1 , p[1] + 1)
        north_west = (p[0] -1 , p[1] - 1)

        south = (p[0] + 1, p[1])
        south_west = (p[0] + 1, p[1] - 1)

        east = (p[0], p[1] + 1)
        west = (p[0], p[1] - 1) 

        if north not in positions and (west not in positions or north_west in positions):
            sides += 1
        
        if south not in positions and (west not in positions or south_west in positions):
            sides += 1
        
        if west not in positions and (north not in positions or north_west in positions):
            sides += 1
        
        if east not in positions and (north not in positions or north_east in positions):
            sides += 1

    return sides

def determine_sides(regions_pos):
    sides_per_region = {}
    
    for r in regions_pos.keys():
        positions = regions_pos[r]        
        # sort by row then by column
        positions = sorted(positions, key=lambda x : (x[0], x[1]))
        sides = count_sides(positions)
        sides_per_region[r] = sides
    
    return sides_per_region

if __name__ == "__main__":
    filename = "Day12_test.txt"

    symbols = {}

    puzzle = []
    
    i = 0
    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            row = list(line.strip())
            puzzle.append(row)            

    regions = determine_regions(puzzle)
    perimeters, perimeter_positions = determine_perimeters(regions, puzzle)
    sides = determine_sides(regions)

    total_price = 0
    for k,v in regions.items():
        area = len(v)
        perimeter = perimeters[k]
        total_sides = sides[k]
        print("Region: ", puzzle[v[0][0]][v[0][1]], " Area: ", area, ", Sides: ", total_sides, " Price: ", total_sides * area)

        total_price += area*total_sides
    
    print("Total price: ", total_price)
