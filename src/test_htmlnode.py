import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLNode()
        node2 = HTMLNode("tag")
        node3 = HTMLNode("tag", "value")
        node4 = HTMLNode("tag", "value", "children")
        node5 = HTMLNode("tag", "value", "children", "props")
        self.assertTupleEqual((node.tag, node.value, node.children, node.props), (None,) * 4)
        self.assertTupleEqual((node2.tag, node2.value, node2.children, node2.props), ("tag", None, None, None))
        self.assertTupleEqual((node3.tag, node3.value, node3.children, node3.props), ("tag", "value", None, None))
        self.assertTupleEqual((node4.tag, node4.value, node4.children, node4.props), ("tag", "value", "children", None))
        self.assertTupleEqual((node5.tag, node5.value, node5.children, node5.props), ("tag", "value", "children", "props"))

    def test_props_to_html(self):
        node = HTMLNode("tag", "value", "children", {
            "testkey": "testvalue",
            "moreKey": "Morevalue",
            "primeagen": "lane"
        })

        self.assertEqual(node.props_to_html(), "testkey=\"testvalue\" moreKey=\"Morevalue\" primeagen=\"lane\"")

    def test_props_to_html_rig(self):
        node = HTMLNode("tag", "value", "children", {
            "testkey": "testvalue",
            "moreKey": "Morevalue",
            "primeagen": "lane",
            "plane": "osama",
            "a": "b",
            "e": "mc^2"
        })

        self.assertEqual(node.props_to_html(), "testkey=\"testvalue\" moreKey=\"Morevalue\" primeagen=\"lane\" plane=\"osama\" a=\"b\" e=\"mc^2\"")
        

if __name__ == "__main__":
    unittest.main()