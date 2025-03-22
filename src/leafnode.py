from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have a value")
        if not self.tag:
            return self.value
        
        props = f" {self.props_to_html()}" if self.props else ""
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"