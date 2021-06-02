from copy import copy
from .Gate import Gate


class KNGate(Gate):
    def __init__(self, k, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.k = k

    def _calc_prob(self, elements, i):
        prob = 0
        if i <= self.k:
            for ele in elements:
                subelements = copy(elements)
                subelements.remove(ele)
                i += 1
                prob += (1 - ele.get_probability()) * self._calc_prob(subelements, i)
        else:
            prob = 1
            for ele in elements:
                prob *= ele.get_probability()

        return prob

    def get_probability(self):
        prob = 0
        for i in range(self.k, len(self.subelements) + 1):
            prob += self._calc_prob(self.subelements, i)
        return prob
