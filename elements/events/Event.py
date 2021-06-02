from ..Element import Element


class Event(Element):
    def __init__(self, prob, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.probability = prob
        self.subelement = None

    def add_subelement(self, element):
        self.subelement = element

    def get_probability(self):
        if self.subelement:
            return self.probability * self.subelement.get_probability()
        return self.probability
