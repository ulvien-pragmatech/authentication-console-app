import json
with open("newDB.json") as json_file:  # jsondan goturur
    db = json.load(json_file)

# json_file = open("newDB.json) demekdir
# json.load nagarir => ona argument kimi daxil olunan fayla girir (burada json_file), ve ordaki listi db'e beraber edir
