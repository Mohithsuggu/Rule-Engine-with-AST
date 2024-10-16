def combine_rules(rules):
    """Combines multiple rule strings into a single AST, minimizing redundancy."""
    def merge_trees(tree1, tree2):
        """Merge two ASTs with AND operation while checking for redundancy."""
        # If both trees are the same, return one of them
        if tree1 == tree2:
            return tree1
        # Otherwise, create a new operator node
        return Node("operator", left=tree1, right=tree2, value="AND")

    root = None
    seen_expressions = {}

    for rule in rules:
        ast = create_rule(rule)
        
        # Check for existing sub-expressions to minimize redundancy
        expression_key = repr(ast)  # Use string representation for uniqueness

        if expression_key in seen_expressions:
            # If the expression already exists, use the existing node
            existing_ast = seen_expressions[expression_key]
            root = merge_trees(root, existing_ast) if root else existing_ast
        else:
            # If new, add to seen expressions
            seen_expressions[expression_key] = ast
            root = merge_trees(root, ast) if root else ast

    return root
