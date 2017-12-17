documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def doc_list():
    print("\nDATABASE OVERVIEW:\n")
    for document in documents:
        print(document["type"], document["number"], document["name"])


def holder_search():
    doc_number = input("Enter required doc's number:")
    for document in documents:
        if doc_number == document["number"]:
            print("Document holder:", document["name"])


def folder_by_number_search():
    doc_number = input("Enter required doc's number:")
    for folder_number, folder_docs in directories.items():
        if doc_number in folder_docs:
            print("Current folder's number to store:", folder_number)


def add_doc():
    new_doc = dict.fromkeys(["type", "number", "name"])
    doc_type = input("Type:")
    new_doc["type"] = doc_type
    doc_number = input("Number:")
    new_doc["number"] = doc_number
    holder = input("Doc's holder name:")
    new_doc["name"] = holder
    documents.append(new_doc)
    folder_number = input("Folder to store:")
    for folder, docs in directories.items():
        if folder == folder_number:
            docs.append(doc_number)


def move_doc():
    doc_number = input("Enter required doc's number:")
    folder_number = input("Enter folder's number where to move:")
    for folder, docs in directories.items():
        if doc_number in docs:
            docs.remove(doc_number)
        if folder_number == folder:
            docs.append(doc_number)


def doc_del():
    doc_number = input("Enter required doc's number:")
    for docs in directories.values():
        if doc_number in docs:
            docs.remove(doc_number)
    for document in documents:
        if doc_number == document["number"]:
            documents.remove(document)


def add_folder():
    folder_to_add = input("Enter the number of folder to add:")
    directories[folder_to_add] = []


def main():
    print(r"Welcome to <PROTO-Tech> Tyrel Corp. Data Base System")
    while True:
        console = input(
            "\n\nP - search document holder by doc's number\nL - browse documents list\nF - display folder number by doc's number\nA - add new document\nD - delete existing document\nM - move document between folders\nAS - add new folder\nQ - quit\n").upper()
        if console == ("L"):
            doc_list()
        elif console == "P":
            holder_search()
        elif console == "F":
            folder_by_number_search()
        elif console == "A":
            add_doc()
        elif console == "M":
            move_doc()
        elif console == "D":
            doc_del()
        elif console == "AS":
            add_folder()
        elif console == "Q":
            break
        else:
            print("Unknown command")


main()