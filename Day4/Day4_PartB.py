def scan_diagonally_right_left(puzzle, i, j, max_len, word, reverse_word):
    if (i >= len(puzzle) or j >= len(puzzle[i])):
        return False
    
    ii = 0
    jj = 0
    puzzle_piece = ''
    while i+ii < len(puzzle) and j+jj < len(puzzle[i]) and j+jj >= 0 and len(puzzle_piece) < max_len:
        puzzle_piece += puzzle[i+ii][j+jj]
        ii += 1
        jj -= 1
        
    if word == puzzle_piece or reverse_word == puzzle_piece:
        return True
            
    return False

def scan_diagonally_left_right(puzzle, max_len, word, reverse_word):
    total_words = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            ii = 0
            jj = 0

            puzzle_piece = ''
            while i+ii < len(puzzle) and j+jj < len(puzzle[i]) and len(puzzle_piece) < max_len:
                puzzle_piece += puzzle[i+ii][j+jj]
                ii += 1
                jj += 1
            
            if word == puzzle_piece or reverse_word == puzzle_piece:
                if (scan_diagonally_right_left(puzzle, i, j + len(word)-1, max_len, word, reverse_word)):
                    total_words += 1
            
    return total_words

def scan(puzzle, word):
    max_len = len(word)

    reverse_word = word[::-1]

    return scan_diagonally_left_right(puzzle, max_len, word, reverse_word)
    
if __name__ == "__main__":
    filename = "input_4_test.txt"

    puzzle = []
    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            puzzle.append(list(line.strip()))
    
    print(scan(puzzle, "MAS"))

