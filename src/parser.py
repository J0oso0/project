def parse_expression(expression: str):
    """
    Parses a string representation of a form and returns a Form object.
    """
    expression = expression.replace(" ", "")  # Remove spaces
    stack = []
    current = None

    for char in expression:
        if char in {"□", "_"}:
            form = Form(char)
            if current:
                current.children.append(form)
            else:
                current = form
        elif char == "(":
            stack.append(current)
            current = None
        elif char == ")":
            if stack:
                parent = stack.pop()
                parent.children.append(current)
                current = parent

    return current if current else Form("□")
