def scan_horizontally(puzzle, max_len, word, reverse_word, total_words):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if (j + max_len) > len(puzzle[i]):
                break
            
            puzzle_piece = ''.join(puzzle[i][j:j+max_len])
            
            if word == puzzle_piece or reverse_word == puzzle_piece:
                total_words += 1

    return total_words

def scan_vertically(puzzle, max_len, word, reverse_word, total_words):
    transposed_puzzle = list(zip(*puzzle))
    return scan_horizontally(transposed_puzzle, max_len, word, reverse_word, total_words)

def scan_diagonally(puzzle, max_len, word, reverse_word, total_words):
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
                total_words += 1
            
            ii = 0
            jj = 0
            puzzle_piece = ''
            while i+ii < len(puzzle) and j+jj < len(puzzle[i]) and j+jj >= 0 and len(puzzle_piece) < max_len:
                puzzle_piece += puzzle[i+ii][j+jj]
                ii += 1
                jj -= 1
           
            if word == puzzle_piece or reverse_word == puzzle_piece:
                total_words += 1
            
    return total_words

def scan(puzzle, word):
    total_words = 0

    max_len = len(word)

    reverse_word = word[::-1]

    total_words = scan_horizontally(puzzle, max_len, word, reverse_word, total_words)
    total_words = scan_vertically(puzzle, max_len, word, reverse_word, total_words)
    total_words = scan_diagonally(puzzle, max_len, word, reverse_word, total_words)
    
    return total_words

if __name__ == "__main__":
    filename = "input_4_test.txt"

    puzzle = []
    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            puzzle.append(list(line.strip()))
    
    print(scan(puzzle, "XMAS"))

