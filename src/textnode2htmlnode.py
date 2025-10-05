from leafnode import LeafNode
from textnode import TextType


def textnode_to_htmlnode(textnode):
    enum_values = set(type.value for type in TextType)

    if textnode.text_type.value not in enum_values:
        raise Exception(
            f"TextNode does not have valid TextType: {textnode.text_type} was given"
        )

    match textnode.text_type:
        case TextType.TEXT:
            return LeafNode(None, textnode.text)
        case TextType.BOLD:
            return LeafNode("b", textnode.text)
        case TextType.ITALIC:
            return LeafNode("i", textnode.text)
        case TextType.CODE:
            return LeafNode("code", textnode.text)
        case TextType.LINK:
            return LeafNode("a", textnode.text, {"href": textnode.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})
