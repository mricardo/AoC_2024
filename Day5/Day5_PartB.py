def custom_bubble_sort(ordered_list, keys):
  n = len(keys)

  for i in range(n):
    for j in range(0, n-i-1):
      if keys[j+1] in ordered_list and keys[j] in ordered_list[keys[j+1]]:
        keys[j], keys[j+1] = keys[j+1], keys[j]

if __name__ == "__main__":
    filename = "Day5_input.txt"

    ordered_list = {}
    sort_order = []
    total =+ 0
    with open(filename, "r") as f:
        lines = f.readlines()
        
        sum_middle_number = 0

        for line in lines:
            if "|" in line:
                key,value = line.strip().split("|")
                if key not in ordered_list:
                    ordered_list[key] = []

                ordered_list[key].append(value)
                
            elif len(line.strip()) > 0:
                keys = line.strip().split(",")
                update_correct = True
                for index, key in enumerate(keys):
                    ordering = ordered_list[key] if key in ordered_list else []
                    update = keys[index+1:]
                    if not set(update).issubset(set(ordering)):
                        update_correct = False
                        break
                
                if not update_correct:
                    custom_bubble_sort(ordered_list, keys)
                    middle = len(keys) // 2
                    sum_middle_number += int(keys[middle])
        
        print(sum_middle_number)