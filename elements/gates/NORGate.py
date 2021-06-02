from .ORGate import ORGate


class NORGate(ORGate):
    def get_probability(self):
        return 1 - super().get_probability()
