import json
import matplotlib.pyplot as plt
from elements import *


class FTA:
    def __init__(self, path_to_json):
        with open(path_to_json) as json_file:
            fta_dict = json.load(json_file)
        self.map = {}
        self.tree = self.create_tree(fta_dict)

    def create_tree(self, fta_dict):
        ele_type, ele_prop = list(fta_dict.items())[0]
        element = self.make_element(ele_type, ele_prop)
        self.map[ele_prop["id"]] = element
        for sub_element_dict in ele_prop["subelements"]:
            sub_element = self.create_tree(sub_element_dict)
            element.add_subelement(sub_element)
        return element

    def make_element(self, type, properties):
        desc = properties["desc"]
        ele_id = properties["id"]
        #Events
        if type == "BasicEvent":
            failure_rate = properties["prop"]["failure_rate"]
            element = BasicEvent(failure_rate, ele_id, desc)
        elif type == "ExternalEvent":
            failure_rate = properties["prop"]["failure_rate"]
            element = ExternalEvent(failure_rate, ele_id, desc)
        #Gates
        elif type == "ANDGate":
            element = ANDGate(ele_id, desc)
        elif type == "ORGate":
            element = ORGate(ele_id, desc)
        elif type == "NANDGate":
            element = NANDGate(ele_id, desc)
        elif type == "NORGate":
            element = NORGate(ele_id, desc)
        elif type == "KNGate":
            k = properties["prop"]["k"]
            element = KNGate(k, ele_id, desc)
        else:
            raise Exception(f"Nieznany typ elementu FTA: {type}")

        return element


def run_fta(json_path, event_id, time):
    try:
        fta = FTA(json_path)
    except BaseException:
        print("Nie udało się załadować pliku JSON.")
        return

    event = fta.map[event_id]

    ts = [i / 1000 for i in range(time*1000)]
    ps = [event.get_probability(t) for t in ts]

    plt.plot(ts, ps)
    plt.title(f"Prawdopodobieństwo zaistnienia zdarzenia: {event_id}")
    plt.grid()
    plt.xlabel("Czas")
    plt.ylabel("Prawdopodobieństwo")
    plt.xlim(0, time)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()
