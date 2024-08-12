# cost = input("Введите стоимость покупки: ")

# try:
#     cost = int(cost)

#     if cost >= 1000:
#         discount = cost * 0.1
#     elif cost >= 500:
#         discount = cost * 0.05
#     else:
#         discount = 0

#     if discount > 0:
#         print(f"Скидка составляет: {discount} рублей")
#     else:
#         print("Покупка без скидки")

# except ValueError:
#     print("Ошибка ввода. Введите число.")


# word = input("Введите слово: ")
# length = len(word)

# if length > 5:
#     print("Слово длинное")

# print(f"Длина слова {word}: {length} символов")



try:
    price = int(input("Введите цену билета: "))
    
    if price <= 0:
        ticket = "Некорректная цена"
    elif price < 200:
        ticket = "Дешевый билет"
    elif price < 500:
        ticket = "Средний билет"
    else:
        ticket = "Дорогой билет"

    print(f"Тип билета: {ticket}")

except ValueError:
    print("Ошибка ввода. Введите число.")