import unittest
from inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        old_nodes = [TextNode("Normal text in **TextType.BOLD** but normal again", TextType.TEXT),
                    TextNode("**Bold start** but normal ending", TextType.TEXT),
                    TextNode("Normal but **TextType.BOLD** and it's **twice**", TextType.TEXT)]
        new_node = [[TextNode("Normal text in ", TextType.TEXT),
                     TextNode("TextType.BOLD", TextType.BOLD),
                     TextNode(" but normal again", TextType.TEXT)],
                    [TextNode("Bold start", TextType.BOLD),
                     TextNode(" but normal ending", TextType.TEXT)],
                    [TextNode("Normal but ", TextType.TEXT),
                     TextNode("TextType.BOLD", TextType.BOLD),
                     TextNode(" and it's ", TextType.TEXT),
                     TextNode("twice", TextType.BOLD)]]
        self.assertEqual(split_nodes_delimiter(old_nodes, '**', TextType.BOLD),
                         split_nodes_delimiter(old_nodes, '**', TextType.BOLD), new_node)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )    

def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
def test_text_to_textnodes(self):
        matches = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            matches,
        )



if __name__ == "__main__":
    unittest.main()