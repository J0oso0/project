import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("src/tests")
    runner = unittest.TextTestRunner()
    runner.run(suite)
