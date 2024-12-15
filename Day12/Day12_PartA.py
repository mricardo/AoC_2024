def search_radius(coord):    
    radius = []
    if coord[0] - 1 >= 0:        
        radius.append((coord[0] - 1, coord[1]))
    
    if coord[0] + 1 < len(puzzle):
        radius.append((coord[0] + 1, coord[1]))
    
    if coord[1] - 1 >= 0:
        radius.append((coord[0], coord[1] - 1))
    
    if coord[1] + 1 < len(puzzle[0]):        
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
    for region, positions in regions.items():
        perimeters[region] = 0
        symbol = puzzle[positions[0][0]][positions[0][1]]
        
        for p in positions:
            radius = search_radius(p)
            perimeter = 4 - len(radius)
        
            for r in radius:
                if puzzle[r[0]][r[1]] != symbol:
                    perimeter += 1
            
            if perimeter > 0:
                perimeters[region] += perimeter
            
    return perimeters

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
    perimeters = determine_perimeters(regions, puzzle)
    print(perimeters)
    print()
    total_price = 0
    for k,v in regions.items():
        area = len(v)
        perimeter = perimeters[k]
        print("Region: ", puzzle[v[0][0]][v[0][1]], " Area: ", area, " Perimiter: ", perimeter)

        total_price += area*perimeter
    
    print("Total price: ", total_price)