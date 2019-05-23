#!python3
"""

Boyer-Moore substring search

"""
import unittest


def bm_search(pattern, text):
    if not pattern or not text:
        return -1
    plen = len(pattern)
    right_chars = {pattern[i]: i for i in range(plen)}
    i = 0
    while i < len(text) - plen + 1:
        skip = 0
        for j in range(plen-1, -1, -1):
            if text[i+j] != pattern[j]:
                """
                This is the trickest part. Skip not 1 each time but as more
                as possible.
                1. If char in pattern, place at the most right char. Example:
                    ....BAB...
                     BABCAB
                     i  j
                    into:
                    ....BAB...
                        BABCAB
                2. If char not in pattern skip to the after the mismatched.
                """
                if text[i+j] in right_chars:
                    skip = j - right_chars[text[i+j]]
                else:
                    skip = j + 1
                if skip < 1:
                    skip = 1
        if skip == 0:  # found
            return i
        i += skip
    return -1  # not found


class BMTests(unittest.TestCase):
    def test_13_chars(self):
        text = "ABRACADABRA"
        #       01234567890
        pattern = "DABR"
        self.assertEqual(bm_search(pattern, text), 6)

    def test_19_repeating_chars(self):
        text = "AACAACAACAACAAACAAC"
        #       01234567890123456789
        pattern = "AAAC"
        self.assertEqual(bm_search(pattern, text), 12)

    def test_empty(self):
        self.assertEqual(bm_search("A", ""), -1)
        self.assertEqual(bm_search("", "A"), -1)

    def test_long(self):
        text = """
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore e t dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. S tet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit ame t, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam e rat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,  no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. A t vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."""
        pattern = "labore et dolore"
        self.assertEqual(bm_search(pattern, text), 399)

    def test_random(self):
        self.assertEqual(bm_search('a', 'a'), 0)
        self.assertEqual(bm_search('a', 'ba'), 1)
        """
        baab  ->   baab
        aab         aab
        """
        self.assertEqual(bm_search('aab', 'baab'), 1)
        self.assertEqual(bm_search('needle', 'xxxxxexxneedle'), 8)
        self.assertEqual(bm_search('needle', 'eedle'), -1)


if __name__ == '__main__':
    unittest.main()
