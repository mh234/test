# Создаем список books с двумя элементами "*"
books = ["*", "*"]

# Создаем список num с четырьмя элементами "*"
num = ["*", "*", "*", "*"]

# Объединяем списки books и num в новый список overall
overall = books + num

# Расширяем список books, добавляя в него все элементы из списка num
books.extend(num)

# Проходим по каждому элементу в списке books и для каждого элемента печатаем весь список num
for x in books:
    print(num)

# Заменяем элементы списка books с индексами от 1 до 2 включительно на элементы 'astronomiya' и 'vseleniya'
# books[1:3] = ['astronomiya', 'vseleniya']

# Создаем копию списка books и сохраняем ее в переменную key_books
# key_books = books.copy()

# Заменяем элемент списка books с индексом 2 на строку "himiua"
# books[2] = "himiua"

# Переворачиваем порядок элементов в списке books
# books.reverse()

# Сортируем список num
# num.sort()

# Печатаем список num после сортировки
# print(num)

# Удаляем первый встреченный элемент со значением "geometriya" из списка books
# books.remove("geometriya")

# Проходим по каждому элементу в списке books и печатаем каждый элемент
# for x in books:
#     print(x)