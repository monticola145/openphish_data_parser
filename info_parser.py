import csv
import datetime

import pandas
import requests
from bs4 import BeautifulSoup


def parse_info():
    result = []
    response = requests.get("https://openphish.com/index.html").text
    block = BeautifulSoup(response, "lxml")
    rows = block.find_all("td")

    for row in rows:
        result.append(row.text.strip())

    return [result[x : x + 3] for x in range(0, len(result), 3)]


def get_data():
    data = [parse_info()]
    for attack in data:
        for attack_data in attack:
            with open("data.csv", "r") as read_csv:
                reader = csv.reader(read_csv, delimiter=",", quotechar='"')
                if attack_data in list(reader):  # проверка уникальности
                    attack.remove(attack_data)
                else:
                    with open("data.csv", "a", newline="") as write_csv:
                        writer = csv.writer(write_csv, delimiter=",")
                        writer.writerow(attack_data)


def get_results(time=None):
    with open("data.csv", "r") as read_csv:
        reader = csv.reader(read_csv, delimiter=",", quotechar='"')
        print(
            "Время начала парсинга ==",
            datetime.datetime.strptime(str(time)[0:19], "%Y-%m-%d %H:%M:%S"),
        )
        print(
            "Время окончания парсинга ==",
            datetime.datetime.strptime(
                str(datetime.datetime.now())[0:19], "%Y-%m-%d %H:%M:%S"
            ),
        )
        print(
            "Количество уникальных URL ==",
            len(pandas.read_csv("data.csv").drop_duplicates()),
        )  # дополнительная проверка уникальности
        df = (
            pandas.read_csv("data.csv")
            .sort_values(by=["time", "name", "url"], ascending=False)["name"]
            .value_counts()[:3]
            .to_frame()
        )
        print("Топ 3 наиболее атакуемых брендов:", "\n", df)
