import re

def calculate(buttonA, buttonB, prize):
   tokenA = 3
   tokenB = 1

   Px = prize[0]
   Py = prize[1]

   Ax = buttonA[0]
   Ay = buttonA[1]

   Bx = buttonB[0]
   By = buttonB[1]

   Na = (Px*By - Bx*Py) / (By * Ax - Bx * Ay)
   Nb = (Py - Ay * Na) / By

   print("Na: ", Na)
   print("Nb: ", Nb)

   if not Na.is_integer() or not Nb.is_integer():
       return float('inf')

   return Na * tokenA + Nb * tokenB

if __name__ == "__main__":
    filename = "Day13_test.txt"
    total_cost = 0
    add_measurement = 10000000000000
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        i = 0
        while i < len(lines):
            matches = re.findall(r'\d+', lines[i].strip())  
            buttonA = (int(matches[0]), int(matches[1]))
            
            matches = re.findall(r'\d+', lines[i+1].strip())  
            buttonB= (int(matches[0]), int(matches[1]))

            matches = re.findall(r'\d+', lines[i+2].strip())
            prize = (int(matches[0]) + add_measurement, int(matches[1]) + add_measurement)

            cost = calculate(buttonA, buttonB, prize)
            if cost != float('inf'):
                total_cost += cost
            
            print("Cost for ButtonA [", buttonA, "], ButtonB [", buttonB, "], Prize [", prize, "] = ", cost)

            i += 4

    print("Total cost: ", total_cost)