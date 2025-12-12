import glob
import json

from tqdm import tqdm

files = glob.glob("data/events/*.json")

event_types = set()
for x in tqdm(files, total=len(files)):
    with open(x, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        event_types.add(data["premiere"])
        for y in data["productions"]:
            event_types.add(y["premiere"])

print(event_types)

foo = {
    "Neueinstudierung": "",
    "Premiere": "",
    "Erstaufführung": "",
    "Neuinszenierung": "",
    "Uraufführung": "",
}
