from .Gate import Gate


class ORGate(Gate):
    def get_probability(self):
        prob = 1
        for ele in self.subelements:
            prob *= (1 - ele.get_probability())
        return 1 - prob
