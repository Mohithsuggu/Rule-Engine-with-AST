import re

def parse_condition(condition):
    match = re.match(r"(\w+)\s*([<>=!]+)\s*(.+)", condition)
    if match:
        attr, operator, value = match.groups()
        return Node("operand", value=value, left=attr, right=operator)
    return None

def create_rule(rule_string):
    # Tokenize and construct the AST from the rule string.
    # Handle precedence and parentheses correctly.
    tokens = re.findall(r'\w+|AND|OR|\(|\)', rule_string)
    stack = []
    output = []

    precedence = {'AND': 2, 'OR': 1}

    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        elif token in precedence:
            while (stack and stack[-1] in precedence and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        else:
            # Assume the token is a condition
            output.append(parse_condition(token))

    while stack:
        output.append(stack.pop())

    return build_ast(output)

def build_ast(output):
    stack = []
    for token in output:
        if isinstance(token, Node):
            stack.append(token)
        else:  # It's an operator
            right = stack.pop()
            left = stack.pop()
            stack.append(Node("operator", left=left, right=right, value=token))
    return stack.pop()
