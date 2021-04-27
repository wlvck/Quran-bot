import json

with open("D:\Pycharm projects\/aio_names_bot\data\/books_url.json", "r", encoding="utf8") as file:
    read_file = json.load(file)
a = 'Тафсир Куртуби. Введение, сура 1, сура 2 (аяты 1–20)'
for i in read_file.values():
    for key in i.items():
        if a in key:
            print(True)