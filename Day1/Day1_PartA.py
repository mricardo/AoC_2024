import sys

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        lines = f.readlines()

    list_a = []
    list_b = []
    for line in lines:
        numbers = line.strip().split()
        num1 = int(numbers[0])
        num2 = int(numbers[1])

        list_a += [num1]
        list_b += [num2]

    total_distance = 0
    while len(list_a) != 0:
        min_a = min(list_a)
        min_b = min(list_b)
        
        list_a.remove(min_a)
        list_b.remove(min_b)

        total_distance += abs(min_a - min_b)
    
    print(total_distance)
