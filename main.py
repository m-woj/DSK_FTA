from FTA import FTA


def gen_json():
    e0 = {"BasicEvent": {"id": "A1",
                         "desc": "egg",
                         "prop": {
                             "probability": 0.3,
                                  },
                         "subelements": []}
             }

    g1 = {"ANDGate": {"id": "G1",
                         "desc": "egg",
                         "prop": {},
                         "subelements": [e0]}
             }

    e1 = {"BasicEvent": {"id": "A2",
                         "desc": "egg",
                         "prop": {
                             "probability": 0.3,
                         },
                         "subelements": [g1]}
             }

    with open("sample.json", "w") as outfile:
        json.dump(e1, outfile, indent=2)


if __name__ == "__main__":
    # gen_json()
    fta = FTA("my_sample.json")
    top_event = fta.map["TopEvent"]
    print(top_event.get_probability())
    print(top_event.get_description())

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
