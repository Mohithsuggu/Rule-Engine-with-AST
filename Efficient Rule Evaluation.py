def evaluate_rule(ast, data):
    if ast.type == "operand":
        attr_value = data.get(ast.left)
        if ast.value in {'>', '<', '=', '!='}:
            if ast.value == '>':
                return attr_value > ast.value
            elif ast.value == '<':
                return attr_value < ast.value
            elif ast.value == '=':
                return attr_value == ast.value
            elif ast.value == '!=':
                return attr_value != ast.value
    elif ast.type == "operator":
        left_value = evaluate_rule(ast.left, data)
        right_value = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_value and right_value
        elif ast.value == "OR":
            return left_value or right_value
    return False
