import unittest

from delimiter import *
from textnode import *

class TestDelimiter(unittest.TestCase):
    def test_eq(self):
        pass
        '''node = TextNode("This is *a* title",TextType.TEXT)
        print(split_nodes([node],'*',TextType.TEXT))
        node = TextNode("This is **a** title",TextType.TEXT)
        print(split_nodes([node],'**',TextType.TEXT))
        node = TextNode("This is `a` title",TextType.TEXT)
        print(split_nodes([node],'`',TextType.TEXT))
        node = TextNode("This is **a** title",TextType.TEXT)
        print(split_nodes([node],'*',TextType.TEXT))
        node = TextNode("*This is *a* title*",TextType.ITALIC)
        print(split_nodes([node],'*',TextType.TEXT))'''

if __name__ == "__main__":
    unittest.main()