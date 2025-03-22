import unittest
from node_split import split_nodes_delimiter
from textnode import TextNode, TextType

class TestNodeSplit(unittest.TestCase):
    def test_single_char_delim_occuring_once(self):
        text = "I like `code` it's cool"
        node1 = TextNode(text, TextType.TEXT)
        new_node = split_nodes_delimiter([node1], "`", TextType.CODE)
        self.assertEqual(new_node, [
            TextNode("I like ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" it's cool", TextType.TEXT),
        ])

    def test_single_char_delim_occuring_once_multiple_nodes(self):
        text1 = "I like *pepper* it tastes good"
        text2 = "Man I *love* eating chicken."
        text3 = "That chicken is *tasty* oh my god"
        node1 = TextNode(text1, TextType.TEXT)
        node2 = TextNode(text2, TextType.TEXT)
        node3 = TextNode(text3, TextType.TEXT)
        new_node = split_nodes_delimiter([node1, node2, node3], "*", TextType.ITALIC)
        self.assertEqual(new_node, [
            TextNode("I like ", TextType.TEXT),
            TextNode("pepper", TextType.ITALIC),
            TextNode(" it tastes good", TextType.TEXT),

            TextNode("Man I ", TextType.TEXT),
            TextNode("love", TextType.ITALIC),
            TextNode(" eating chicken.", TextType.TEXT),

            TextNode("That chicken is ", TextType.TEXT),
            TextNode("tasty", TextType.ITALIC),
            TextNode(" oh my god", TextType.TEXT),
        ])

    def test_single_char_delim_occuring_multiple(self):
        text = "I like `code` in fact I love `coding` so much that I `code for hours on end` it's crazy"
        node1 = TextNode(text, TextType.TEXT)
        new_node = split_nodes_delimiter([node1], "`", TextType.CODE)
        self.assertEqual(new_node, [
            TextNode("I like ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" in fact I love ", TextType.TEXT),
            TextNode("coding", TextType.CODE),
            TextNode(" so much that I ", TextType.TEXT),
            TextNode("code for hours on end", TextType.CODE),
            TextNode(" it's crazy", TextType.TEXT),
        ])

    def test_single_char_delim_unfinished(self):
        text = "I like `code` in fact I love `coding` so much that I `code for hours on end it's crazy"
        node1 = TextNode(text, TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node1], "`", TextType.CODE)

    def test_single_char_delim_ultimate(self):
        text1 = "Alright this is getting *ridiculous* I *can't* with this anymore"
        text2 = "I'm *done* I quit"
        text3 = "*Hey* alright so I *found* out about a *particular* person that *really* annoys me *so*"
        node1 = TextNode(text1, TextType.TEXT)
        node2 = TextNode(text2, TextType.TEXT)
        node3 = TextNode(text3, TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("Alright this is getting ", TextType.TEXT),
            TextNode("ridiculous", TextType.ITALIC),
            TextNode(" I ", TextType.TEXT),
            TextNode("can't", TextType.ITALIC),
            TextNode(" with this anymore", TextType.TEXT),

            TextNode("I'm ", TextType.TEXT),
            TextNode("done", TextType.ITALIC),
            TextNode(" I quit", TextType.TEXT),

            TextNode("Hey", TextType.ITALIC),
            TextNode(" alright so I ", TextType.TEXT),
            TextNode("found", TextType.ITALIC),
            TextNode(" out about a ", TextType.TEXT),
            TextNode("particular", TextType.ITALIC),
            TextNode(" person that ", TextType.TEXT),
            TextNode("really", TextType.ITALIC),
            TextNode(" annoys me ", TextType.TEXT),
            TextNode("so", TextType.ITALIC),
        ])

    def test_multi_char_delim_unfinished(self):
        text = "I like **code** in fact I love **coding** so much that I **code for hours on end it's crazy"
        node1 = TextNode(text, TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node1], "**", TextType.BOLD)

    def test_multi_char_delim_ultimate(self):
        text1 = "Alright this is getting **ridiculous** I **can't** with this anymore"
        text2 = "I'm **done** I quit"
        text3 = "**Hey** alright so I **found** out about a **particular** person that **really** annoys me **so**"
        node1 = TextNode(text1, TextType.TEXT)
        node2 = TextNode(text2, TextType.TEXT)
        node3 = TextNode(text3, TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("Alright this is getting ", TextType.TEXT),
            TextNode("ridiculous", TextType.BOLD),
            TextNode(" I ", TextType.TEXT),
            TextNode("can't", TextType.BOLD),
            TextNode(" with this anymore", TextType.TEXT),

            TextNode("I'm ", TextType.TEXT),
            TextNode("done", TextType.BOLD),
            TextNode(" I quit", TextType.TEXT),

            TextNode("Hey", TextType.BOLD),
            TextNode(" alright so I ", TextType.TEXT),
            TextNode("found", TextType.BOLD),
            TextNode(" out about a ", TextType.TEXT),
            TextNode("particular", TextType.BOLD),
            TextNode(" person that ", TextType.TEXT),
            TextNode("really", TextType.BOLD),
            TextNode(" annoys me ", TextType.TEXT),
            TextNode("so", TextType.BOLD),
        ])

    def test_non_text_type(self):
        node1 = TextNode("i'm just **normal** text", TextType.TEXT)
        node2 = TextNode("i'm bold!", TextType.BOLD)
        node3 = TextNode("more of **normal** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("i'm just ", TextType.TEXT),
            TextNode("normal", TextType.BOLD),
            TextNode(" text", TextType.TEXT),

            TextNode("i'm bold!", TextType.BOLD),

            TextNode("more of ", TextType.TEXT),
            TextNode("normal", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ])
    
    def test_empty_string(self):
        empty_node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([empty_node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [empty_node])

if __name__ == "__main__":
    unittest.main()