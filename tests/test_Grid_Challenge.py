from production_code.Grid_Challenge import grid_challenge
import unittest

class TestGridChallenge(unittest.TestCase):
    def test_grid_challenge_sorted_grid(self):
        grid = ["abc", "ade", "efg"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)
    
    def test_grid_challenge_unsorted_grid(self):
        grid = ["ebc", "ade", "efg"]
        expected = "NO"
        self.assertEqual(grid_challenge(grid), expected)
    
    def test_grid_challenge_single_row(self):
        grid = ["zxy"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)
    
    def test_grid_challenge_identical_rows(self):
        grid = ["aaa", "aaa", "aaa"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)
    
    def test_grid_challenge_mixed_case(self):
        grid = ["aBc", "Ade", "eFg"]
        expected = "NO"
        self.assertEqual(grid_challenge(grid), expected)