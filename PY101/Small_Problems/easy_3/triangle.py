def triangle(size):
    print('\n'.join([(val * '*').rjust(size)  for val in range(1, size + 1) ]))