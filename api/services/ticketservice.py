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
                    "_id": {"show_id": "$metadata.show_id"},
                    "time": {"$last": "$timestamp"},
                    "sold": {"$last": "$sold"}
                }
            },
            {
                "$sort": {"metadata.show_id": 1}
            },
            {
                "$project": {
                    "show": "$_id.show_id",
                    "sold": "$sold",
                    "time": "$time"
                }
            }
        ]
        result = self.tickets.aggregate(pipeline)

        last_sold = []
        for show in result:
            sold = show["sold"]
            show_id = show["show"]
            timestamp = show["time"].isoformat()
            last_sold.append(dict(sold=sold, show_id=show_id, timestamp=timestamp))
        last_sold.sort(key=lambda k: k.get("show_id"))
        return last_sold

    def get_daily_sold(self):
        date = datetime.datetime(year=2023, month=9, day=10)
        upper_date = date + datetime.timedelta(days=2)
        pipeline = [
            {
                "$addFields": {
                    "createdDate": {"$dateToString": {"format": "%Y-%m-%d", "date": "$timestamp"}}
                }
            },

            {
                "$group": {
                    "_id": {
                        "time": "$createdDate",
                        "show_id": "$metadata.show_id",
                    },
                    "minimum": {"$min": "$sold"},
                    "maximum": {"$max": "$sold"},
                },
            },
            {
                "$addFields": {
                    "show": "$_id.show_id",
                    "sold": {"$subtract": ["$maximum", "$minimum"]},
                    "minimum": "$minimum",
                    "maximum": "$maximum",
                    "time": "$_id.time"

                }
            },
            {
                "$group": {
                    "_id": "$_id.time",
                    "sold": {"$sum": "$maximum"}
                },
            },
            {
                "$sort": {"_id": -1}
            }
            ]

        result = self.tickets.aggregate(pipeline)
        last_sold = []
        for show in result:
            sold = show["sold"]
            date = show["_id"]
            last_sold.append(dict(total=sold, date=date))
        return last_sold
