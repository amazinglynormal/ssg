import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_basic_to_html_usage_correct(self):
        node = LeafNode("p", "test paragraph text")
        self.assertEqual(node.to_html(), "<p>test paragraph text</p>")

    def test_raises_error_when_missing_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_returns_value_as_string_if_no_tag(self):
        node = LeafNode(None, "test paragraph text")
        self.assertEqual(node.to_html(), "test paragraph text")

    def test_to_html_renders_props_correctly(self):
        node = LeafNode(
            "a", "Test link", {"href": "http://www.example.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="http://www.example.com" target="_blank">Test link</a>',
        )


if __name__ == "__main__":
    unittest.main()
