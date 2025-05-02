def calculate_leftover_blocks(total_no_of_blocks):
    layer_number = 0
    blocks_remaining = total_no_of_blocks

    while blocks_remaining > 0:
        layer_number += 1
        blocks_required = layer_number ** 2
        if blocks_required > blocks_remaining:
            return blocks_remaining
        else:
            blocks_remaining -= blocks_required
    return 0

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # Truex
print(calculate_leftover_blocks(14) == 0) # True