import os

def sapling():
    print("Выкапываем яму")
    if shift == "НЕТ":
        print("Петрович кладет саженец")
    print("Серега закапывает яму")
    print("Перекур")


print("САЖАЕМ САЖЕНЦЫ\n\n")
while (True):
    shift = input("Петрович опять болеет?\n").upper()
    if shift == "НЕТ" or shift == "ДА":
        break

sapling()

while (True):
    answer = input("Рабочая смена закончена?").upper()
    if answer == "ДА":
        break
    elif answer == "НЕТ":
        sapling()
os.system("pause")