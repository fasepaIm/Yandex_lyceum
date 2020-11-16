def arithmetic_operation(operation):
    if operation == '+':
        return lambda x, y: x + y
    if operation == '-':
        return lambda x, y: x - y
    if operation == '*':
        return lambda x, y: x * y
    if operation == '/':
        return lambda x, y: x / y