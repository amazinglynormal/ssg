import unittest

from textnode import TextNode, TextType
from textnode2htmlnode import textnode_to_htmlnode


class TestTextNode2HTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def text_link(self):
        node = TextNode("This is a link node", TextType.LINK, "http://www.example.com")
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertIn("href", html_node.props)


if __name__ == "__main__":
    unittest.main()
