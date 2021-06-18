from .Gate import Gate


class ORGate(Gate):
    def get_probability(self, t):
        prob = 1
        for ele in self.subelements:
            prob *= (1 - ele.get_probability(t))
        return 1 - prob
