import os
import chardet


def decoder(directory, file_name):
    with open(os.path.join(directory, file_name), "rb") as f:
        data = f.read()
        decode = chardet.detect(data)
        return data.decode(decode["encoding"])


def main():
    directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Migrations")
    files = os.listdir(directory)
    database = set()
    for file in files:
        if file.endswith(".sql"):
            database.add(file)
    while True:
        search = input("SEARCH:\nQ for exit")
        match = set()
        if search.lower() == "q":
            break
        for file in database:
            data = decoder(directory, file)
            if search in data:
                match.add(file)
        if not match:
            print("No match at any file")
            continue
        else:
            database = match
        for file in database:
            print(file)
        print(f"TOTAL FILES: {len(database)}")


main()
