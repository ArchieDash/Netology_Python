import chardet
import json
from xml.etree import ElementTree as ET
from collections import Counter


def decoder(file_name):
    with open(file_name, "rb") as f:
        decode = chardet.detect(f.read())
        return decode["encoding"]


def report_txt(file_name):
    with open(file_name, "r", encoding=decoder(file_name)) as file:
        results = list()
        for line in file:
            for word in line.split(" "):
                if len(word) >= 6:
                    results.append(word)
                answer = Counter(results).most_common(10)
        for i in answer:
            print("Слово:", i[0], "\nКоличество упоминаний в тексте: ", i[1])


def report_json(file_name):
    with open(file_name, "r", encoding=decoder(file_name)) as file:
        data = json.loads(file.read())
        results = list()
        for item in data["rss"]["channel"]["items"]:
            for word in item["description"].split(" "):
                if len(word) >= 6:
                    results.append(word)
                    answer = Counter(results).most_common(10)
        for i in answer:
            print("Слово:", i[0], "\nКоличество упоминаний в тексте: ", i[1])


def report_xml(file_name):
    parser = ET.XMLParser(encoding=decoder(file_name))
    tree = ET.parse(file_name, parser=parser)
    results = list()
    news = tree.findall("channel/item/description")
    for item in news:
        data = item.text
        for word in data.split(" "):
            if len(word) >= 6:
                results.append(word)
                answer = Counter(results).most_common(10)
    for i in answer:
        print("Слово:", i[0], "\nКоличество упоминаний в тексте: ", i[1])


def main():
    while True:
        mode = input("Choose mode:\n1 - TXT\n2 - JSON\n3 - XML\nQ-for quit")
        modes = {"1": ".txt", "2": ".json", "3": ".xml"}
        file = input("Choose a file to open:\n1-France\n2-Africa\n3-Cyprus\n4-Italy")
        files = {"1":"newsfr", "2":"newsafr", "3":"newscy", "4":"newsit"}
        file_name = files[file]+modes[mode]
        if mode == "1":
            report_txt(file_name)
        elif mode == "2":
            report_json(file_name)
        elif mode == "3":
            report_xml(file_name)
        elif mode.lower() == "q":
            break


main()
