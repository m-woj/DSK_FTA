from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self, id_code, desc):
        super(ABC, self).__init__()
        self.id = id_code
        self.description = desc

    @abstractmethod
    def add_subelement(self, element):
        pass

    @abstractmethod
    def get_probability(self, t):
        pass

    def get_description(self):
        return self.description
