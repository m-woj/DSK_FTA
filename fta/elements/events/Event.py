import math

from ..Element import Element


class Event(Element):
    def __init__(self, failure_rate, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.failure_rate = failure_rate
        self.subelement = None

    def add_subelement(self, element):
        self.subelement = element

    def get_probability(self, t):
        if self.subelement:
            return self._own_probability(self.failure_rate, t) * self.subelement.get_probability(t)
        return self._own_probability(self.failure_rate, t)

    @staticmethod
    def _own_probability(failure_rate, t):
        return 1 - math.exp(-failure_rate * t)
