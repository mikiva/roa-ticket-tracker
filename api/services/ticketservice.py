import datetime
from collections import defaultdict

from pymongo import MongoClient


class TicketService:
    def __init__(self, db: MongoClient):
        self._db = db
        self.tickets = db["roa"]["tickets"]

    def close_db(self):
        try:
            self._db.close()
        except:
            ...

    def get_today_sold(self):
        now = datetime.datetime.now().date()
        pipeline = [
            {
                "$addFields": {
                    "createdDate": {"$dateToString": {"format": "%Y-%m-%d", "date": "$timestamp"}}
                }
            },
            {
                "$match": {
                    "createdDate": str(now)
                }
            },
            {
                "$project": {
                    "show_id": "$metadata.show_id",
                    "sold": "$sold",

                    "timestamp": "$timestamp"
                }
            },
            {
                "$sort": {"timestamp": 1}
            },
        ]

        result = self.tickets.aggregate(pipeline)
        shows = defaultdict(list)
        for show in result:
            show_id = show["show_id"]
            sold = show["sold"]
            date = show["timestamp"].isoformat()
            shows[show_id].append(dict(sold=sold, date=date))
        shows_total = defaultdict(dict)
        for k, v in shows.items():
            first = v[0].get("sold")
            last = v[-1].get("sold")
            total = last - first
            shows_total[k] = {
                "current": last,
                "today": total,
            }

        return dict(shows_total)

    def get_latest_sold(self):
        pipeline = [
            {
                "$group": {
                    "_id": {"show": "$metadata.show_id", "sold": "$sold"},
                    "maxT":
                        {
                            "$max": "$timestamp"
                        }
                }
            },
            {
                "$project": {
                    "sold": "$_id.sold",
                    "show": "$_id.show",
                    "maxT": "$maxT"
                }
            }
        ]
        result = self.tickets.aggregate(pipeline)

        last_sold = []
        for show in result:
            sold = show["sold"]
            show_id = show["show"]
            timestamp = show["maxT"].isoformat()
            last_sold.append(dict(sold=sold, show_id=show_id, timestamp=timestamp))
        last_sold.sort(key=lambda k: k.get("show_id"))
        return last_sold
