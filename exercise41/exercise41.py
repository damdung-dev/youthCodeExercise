import itertools

def calculate_expression(ops):
    try:
        result = eval(f"((((1 {ops[0]} 2) {ops[1]} 3) {ops[2]} 4) {ops[3]} 5) {ops[4]} 6")
        return result
    except ZeroDivisionError:
        return None

def find_expressions():
    operators = ['+', '-', '*', '/']
    for ops in itertools.product(operators, repeat=5):
        result = calculate_expression(ops)
        if result == 36:
            expression = f"((((1 {ops[0]} 2) {ops[1]} 3) {ops[2]} 4) {ops[3]} 5) {ops[4]} 6"
            print(f"{expression} = 36")

find_expressions()
