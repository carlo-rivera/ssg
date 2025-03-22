import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_nc(self):
        node = LeafNode("p", "Hello, world!", {"a": "b"})
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"a": "b"})
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Some bold text")
        self.assertEqual(node.to_html(), "<b>Some bold text</b>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "a link", {"href": "https://boot.dev/"})
        self.assertEqual(node.to_html(), "<a href=\"https://boot.dev/\">a link</a>")

if __name__ == "__main__":
    unittest.main()