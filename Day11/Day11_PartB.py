import sys
import copy

def run_rules(stone, current_blink, blinkings, cache):    
    if current_blink >= blinkings:
        return None 
    
    children = []
    while (current_blink < blinkings):        
        print("Current Blink: ", current_blink, " Stone: ", stone, " Cache: ", cache, "\n")                
        input()
        if stone in cache:
            result = cache[stone]                       
            if len(result) > (blinkings - current_blink):
                return None
        else:
            cache[stone] = []
        
        if stone == '0':
            next_stone = '1'
            cache[stone].append(next_stone)
            children = run_rules(next_stone, current_blink+1, blinkings, cache)            
            if children:
                cache[stone].append(children)
        elif len(stone) % 2 == 0:
            half = int(len(stone) / 2)
                
            left_stone = str(int(stone[0:half]))
            right_stone = str(int(stone[half:]))

            cache[stone].append(left_stone)
            children = run_rules(left_stone, current_blink+1, blinkings, cache)
            if children:
                cache[stone][len(cache[stone]-1)].append(children)
            
            cache[stone].append(right_stone)
            children = run_rules(right_stone, current_blink+1, blinkings, cache)            
            if children:
                cache[stone][len(cache[stone]-1)].append(children)
        else:                
            next_stone = str(int(stone) * 2024)
            cache[stone].append(next_stone)
            children = run_rules(next_stone, current_blink+1, blinkings, cache)                   
            if children:
                cache[stone].append(children)
    return children

if __name__ == "__main__":
    filename = "Day11_test.txt"

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
    
    cache = {}
    for s in stones:
        run_rules(s, 0, blinkings, cache)
    
    print("Cache: ", cache)
    #print("Final stone arrangement: ", final_stone_arrangement)
    # 185894
    #print("Total stones: ", len(final_stone_arrangement))