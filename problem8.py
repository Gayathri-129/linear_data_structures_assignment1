def are_brackets_closed(code):
    stack = []

    opening_brackets = {"(", "[", "{"}
    closing_brackets = {")", "]", "}"}

    bracket_pairs = {"(": ")", "[": "]", "{": "}"}

    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0 or bracket_pairs[stack[-1]] != char:
                return False
            else:
                stack.pop()

    return len(stack) == 0


code_snippet = """
def foo():
    if (x > 0) {
        print("Hello World!")
    }
}
"""

if are_brackets_closed(code_snippet):
    print("All brackets are closed.")
else:
    print("Some brackets are unclosed.")