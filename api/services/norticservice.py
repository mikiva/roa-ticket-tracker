import json

class NorticService:

    def __init__(self):
        self.url = "https://www.nortic.se/api/json/event/47696"

    def get_event(self):
        with open("shows.json") as file:
            j = json.load(file)
            return j["events"][0]

    def get_all_shows_info(self):
        event = self.get_event()
        return event.get("shows")