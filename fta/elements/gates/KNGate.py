import copy
from itertools import combinations
from .Gate import Gate


class KNGate(Gate):
    def __init__(self, k, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.k = k

    def get_probability(self, t):
        n = len(self.subelements)
        ele_prob = []
        for ele in self.subelements:
            ele_prob.append(ele.get_probability(t))

        prob = 0
        for k in range(self.k, n + 1):
            prob += self._calc_prob(n, k, ele_prob)
        return prob

    def _calc_prob(self, n, k, elements_prob):
        fails_num = n - k
        fails = combinations(elements_prob, fails_num)
        probability = 0

        for fails_case_prob in fails:
            good_cases = self._get_good_cases(elements_prob, fails_case_prob)
            probability += self._calc_case(good_cases, fails_case_prob)
        return probability

    @staticmethod
    def _get_good_cases(elements, fails):
        good_elements = copy.deepcopy(elements)
        for fail in fails:
            good_elements.remove(fail)
        return good_elements

    @staticmethod
    def _calc_case(well, fails):
        w_sum = 1
        for w in well:
            w_sum *= w

        f_sum = 1
        for f in fails:
            f_sum *= (1 - f)

        return w_sum * f_sum
