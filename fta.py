from fta import draw_fta


if __name__ == "__main__":
    JSON_PATH = "samples/fta.json"
    EVENT_ID = "TopEvent"
    TIME = 10

    draw_fta(JSON_PATH, EVENT_ID, TIME)
