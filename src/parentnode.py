from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(None,tag,props,children)
    
    def to_html(self):
        if self.tag == "":
            raise ValueError("No tag for this parent")
        if self.children == None:
            raise ValueError("Node is not a parent")
        keys = []
        for i, v in enumerate(self.children):
            if isinstance(v,LeafNode):
                keys.append(i)
        if len(self.children) == 0 or len(keys) == 0:
            raise ValueError("Node is not a parent")
        childrun = ""
        for key in keys:
            childrun += self.children[key].to_html()
        return f'<{self.tag}>{childrun}</{self.tag}>'