from .context import mymod

import unittest

class BasicThingoTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_basic_thingo(self):
        thingo = mymod.Thingo()
        assert(thingo.get_one() == 1)

if __name__ == '__main__':
    unittest.main()
