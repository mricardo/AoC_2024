import re

def calculate(buttonA, buttonB, prize):
   total_cost = float('inf')
   tokenA = 3
   tokenB = 1

   for i in range(1, 100):
       for j in range(0, 100):
           X = buttonA[0] * i + buttonB[0] * j
           Y = buttonA[1] * i + buttonB[1] * j

           cost = i * tokenA + j * tokenB
 
           if (X, Y) == prize and cost < total_cost:
               total_cost = cost
           
           if (X > prize[0] or Y > prize[1]):
               break

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
            
            matches = re.findall(r'\d+', lines[i+1].strip())  
            buttonB= (int(matches[0]), int(matches[1]))

            matches = re.findall(r'\d+', lines[i+2].strip())
            prize = (int(matches[0]), int(matches[1]))

            cost = calculate(buttonA, buttonB, prize)
            if cost != float('inf'):
                total_cost += cost
            i += 4

    print("Total cost: ", total_cost)