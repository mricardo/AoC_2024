import sys

if __name__ == "__main__":
    filename = "input_1_1.txt"

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

    similarity_score = 0
    
    for num in list_a:
        count = list_b.count(num)

        similarity_score += num * count
    
    print(similarity_score)
