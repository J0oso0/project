class Form:
    """
    Represents a symbolic form in Spencer-Brown calculus.
    """

    def __init__(self, value, children=None):
        self.value = value  # Can be □, _, or another symbol
        self.children = children if children else []

    def __repr__(self):
        """String representation for debugging."""
        if self.children:
            return f"{self.value}({', '.join(map(str, self.children))})"
        return self.value

    def __eq__(self, other):
        """Equivalence of forms based on structure and value."""
        return isinstance(other, Form) and self.value == other.value and self.children == other.children

    def reduce(self):
        """Apply reduction rules to simplify expressions."""
        reduced_children = [child.reduce() for child in self.children]

        if self.value == "□":
            return self  # Unmarked remains unchanged

        # Cancellation: _(_) → □
        if self.value == "_" and len(reduced_children) == 1 and reduced_children[0].value == "_":
            return Form("□")

        # Condensation: _ _ → _
        if self.value == "_" and all(child.value == "_" for child in reduced_children):
            return Form("_")

        # Juxtaposition preservation: _ □ → _ (□)
        if self.value == "_" and len(reduced_children) == 1 and reduced_children[0].value == "□":
            return Form("_", [Form("□")])

        return Form(self.value, reduced_children)

    def is_equivalent(self, other):
        """Checks if two forms belong to the same equivalence class."""
        return self.reduce() == other.reduce()
