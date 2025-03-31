def multiply():
    first = input("Enter the first number: ").strip()
    second = input("Enter the second number: ").strip()
    answer = float(first) * float(second)
    print(f'{first} * {second} = {answer}')


multiply()