
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

def find_free_space(disk_layout):
    try:
        return disk_layout.index('.')
    except ValueError:
        return -1
    
def rearrange_disk_layout(disk_layout):
    for i in range(len(disk_layout) - 1, -1, -1):

        block = disk_layout[i]
        if block != '.':
            free_space = find_free_space(disk_layout)
            if free_space != -1 and free_space < i:
                disk_layout[free_space] = block
                disk_layout[i] = '.'

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
    print("Rearranged layout: ", ''.join(str(e) for e in rearranged_layout))
    checksum = calculate_checksum(rearranged_layout)
    # 6310675819476
    print("Checksum: ", checksum)