import os

euro_exchange = 69.33
print("Текущий курс RUR/EUR равен:", euro_exchange)

trip_budget = int(input("Общий бюджет поездки в рублях:"))
trip_budget_eur = round(trip_budget / euro_exchange, 2)
print("Общий бюджет поездки в евро:", trip_budget_eur)

flight_cost = int(input("Стоимость перелета в рублях:"))
trip_lenght = int(input("Дней проживания:"))
daily_accommodation = int(input("Стоимость суток проживания в рублях:"))
daily_accommodation_eur = round(daily_accommodation / euro_exchange, 2)
print("Стоимость суток проживания в евро:", daily_accommodation_eur)

accommodation = (daily_accommodation * trip_lenght)
accommodation_eur = round(daily_accommodation_eur * trip_lenght, 2)
print("Всего за проживание в рублях:", accommodation)
print("Всего за проживание в евро:", accommodation_eur)

total_budget = flight_cost + accommodation
total_budget_eur = round(flight_cost / euro_exchange + accommodation_eur, 2)

if total_budget <= trip_budget:
    print("Остаток бюджета после оплаты перелета и проживания:", trip_budget - total_budget, "рублей или",
          trip_budget_eur - total_budget_eur, "евро.")
else:
    print("Запланированный размер бюджета поездки превышен!")

personal_expenses = []
value = 0

while True:
    value = input("Введите сумму личных расходов в евро. Для завершения списка введите Q:")
    if value != "q":
        value = int(value)
        personal_expenses.append(value)
    elif value == "q":
        break

print("Список личных расходов за поездку:", personal_expenses)
personal_expenses = sum(personal_expenses)
print("Общая сумма личных раходов в евро:", personal_expenses)
personal_expenses_rur = personal_expenses * euro_exchange
print("Общая сумма личных раходов в рублях:", personal_expenses_rur)

if (total_budget + personal_expenses_rur) <= (trip_budget - total_budget - personal_expenses_rur):
    print("Остаток бюджета после оплаты личных расходов:", trip_budget - total_budget - personal_expenses_rur,
          "рублей или", trip_budget_eur - total_budget_eur - personal_expenses, "евро")
else:
    print("Запланированный размер бюджета поездки превышен!")
os.system("pause")