def evaluate_expression(s):
    def evaluate(stack):
        res = 0
        num = 0
        sign = 1  # 1 for positive, -1 for negative

        while stack:
            token = stack.pop()

            if token == '(':
                # End of this parenthesis level
                break
            elif token.isdigit():
                # Forming a number
                num = int(token) + num * 10
            elif token in '+-':
                # Process previous number
                res += sign * num
                num = 0
                sign = 1 if token == '+' else -1

        res += sign * num
        return res

    # Parse the input string
    stack = []
    for char in reversed(s.replace(" ", "")):
        if char == ')':
            # Push closing parenthesis onto the stack
            stack.append('(')
        elif char == '(':
            result = evaluate(stack)
            stack.append(str(result))  # Push evaluated result
        else:
            stack.append(char)

    return evaluate(stack)

# Example usage
expression = "3 + (2 - (5 + 1)) + 8"
result = evaluate_expression(expression)
print(f"The result of the expression '{expression}' is {result}.")
