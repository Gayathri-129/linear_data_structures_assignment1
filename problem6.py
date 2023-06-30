def postfix_to_prefix(expression):
    stack = []

    for token in expression:
        if token.isalnum():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix = token + operand1 + operand2
            stack.append(prefix)

    return stack.pop()


postfix_expression = "34+5*"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)