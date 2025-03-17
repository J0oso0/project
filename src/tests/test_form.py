import unittest
from src.form import Form

class TestFormOperations(unittest.TestCase):
    def test_reduction(self):
        f1 = Form("_", [Form("_")])  # Equivalent to _(_)
        self.assertEqual(f1.reduce(), Form("□"))

    def test_equivalence(self):
        f1 = Form("_", [Form("_")])
        f2 = Form("□")
        self.assertTrue(f1.is_equivalent(f2))

    def test_complexity(self):
        f1 = Form("_", [Form("_", [Form("□")])])
        self.assertEqual(f1.complexity(), 3)

if __name__ == "__main__":
    unittest.main()
