from .Event import Event


class BasicEvent(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
