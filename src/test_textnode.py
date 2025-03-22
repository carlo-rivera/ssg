import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a cool node", TextType.CODE)
        node2 = TextNode("This is a boring node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is a cool node", TextType.CODE)
        node2 = TextNode("This is a cool node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a url node", TextType.LINK, "https://antisemitic.com")
        node2 = TextNode("This is a url node", TextType.LINK, "https://kanye.com")
        self.assertNotEqual(node, node2)

    def test_url_default(self):
        node = TextNode("im a really cool url", TextType.LINK)
        self.assertTrue(node.url is None)
    

if __name__ == "__main__":
    unittest.main()