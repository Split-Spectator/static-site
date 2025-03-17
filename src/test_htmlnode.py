import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_same_props(self):
        # Create two nodes with identical properties
        node_1 = HTMLNode(
            tag="a",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        node_2 = HTMLNode(
            tag="a",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        # Assert they are equal
        self.assertEqual(node_1, node_2)

    def test_eq_same_tag_and_value(self):
        # Create two nodes with identical tag and value
        node_1 = HTMLNode(tag="title", value="Why Frontend Development Sucks")
        node_2 = HTMLNode(tag="title", value="Why Frontend Development Sucks")
        # Assert they are equal
        self.assertEqual(node_1, node_2)

    def test_not_equal_different_nodes(self):
        # Create two nodes with differing tag and value
        node_1 = HTMLNode(tag="li", value="hate writing")
        node_2 = HTMLNode(tag="title", value="Why Frontend Development Sucks")
        # Assert they are not equal
        self.assertNotEqual(node_1, node_2)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_l(self):
        node = LeafNode("li", "This is a line")
        self.assertEqual(node.to_html(), "<li>This is a line</li>")
    
    def test_leaf_to_html_h(self):
        node = LeafNode("h1", "This is a Header")
        self.assertEqual(node.to_html(), "<h1>This is a Header</h1>")

    def test_error_handle(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")
    
    def test_error_handle_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_children2(self):
        child_node = LeafNode("span", "stepchild")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>stepchild</span></div>")

    def test_to_html_with_grandchildren2(self):
        grandchild_node = LeafNode("b", "greatgrandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>greatgrandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()



