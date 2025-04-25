import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        pass
        '''node = ParentNode("p",[LeafNode("This is a paragraph")])
        node2 = ParentNode("h1",[LeafNode("Click me!","a",{"href": "https://www.google.com"})])
        node3 = ParentNode("p",[LeafNode("Bold text","b"),LeafNode("Normal text"),LeafNode("italic text","i"),LeafNode("Normal text"),])
        node4 = ParentNode("p",[LeafNode("Bold text","b"),"This should not appear",LeafNode("Normal text"),LeafNode("italic text","i"),LeafNode("Normal text"),])
        #node5 = ParentNode("p",["This is italicized text"])
        #node6 = ParentNode("I'm Tagless",None)
        print(node.to_html())
        print(node2.to_html())
        print(node3.to_html())
        print(node4.to_html())
        #print(node5.to_html())
        #print(node6.to_html())'''

if __name__ == "__main__":
    unittest.main()