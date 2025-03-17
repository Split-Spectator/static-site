class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        if self.tag:
            html = f"<{self.tag}"
            if self.props:
                for prop, value in self.props.items():
                    html += f' {prop}="{value}"'
            html += ">"
            if self.value:  
                html += self.value  
            if self.children:
                for child in self.children:
                    html += child.to_html()
            html += f"</{self.tag}>"
            return html
        else:
            html = ""
            if self.children:
                for child in self.children:
                    html += child.to_html()
            return html

    def props_to_HTML(self):
        if not self.props:
            return ""
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html

    def __repr__(self):
         return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        """Compares two HTMLNode objects for equality based on their attributes."""
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("value cannot be None")
        if self.tag is None:
            return str(self.value)
        if self.children is not None:
            raise Exception("LeafNode is Barren")
    
        props_html = self.props_to_HTML()  # Use self instead of super()
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
         super().__init__(tag, None, children, props)
           
    def to_html(self):
        if self.tag is None:
            raise ValueError("needs tag")
        if self.children is None:
            raise ValueError("You really need a child. have you considered adoption?")
        
        else:
            children_string = ""
            if not self.children:
                children_string += LeafNode(self.tag, self.value, self.props).to_html()
            else:
                for child in self.children:
                    children_string += child.to_html()
            return f"<{self.tag}>{children_string}</{self.tag}>"
    
    def __repr__(self):
        return f'{self.tag}, {self.children}, {self.props}'
