from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("all parent nodes must have a tag")
        if not self.children:
            raise ValueError("all parent nodes must have children with values")
        props = f" {self.props_to_html()}" if self.props else ""
        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        current_node = f"<{self.tag}{props}>{children_html}</{self.tag}>"

        return current_node