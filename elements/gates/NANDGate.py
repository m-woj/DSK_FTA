from .ANDGate import ANDGate


class NANDGate(ANDGate):
    def get_probability(self, t):
        return 1 - super().get_probability(t)
