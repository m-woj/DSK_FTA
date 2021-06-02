from elements import BasicEvent, ANDGate

if __name__ == "__main__":
    top_event = BasicEvent(1, "E1", "egg")
    gate1 = ANDGate("E1", "egg")
    event_2 = BasicEvent(0.2, "E2", "egg")
    event_3 = BasicEvent(0.2, "E3", "egg")
    gate1.add_subelement(event_2)
    gate1.add_subelement(event_3)

    top_event.add_subelement(gate1)
    elements = {top_event.id: top_event,
                gate1.id: gate1}

    print(top_event.get_probability())
