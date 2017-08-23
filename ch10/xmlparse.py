# our xml parser to demonstrate the state design pattern.

class Node:
    'Each <thing> is a node.'
    def __init__(self, tag_name, parent = None):
        self.tag_name = tag_name
        self.children = []
        self.text = ''
    
    def __str__(self):
        if self.text:
            return self.tag_name + ': ' + self.text
        else:
            return self.tag_name

class Parser:
    def __init__(self, parse_string):
        self.parse_string = parse_string
        self.root = None
        self.current_node = None

        self.state = FirstTag()

    def process(self, remaining_string):
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)

    def start(self):
        self.process(self.parse_string)

class FirstTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        tag_name = remaining_string[i_start_tag + 1:i_end_tag]
        root = Node(tag_name)
        parser.root = parser.current_node = root
        parser.state = ChildNode()
        return remaining_string[i_end_tag + 1:]
