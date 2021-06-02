import json
from elements import *


class FTA:
    def __init__(self, path_to_json):
        fta_dict = json.load(path_to_json)
        self.tree = self.create_tree(fta_dict)

    def create_tree(self, fta_dict):
        fta_dict = {}
        top = fta_dict.keys()[0]

    def make_element(self, type, properties):
        desc = properties["desc"]
        ele_id = properties["id"]
        if type == "BasicEvent":
            prob = properties["prop"]["probability"]
            element = BasicEvent(prob, ele_id, desc)
        elif type == "ANDGate":
            element = ANDGate(ele_id, desc)
        else:
            raise Exception(f"Nieznany typ elementu FTA: {type}")

        return element


if __name__ == "__main__":
    e0 = {"BasicEvent": {"id": "A1",
                         "desc": "egg",
                         "prop": {"probability": 0.3,
                                  },
                         "subelements": ""}
             }

    g1 = {"ANDGate": {"id": "G1",
                         "desc": "egg",
                         "prop": "",
                         "subelements": ""}
             }

    e1 = {"BasicEvent": {"id": "A1",
                         "desc": "egg",
                         "prop": "",
                         "subelements": g1}
             }

    # top_event = BasicEvent(1, "Top Event", "egg")
    # gate1 = KNGate(0, "E1", "egg")
    #
    # event_2 = BasicEvent(0.5, "E2", "egg")
    # event_3 = BasicEvent(0.5, "E3", "egg")
    # event_4 = BasicEvent(0.5, "E3", "egg")
    #
    # top_event.add_subelement(gate1)
    # gate1.add_subelement(event_2)
    # gate1.add_subelement(event_3)
    # gate1.add_subelement(event_4)
    #
    # print(top_event.get_probability()/0.125)
