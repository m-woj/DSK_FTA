from .Gate import Gate


class ANDGate(Gate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_probability(self):
        prob = 1
        for ele in self.subelements:
            prob *= ele.get_probability()
        return prob
