import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_first_line(self):
        md = """
# I am a title

nothing else..
well, maybe

i like dogs and cats
and stuff
"""
        title = extract_title(md)
        self.assertEqual(title, "I am a title")

    def test_extract_other_line(self):
        md = """
## Decoy!

i'm a paragraph
blocking
it

# i'm the real title

# i'm an impostor

# me

ok *fine*
"""
        title = extract_title(md)
        self.assertEqual(title, "i'm the real title")

    def test_extract_exception(self):
        md = """
## Decoy!

i'm a paragraph
blocking
it

ok *fine*
"""
    
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()