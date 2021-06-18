from ..Element import Element


class Gate(Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subelements = []

    def add_subelement(self, element):
        self.subelements.append(element)
