import unittest, sys

class Finding_a_Motif_in_DNA_Test(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, "../programs")
        from programs import P9_SUBS.py
    
    def test_substring_match_exists(self):
        assert substring_match("abcde") is True

if __name__ == "__main__":
    unittest.main()