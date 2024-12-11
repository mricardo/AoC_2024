import sys
import copy

def run_rules(current_stones, blinkings):    
    blink = 0
    stone_idx = 0
    while (blink < blinkings):        
        print("Blink: ", blink)
        stone_idx = 0
        original_stones = copy.deepcopy(current_stones)

        for stone in original_stones:
            if stone == '0':
                current_stones[stone_idx] = '1'
                stone_idx += 1
            elif len(stone) % 2 == 0:
                half = int(len(stone) / 2)
                
                left_stone = str(int(stone[0:half]))
                right_stone = str(int(stone[half:]))

                current_stones = current_stones[0:stone_idx] + [left_stone] + [right_stone] + current_stones[stone_idx+1:]
                
                stone_idx += 2                
            else:
                
                current_stones[stone_idx] = str(int(stone) * 2024)                
                
                stone_idx += 1
                
        blink += 1
    
    return current_stones

if __name__ == "__main__":
    filename = "Day11_input.txt"

    blinkings = None
    if len(sys.argv) > 1:
        blinkings = int(sys.argv[1])

    if blinkings is None:
        blinkings = 25
    
    print("Blinkings: ", blinkings)

    with open(filename, 'r') as f:
        line = f.readline().split()

        stones = list(line)

        print("Stones: ", stones)
    
    final_stone_arrangement = run_rules(stones, blinkings)
    print("Final stone arrangement: ", final_stone_arrangement)
    # 185894
    print("Total stones: ", len(final_stone_arrangement))