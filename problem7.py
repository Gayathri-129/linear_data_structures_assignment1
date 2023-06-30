
def is_operator(char):
    return char in "+-*/"


def prefix_to_infix(expression):
    stack = []
    for char in reversed(expression):
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expr = f"({operand1}{char}{operand2})"
            stack.append(infix_expr)
        else:
            stack.append(char)

    return stack.pop()


prefix_expr = "*+AB-CD"
infix_expr = prefix_to_infix(prefix_expr)
print("Prefix Expression:", prefix_expr)
print("Infix Expression:", infix_expr)