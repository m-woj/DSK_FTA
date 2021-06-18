from fta import run_fta


if __name__ == "__main__":
    JSON_PATH = "my_sample.json"
    EVENT_ID = "TopEvent"
    TIME = 10

    run_fta(JSON_PATH, EVENT_ID, TIME)
