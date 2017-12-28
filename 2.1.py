from itertools import islice


def parser():
    with open("menu.txt", "r") as file:
        cook_book = dict()
        for line in file:
            course_name = line.strip()
            n = int(file.readline())
            items = islice(file, n)
            course = list()
            for line in items:
                ingredient = dict(zip(["ingredient", "quantity", "measure"], line.strip().split(" | ")))
                ingredient["quantity"] = int(ingredient["quantity"])
                course.append(ingredient)
            cook_book[course_name] = course
            file.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient'] not in shop_list:
                shop_list[new_shop_list_item['ingredient']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient']]['quantity'] += int(new_shop_list_item['quantity'])
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient'], shop_list_item['quantity'], shop_list_item['measure']))


def main():
    cook_book = parser()
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    print(dishes)
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


main()
