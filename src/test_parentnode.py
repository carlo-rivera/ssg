import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child")
        child_node2 = LeafNode("a", "example link", {"href": "https://example.com/"})
        child_node3 = LeafNode("b", "bold text")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><a href=\"https://example.com/\">example link</a><b>bold text</b></div>")

    def test_to_html_with_nested_children(self):
        child_node1 = LeafNode("span", "child")

        grandchild_node1 = LeafNode("i", "grandchild")
        grandchild_node2 = LeafNode("a", "grippy", {"href": "https://jcole.com/"})

        child_node2 = ParentNode("div", [grandchild_node1, grandchild_node2])
        child_node3 = LeafNode("b", "bold text")

        grandchild_node3 = LeafNode("span", "third grandchild")

        great_grandchild_node1 = LeafNode("b", "woah")
        great_grandchild_node2 = LeafNode("i", "im italic")

        grandchild_node4 = ParentNode("div", [great_grandchild_node1, great_grandchild_node2])

        child_node4 = ParentNode("span", [grandchild_node3, grandchild_node4])

        grandchild_node5 = LeafNode("i", "im base level italic")

        child_node5 = ParentNode("span", [grandchild_node5])

        child_node6 = LeafNode("a", "yt", {"href": "https://youtube.com/"})

        parent_node = ParentNode("div", [child_node1, child_node2, child_node3, child_node4, child_node5, child_node6])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child</span><div><i>grandchild</i><a href=\"https://jcole.com/\">grippy</a></div><b>bold text</b><span><span>third grandchild</span><div><b>woah</b><i>im italic</i></div></span><span><i>im base level italic</i></span><a href=\"https://youtube.com/\">yt</a></div>"
        )
    
if __name__ == "__main__":
    unittest.main()