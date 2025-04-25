from htmlnode import HTMLNode
from textnode import *

class LeafNode(HTMLNode):
    def __init__(self,value,tag=None,props=None):
        super().__init__(value,tag,props)
    
    def to_html(self):
        if self.tag == "img":
            return f'<{self.tag}{super().props_to_html()}>'
        if self.value == "":
            raise ValueError("No value for this leaf")
        if self.tag == None:
            return f'{self.value}'
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'    
        return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'
    
    def text_to_html(self,text_node):
        if text_node.text_type == TextType.TEXT:
            self.value = text_node.text
        if text_node.text_type == TextType.BOLD:
            self.value = text_node.text
            self.tag = "b"
        if text_node.text_type == TextType.ITALIC:
            self.value = text_node.text
            self.tag = "i"
        if text_node.text_type == TextType.CODE:
            self.value = text_node.text
            self.tag = "code"
        if text_node.text_type == TextType.LINK:
            self.value = text_node.text
            self.tag = "a"
            self.props = {"href":text_node.url}
        if text_node.text_type == TextType.IMAGE:
            self.value = ""
            self.tag = "img"
            self.props = {"src":text_node.url,"alt":text_node.text}