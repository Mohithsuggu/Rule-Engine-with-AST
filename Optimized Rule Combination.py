def combine_rules(rules):
    root = None
    for rule in rules:
        ast = create_rule(rule)
        if root is None:
            root = ast
        else:
            # Here we combine with AND by default for simplicity.
            # More complex logic can be applied to minimize redundancy.
            root = Node("operator", left=root, right=ast, value="AND")
    return root
