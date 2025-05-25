class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.props = props
        self.children = children

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        html_props = ''
        if self.props is None:
            return None
        for name, value in self.props.items():
            html_props += f' {name}="{value}"'
        return html_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
