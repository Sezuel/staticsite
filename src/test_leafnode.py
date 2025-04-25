import unittest

from leafnode import LeafNode
from textnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        pass
        #Basic Tests
        '''node = LeafNode("This is a paragraph","p")
        node2 = LeafNode("This is italicized text","i")
        node3 = LeafNode("Click me!","a",{"href": "https://www.google.com"})
        node4 = LeafNode("I'm Tagless")
        #node5 = LeafNode("")
        print(node.to_html())
        print(node2.to_html())
        print(node3.to_html())
        print(node4.to_html())
        #print(node5.to_html())'''
        #Text to HTML tests
        '''node1 = LeafNode("")
        node1.text_to_html(TextNode("This is a test",TextType.TEXT))
        print(node1.to_html())
        node2 = LeafNode("")
        node2.text_to_html(TextNode("This is a bold test",TextType.BOLD))
        print(node2.to_html())
        node3 = LeafNode("")
        node3.text_to_html(TextNode("This is an italisized test",TextType.ITALIC))
        print(node3.to_html())
        node4 = LeafNode("")
        node4.text_to_html(TextNode("This is a codified test",TextType.CODE))
        print(node4.to_html())
        node5 = LeafNode("")
        node5.text_to_html(TextNode("This is a link test",TextType.LINK,"https://www.google.com"))
        print(node5.to_html())
        node6 = LeafNode("")
        node6.text_to_html(TextNode("This is an image test",TextType.IMAGE,"image.jpg"))
        print(node6.to_html())'''


if __name__ == "__main__":
    unittest.main()