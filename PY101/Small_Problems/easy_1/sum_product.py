def sum(a,b):
    return a + b

def product(a,b):
    return a * b

op_dict = {
    's':sum,
    'p':product
}

def apply_op_on_range(number, operation):
    result = number
    for val in range(1, number):
        result = operation(result, val)
    return result

number = int(input("Please enter an integer greater than 0: "))
operation_choice = input("Enter 's' to compute the sum, or 'p' to compute the product. ")
chosen_operation = op_dict[operation_choice]

answer = apply_op_on_range(number, chosen_operation)

print(f"The {chosen_operation.__name__} of the integers between 1 and {number} is {answer}")
