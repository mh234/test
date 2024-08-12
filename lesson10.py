try:
    file_text = input("write your own essay")
    if file_text:
        with open("example.txt", 'w') as file:
            content = file.write(file.text)
            if (content):
                print(f"You file is created now")
            else:
                print("Something is gona wrong")
    else:
        print("Write one more time")
        file = str(input("Write your own essay"))
except FileNotFoundError:
    print("Sorry man you file is not readable")
except IOError:
    print("Error: blablabla")
finally:
    print("This is finally tags")

try:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter second number: "))
    result = num1 / num2
    print(f" {num1} / {num2} = {result}")
except ZeroDivisionError:
    print("learn math")

try:
    with open("File") as file:
        print("We wound file")
except FileNotFoundError:
    print("Somthing went wrong")    


def divide_100():
    try:
        user_input = input("Введите целое число: ")
        number = int(user_input)
        result = 100 / number
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль.")
    except ValueError:
        print("Ошибка: Введено нечисловое значение.")
    else:
        print(f"Результат деления: {result}")

divide_100()

def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
            print("Данные успешно записаны в файл.")
    except IOError:
        print(f"Ошибка: Не удалось открыть файл '{filename}' для записи.")

filename = input("Введите имя файла для записи: ")
data = input("Введите данные для записи: ")
write_to_file(filename, data)



def convert_to_integer():
    user_input = input("Введите строку для преобразования в целое число: ")
    try:
        number = int(user_input)
    except ValueError:
        print("Ошибка: Введена нечисловая строка.")
    else:
        print(f"Преобразованное целое число: {number}")
    finally:
        print("Операция завершена.")

convert_to_integer()
