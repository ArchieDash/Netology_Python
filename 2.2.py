import chardet
from collections import Counter


def decoder(file_name):
    with open(file_name, "rb") as f:
        data = f.read()
        decode = chardet.detect(data)
        return data.decode(decode["encoding"])


def report(file_name):
    file = decoder(file_name)
    results = []
    for word in file.split(" "):
        if len(word) >= 6:
            results.append(word)
        answer = Counter(results).most_common(10)
    for i in answer:
        print("Слово:", i[0], "\nКоличество упоминаний в тексте: ", i[1])


def main():
    while True:
        console = input("Choose a file to open:\n1-France\n2-Africa\n3-Cyprus\n4-Italy\nQ-for quit")
        if console == "1":
            report("newsfr.txt")
        elif console == "2":
            report("newsafr.txt")
        elif console == "3":
            report("newscy.txt")
        elif console == "4":
            report("newsit.txt")
        elif console.lower() == "q":
            break


main()
