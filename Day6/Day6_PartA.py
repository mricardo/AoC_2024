def run_puzzle(puzzle, guard_index):
    guard = puzzle[guard_index[0]][guard_index[1]]
    positions = 1
    new_index = guard_index

    while True: 
        if guard == '^':
            new_index = (new_index[0]-1, new_index[1])
            rotate_guard = '>'
        if (guard == '>'):
            new_index = (new_index[0], new_index[1]+1)
            rotate_guard = 'v'
        if (guard == 'v'):
            new_index = (new_index[0]+1, new_index[1])
            rotate_guard = '<'
        if (guard == '<'):
            new_index = (new_index[0], new_index[1]-1)
            rotate_guard = '^'

        if (new_index[0] == -1 or new_index[0] >= len(puzzle)):
            break

        if (new_index[1] == -1 or new_index[1] >= len(puzzle[0])):
            break
        
        new_position = puzzle[new_index[0]][new_index[1]] 
        
        if (new_position == '.'):
            positions += 1
            puzzle[guard_index[0]][guard_index[1]] = 'X'
            guard_index = new_index
        
        if (new_position == '#'):
            guard = rotate_guard
            new_index = guard_index
        
    return positions

if __name__ == "__main__":
    filename = "Day6_input.txt"

    puzzle = []
    guard_index = (-1,-1)
    
    row_index = 0
    col_index = -1

    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            row = list(line.strip())
            
            col_index = row.index('^') if '^' in row else col_index
            col_index = row.index('>') if '>' in row else col_index
            col_index = row.index('v') if 'v' in row else col_index
            col_index = row.index('<') if '<' in row else col_index
            
            if col_index != -1 and guard_index[0] == -1:
                guard_index = (row_index, col_index)

            puzzle.append(row)

            row_index += 1
    
    positions = run_puzzle(puzzle, guard_index)

    print(positions)