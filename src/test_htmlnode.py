import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html_method(self):
        node = HTMLNode(
            "p", "test text value", None, {"class": "test_classname", "id": "test_id"}
        )
        self.assertEqual(node.props_to_html(), ' class="test_classname" id="test_id"')


if __name__ == "__main__":
    unittest.main()
