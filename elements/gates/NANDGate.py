from .ANDGate import ANDGate


class NANDGate(ANDGate):
    def get_probability(self):
        return 1 - super().get_probability()
