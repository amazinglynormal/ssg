import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_when_url_added(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, "http://www.google.com")
        self.assertNotEqual(node, node2)

    def test_not_equal_with_diff_text_type(self):
        node = TextNode("This is a text node", TextType.LINK, "http://www.google.com")
        node2 = TextNode("This is a text node", TextType.IMAGE, "http://www.google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
