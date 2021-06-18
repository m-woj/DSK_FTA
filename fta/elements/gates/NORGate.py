from .ORGate import ORGate


class NORGate(ORGate):
    def get_probability(self, t):
        return 1 - super().get_probability(t)
