import json
from collections import defaultdict

from compare_per_show import compare


formatted = defaultdict(list)

#dates = set([s.get("date") for s in compare])
#show_ids = set([s.get("show_id") for s in compare])

#print(sorted(list(dates)))
#print(sorted(list(show_ids)))

for item in compare:
    d = item.get("date")
    i = item.get("show_id")
    s = item.get("sold")
    formatted[d].append(dict(show=i, sold=s))

with open("temp.json","w") as t:
    t.write(json.dumps(formatted))


#print(formatted)