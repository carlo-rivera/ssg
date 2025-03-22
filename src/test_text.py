import unittest
from text import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("hi im cute and bold and stuff", TextType.BOLD)  
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "hi im cute and bold and stuff")

    def test_italic(self):
        node = TextNode("leaning tower of pisa", TextType.ITALIC)  
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "leaning tower of pisa")

    def test_code(self):
        node = TextNode("print('i hate tests')", TextType.CODE)  
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('i hate tests')")

    def test_link(self):
        node = TextNode("cat videos", TextType.LINK, "https://cat-videos.com/")  
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "cat videos")
        self.assertEqual(html_node.props, {"href": "https://cat-videos.com/"})

    def test_image(self):
        node = TextNode("cute panda", TextType.IMAGE, "https://stockimage.com/cute-panda")  
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://stockimage.com/cute-panda", "alt": "cute panda"})

    def test_invalid_text(self):
        node = TextNode("invalid text type", "NOT_VALID")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()