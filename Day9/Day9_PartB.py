def create_disk_layout(disk_map):
    disk_layout = []
    block_ids = 0

    for idx, element in enumerate(disk_map):
        if idx % 2 == 0:
            i = 0
            while i < int(element):
                disk_layout.append(block_ids)
                i += 1
            block_ids += 1
        else:
            i = 0
            while i < int(element):
                disk_layout.append('.')
                i += 1

    return disk_layout

def find_block(disk_layout, free_block, block_init):
    idx = 0
    size = len(free_block)

    while idx + size < len(disk_layout) and idx+size <= block_init:
        check_block = disk_layout[idx:idx+size]

        if check_block == free_block:
            return idx
        idx += 1
    return -1

def rearrange_disk_layout(disk_layout):
    block_end = len(disk_layout) - 1

    while block_end > 0:
        block_size = 1
        block = disk_layout[block_end]

        if block != '.':    
            block_init = disk_layout.index(block)
            block_size = block_end - block_init + 1
            block_list = disk_layout[block_init:block_end+1]

            free_block =  ['.'] * block_size
            found_block = find_block(disk_layout, free_block, block_init)
            
            if found_block != -1:
                disk_layout[found_block:found_block+block_size] = block_list
                disk_layout[block_init:block_end+1] = free_block
        
        block_end -= block_size
        
    return disk_layout

def calculate_checksum(rearranged_layout):
    checksum = 0
    for idx, block in enumerate(rearranged_layout):
        if block != '.':
            checksum += idx * block
    
    return checksum

if __name__ == "__main__":
    filename = "Day9_input.txt"

    disk_map = ''
    with open(filename, 'r') as f:
        disk_map = f.readline().strip()

    disk_layout = create_disk_layout(disk_map)
    rearranged_layout = rearrange_disk_layout(disk_layout)
    checksum = calculate_checksum(rearranged_layout)

    print("Checksum: ", checksum)