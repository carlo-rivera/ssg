import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# I'm large!

## i'm **kinda**
`large` and
cool _last_ call

#### a little large
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>I'm large!</h1><h2>i'm <b>kinda</b> <code>large</code> and cool <i>last</i> call</h2><h4>a little large</h4></div>",
        )

    def test_quote(self):
        md = """
> "_No ID_ my mentor now let the arrow begin"
> a quote by
> - Kanye West (a great artist)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>\"<i>No ID</i> my mentor now let the arrow begin\"\na quote by\n- Kanye West (a great artist)</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- i _like_ eggs
- **but kanye** got evicted
- packed his shit in a uhaul
- 10 days b4 he had to get out
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>i <i>like</i> eggs</li><li><b>but kanye</b> got evicted</li><li>packed his shit in a uhaul</li><li>10 days b4 he had to get out</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. i _like_ eggs
2. **but kanye** got evicted
3. packed his shit in a uhaul
4. 10 days b4 he had to get out
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>i <i>like</i> eggs</li><li><b>but kanye</b> got evicted</li><li>packed his shit in a uhaul</li><li>10 days b4 he had to get out</li></ol></div>",
        )

if __name__ == "__main__":
    unittest.main()