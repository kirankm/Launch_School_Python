from math import ceil

def print_in_box(text, max_width):
    text_width = len(text)
    if text_width > max_width - 4:
        text_width = max_width - 4
    text_arr = divide_text(text, text_width)

    vertical_padding = " " * text_width
    text_arr.insert(0, vertical_padding)
    text_arr.append(vertical_padding)

    side_padding = "| "
    padded_text_arr = [side_padding + content + side_padding[::-1] for content in text_arr]

    border = "+" + "-" * (text_width + 2) + "+"
    padded_text_arr.insert(0, border)
    padded_text_arr.append(border)
    print("\n".join(padded_text_arr))
    

def divide_text(text, text_width):
    text_arr = []
    lines = ceil(len(text) / text_width)
    for i in range(lines):
        start_point = i * text_width
        end_point = (i + 1) * text_width

        line = text[start_point:end_point]
        text_arr.append(line)
    print(text_arr)
    text_arr[-1] = text_arr[-1].center(text_width)
    return text_arr


print_in_box('To boldly go where no one has gone before.', 10)



## PEDAC
"""
Explicit Input
text :- str
max_width :- int :- Max widht of table

Explicit requirements
1 line of border above
1 lines of padding above

1 lines of padding below
1 line of border below

| and space on both sides for all lines except for the border

Text should be divided into multiple rows if text greater than max_width - 4


Implicit Requirements
The banner will be smaller than max width if text less than max_width - 4
Center the text, in last line if len(text) > max_width - 4
"""