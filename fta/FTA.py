import json
from fta.elements import *
from .names import *


class FTA:
    def __init__(self, path_to_json):
        with open(path_to_json) as json_file:
            fta_dict = json.load(json_file)
        self.map = {}
        self.tree = self.create_tree(fta_dict)

    def create_tree(self, fta_dict):
        element = self.make_element(fta_dict)
        if element.id:
            self.map[element.id] = element

        for sub_element_dict in fta_dict[SUBELEMENTS]:
            sub_element = self.create_tree(sub_element_dict)
            element.add_subelement(sub_element)
        return element

    def make_element(self, properties):
        desc = self._try_get(properties, DESCRIPTION)
        ele_id = self._try_get(properties, ID)
        type = properties[TYPE]

        #Events
        if type == BASIC_EVENT:
            failure_rate = properties[FAILURE_RATE]
            element = BasicEvent(failure_rate, ele_id, desc)
        elif type == EXTERNAL_EVENT:
            failure_rate = properties[FAILURE_RATE]
            element = ExternalEvent(failure_rate, ele_id, desc)
        #Gates
        elif type == AND_GATE:
            element = ANDGate(ele_id, desc)
        elif type == OR_GATE:
            element = ORGate(ele_id, desc)
        elif type == NAND_GATE:
            element = NANDGate(ele_id, desc)
        elif type == NOR_GATE:
            element = NORGate(ele_id, desc)
        elif type == KN_GATE:
            k = properties[K]
            element = KNGate(k, ele_id, desc)
        else:
            raise Exception(f"Nieznany typ elementu FTA: {type}")

        return element

    @staticmethod
    def _try_get(properties, property_name):
        try:
            return properties[property_name]
        except KeyError:
            return
