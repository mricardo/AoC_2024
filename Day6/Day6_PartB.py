import copy

# 1909

def run_puzzle(puzzle, guard_index):
    guard = puzzle[guard_index[0]][guard_index[1]]
    
    new_index = guard_index
    start_index = guard_index
    start_position = guard

    obstrusions = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if ((i,j) != start_index and puzzle[i][j] == '.'):
                test_puzzle = copy.deepcopy(puzzle)

                guard_index = start_index
                new_index = start_index
                guard = start_position

                seen_obstacles = {}
                test_puzzle[i][j] = 'O'
                cornoured = 0
                
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

                    if (new_index[0] == -1 or new_index[0] >= len(test_puzzle)):
                        break

                    if (new_index[1] == -1 or new_index[1] >= len(test_puzzle[0])):
                        break
                    
                    new_position = test_puzzle[new_index[0]][new_index[1]] 
                   
                    if (new_position == '.' or new_position=='X'):
                        test_puzzle[guard_index[0]][guard_index[1]] = 'X'
                        guard_index = new_index
                        
                    if (new_position == '#' or new_position == 'O'):
                        guard = rotate_guard
                        new_index = guard_index
                        if new_index in seen_obstacles:
                            seen_obstacles[new_index] = seen_obstacles[new_index] + 1

                            if seen_obstacles[new_index] >= 4:
                                cornoured += 1
                            
                            if cornoured >= 2:
                                obstrusions += 1
                                break
                        else:
                            seen_obstacles[new_index] = 1
                    
    return obstrusions

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