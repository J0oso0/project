import unittest
from src.parser import parse_expression
from src.form import Form

class TestParser(unittest.TestCase):
    def test_parsing(self):
        parsed = parse_expression("_(_)")
        self.assertEqual(parsed, Form("_", [Form("_")]))
        self.assertEqual(parsed.reduce(), Form("□"))

if __name__ == "__main__":
    unittest.main()
