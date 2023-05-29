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
            }
        ]
        result = self.tickets.aggregate(pipeline)

        last_sold =[]
        for show in result:
            s = show["_id"]
            last_sold.append(s)
        last_sold.sort(key=lambda k: k.get("show"))
        return last_sold
