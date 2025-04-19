def print_in_box(text):
    text_len = len(text)
    out_array = []
    
    line15 = f"+{'-' * (text_len+2)}+"
    line24 = f"|{' ' * (text_len+2)}|"
    line3 = f"| {text} |"
    
    out_array.append(line15)
    out_array.append(line24)
    out_array.append(line3)
    out_array.append(line24)
    out_array.append(line15)
    
    print("\n".join(out_array))

print_in_box('To boldly go where no one has gone before.')
print_in_box('')
