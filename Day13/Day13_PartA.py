
import re

def calculate(buttonA, buttonB, prize):
   total_cost = float('inf')
   tokenA = 3
   tokenB = 1
   bestA = -1
   bestB = -1

   for i in range(1, 100):
       for j in range(0, 100):
           X = buttonA[0] * i + buttonB[0] * j
           Y = buttonA[1] * i + buttonB[1] * j

           cost = i * tokenA + j * tokenB
 
           if X == prize[0] and Y == prize[1] and cost < total_cost:
               bestA = i
               bestB = j
               total_cost = cost

   print("Best A: ", bestA, "bestB ", bestB)
   return total_cost

if __name__ == "__main__":
    filename = "Day13_test.txt"
    total_cost = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        i = 0
        while i < len(lines):
            matches = re.findall(r'\d+', lines[i].strip())  
            buttonA = (int(matches[0]), int(matches[1]))
            
            print("Button A. X = ", buttonA[0], " Y = ", buttonA[1])

            matches = re.findall(r'\d+', lines[i+1].strip())  
            buttonB= (int(matches[0]), int(matches[1]))

            print("Button B. X = ", buttonB[0], " Y = ", buttonB[1])

            matches = re.findall(r'\d+', lines[i+2].strip())
            prize = (int(matches[0]), int(matches[1]))

            print("Prize. X = ", prize[0], " Y = ", prize[1])            
            print()
            cost = calculate(buttonA, buttonB, prize)
            print("Cost: ", cost)
            if cost != float('inf'):
                total_cost += cost
            i += 4
            
    print("Total cost: ", total_cost)
