class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.props = props
        self.children = children

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        html_props = ''
        if self.props is None:
            return ''
        for name, value in self.props.items():
            html_props += f' {name}="{value}"'
        return html_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self,tag, value, props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children,props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('invalid HTML: no tag')
        if self.children is None:
            raise ValueError('invalid HTML: no children')
        else:
            if self.children is None:
                return self.to_html()
            else:
                children = ''
                for child in self.children:
                    children += child.to_html()
                return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
