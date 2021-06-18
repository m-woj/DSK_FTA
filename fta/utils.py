import matplotlib.pyplot as plt
from .FTA import FTA


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
