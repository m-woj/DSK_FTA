import matplotlib.pyplot as plt
from .FTA import FTA


def _load_fta(json_path):
    try:
        return FTA(json_path)
    except BaseException as e:
        print(f"Nie udało się załadować pliku \"{json_path}\".\n{e}")


def draw_fta(json_path, event_id, time):
    fta = _load_fta(json_path)
    if not fta:
        return

    event = fta.map[event_id]
    ts = [i * 0.001 for i in range(time*1000)]
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
