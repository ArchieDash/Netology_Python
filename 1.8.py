import os
from collections import Counter


def report(file_name, type):
    with open(file_name, encoding=type) as file:
        results = []
        for line in file:
            for word in line.split(" "):
                if len(word) >= 6:
                    results.append(word)
                answer = Counter(results).most_common(10)
        for i in answer:
            print("Слово:", i[0], "\nКоличество упоминаний в тексте: ", i[1])


while True:
    console = input("Choose a file to open:\n1-France\n2-Africa\n3-Cyprus\n4-Italy\nQ-for quit")
    if console == "1":
        report("newsfr.txt", None)
    elif console == "2":
        report("newsafr.txt", "utf-8")
    elif console == "3":
        report("newscy.txt", None)
    elif console == "4":
        report("newsit.txt", None)
    elif console.lower() == "q":
        break
os.system("pause")
