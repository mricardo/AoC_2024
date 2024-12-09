def print_puzzle(puzzle):
    for row in puzzle:
        for item in row:
            print(item, end=" ")
        print()

def search_antenas(row, antenas, i):
    for j, r in enumerate(row):
        if r != '.':
            if r not in antenas:
                antenas[r] = []

            antenas[r].append((i, j))

def set_antinodes(puzzle, antenas):
    antinodes = []
    for index, (antena, locations) in enumerate(antenas.items()):
        for i, l in enumerate(locations):
            current_location = locations[i]
            for j, l in enumerate(locations):
                if i != j:
                    other_location = locations[j]
                    while True:
                        row = current_location[0] - other_location[0]
                        col = current_location[1] - other_location[1]

                        row_antinode = current_location[0] + row 
                        col_antinode = current_location[1] + col
                        if current_location not in antinodes:
                            antinodes.append(current_location)
                            
                        if other_location not in antinodes:
                            antinodes.append(other_location)
                        
                        if (not row_antinode < 0 and not row_antinode >= len(puzzle)) and \
                            (not col_antinode < 0 and not col_antinode >= len(puzzle[0])):
                            if puzzle[row_antinode][col_antinode] == '.':
                                puzzle[row_antinode][col_antinode] = 'X'
                            
                            new_antinode = (row_antinode, col_antinode)
                            if new_antinode not in antinodes:
                                antinodes.append(new_antinode)
                            
                            other_location = current_location
                            current_location = new_antinode
                        else:
                            break
                    current_location = locations[i]
    return antinodes

if __name__ == "__main__":
    filename = "Day8_input.txt"

    puzzle = []

    with open(filename, 'r') as f:
        lines = f.readlines()
        antenas = {}
        
        i = 0
        for line in lines:
            row = list(line.strip())

            search_antenas(row, antenas, i)

            puzzle.append(row)

            i += 1
    
        antinodes = set_antinodes(puzzle, antenas)
        print("Antinodes: ", len(antinodes))