import json
import os
import glob


data = "data"
calendar_folder = os.path.join(data, "calendar")
save_path = os.path.join(data, "events.json")

years = glob.glob(f"./{calendar_folder}/*.json")

ids = {}

for x in years:
    with open(x, 'r', encoding="utf-8") as fp:
        data = json.load(fp)
        for y in data:
            ids[y["_id"]] = y

with open(save_path, "w", encoding="utf-8") as fp:
    json.dump(ids, fp, ensure_ascii=False, indent=2)

print(f"{len(ids)=}")