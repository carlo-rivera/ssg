class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        props_kv = list(map(
            lambda prop_name: f"{prop_name}=\"{self.props[prop_name]}\"", 
            self.props
        ))

        return " ".join(props_kv)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"