import unittest
from textnode import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        nod = TextNode("Am I doing this right?", TextType.TEXT)
        nod2 = TextNode("Am I doing this right?", TextType.TEXT)
        self.assertAlmostEqual(nod, nod2)
    
    def test_neq(self):
        wro = TextNode("We'll see", TextType.BOLD)
        wro2 = TextNode("Hope so", TextType.TEXT)
        self.assertNotEqual(wro, wro2)

    def test_eq3(self):
        edge_case = ("Doubt it", TextType.TEXT)
        edge_case2 = ("but really hope so", TextType.BOLD)
        self.assertNotEqual(edge_case, edge_case2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node) # its this line thats screwing things up. test example given to be used 
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")



if __name__ == "__main__":
    unittest.main()
