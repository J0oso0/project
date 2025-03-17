from src.form import Form
from src.parser import parse_expression

if __name__ == "__main__":
    f1 = Form("_", [Form("_")])  # Equivalent to _(_)
    f2 = Form("□")  # Unmarked state

    print("Original Form:", f1)
    print("Reduced Form:", f1.reduce())
    print("Is Equivalent to □?:", f1.is_equivalent(f2))

    # Example: Creating nested forms
    nested_form = Form("_", [Form("_", [Form("□")])])
    print("Nested Form:", nested_form)
    print("Reduced Nested Form:", nested_form.reduce())

    # Example: Parsing expressions
    parsed = parse_expression("_(_)")
    print("Parsed Expression:", parsed)
    print("Reduced Parsed Expression:", parsed.reduce())