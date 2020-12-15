def sapling(shift):
    print("Выкапываем яму")
    if shift == "НЕТ":
        print("Петрович кладет саженец")
    print("Серега закапывает яму")
    print("Перекур")


def main():    
    print("САЖАЕМ САЖЕНЦЫ\n\n")
    while (True):
        shift = input("Петрович опять болеет?\n").upper()
        if shift == "НЕТ" or shift == "ДА":
          break
    sapling(shift)
    while (True):
        answer = input("Рабочая смена закончена?").upper()
        if answer == "ДА":
            break
        elif answer == "НЕТ":
            sapling(shift)


if __name__ == "__main__":
    main()
