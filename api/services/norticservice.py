from requests import get

class NorticService:

    def __init__(self):
        self.url = "https://www.nortic.se/api/json/event/47696"

    def get_event(self):
        resp = get(self.url)
        j = resp.json()
        return j["events"][0]

    def get_all_shows_info(self):
        event = self.get_event()
        return event.get("shows")