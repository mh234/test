        # 1
# class book():
#     def __init__(self,title,author,year,isbn):
#         self.mavzu = title
#         self.avtor = author
#         self.sanasi = year
#         self.nazvaniye = isbn

#     def kitob(self):
#         return 2024 - self.sanasi
    

# a = book("baliq","Pushkin",1984,"zolotaya ribka")

# print(a.kitob())


        # 2


# class BancAccount:
#     def __init__(self,account_number,account_holder,balance,a,b): # initialize boshlamoq 
#         self.akk_number = account_number
#         self.akk_holder = account_holder
#         self.balance = balance
#         self.a = a
#         self.b = b
    
#     def getBalance(self,balance):
#         self.balance = balance
#     def minus(self):
#         self.balance -= self.b
    
#     def plyus(self):
#         self.balance += self.a
    
#     def total(self):
#         return self.balance


# c = BancAccount(76,"Mahmudov_Muhammadqodir",500,200,100)
# print(c.total())
     

#                                                     3
# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.grades = []

#     def add_grade(self, grade):
#         self.grades.append(grade)

#     def average_grade(self):
#         if not self.grades:
#             return 0
#         total = sum(self.grades)
#         count = 0
#         for _ in self.grades:
#             count += 1
#         return total / count

#     def display_info(self):
#         average = self.average_grade()
#         print(f"Name: {self.name}")
#         print(f"Student ID: {self.student_id}")
#         print(f"Grades: {self.grades}")
#         print(f"Average Grade: {average:.2f}")

# student = Student("John Doe", "12345")
# student.add_grade(90)
# student.add_grade(85)
# student.add_grade(78)
# student.display_info()
#                         4
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model 
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.make} {self.model}")

# class CarPark:
#     def __init__(self):
#         self.cars = []

#     def add_car(self, car):
#         self.cars.append(car)

#     def remove_car(self, car):
#         self.cars.remove(car)

#     def display_cars(self):
#         for car in self.cars:
#             car.display_info()


# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Honda", "Civic", 2019)
# car_park = CarPark()
# car_park.add_car(car1)
# car_park.add_car(car2)
# car_park.display_cars()

# # 5. Разработка простого игрового приложения

# class Character:
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     def attack(self, other):
#         if self.health > 0:
#             print(f"{self.name} атакует {other.name} на {self.attack_power} урона.")
#             other.take_damage(self.attack_power)
#         else:
#             print(f"{self.name} не может атаковать, потому что он побежден.")

#     def take_damage(self, damage):
#         self.health -= damage
#         print(f"{self.name} получает {damage} урона и теперь у него {self.health} здоровья.")
#         if self.health <= 0:
#             print(f"{self.name} был побежден.")

# class Warrior(Character):
#     def __init__(self, name, health, attack_power, shield):
#         super().__init__(name, health, attack_power)
#         self.shield = shield

#     def attack(self, other):
#         print(f"{self.name} использует мощный удар!")
#         super().attack(other)

# class Mage(Character):
#     def __init__(self, name, health, attack_power, mana):
#         super().__init__(name, health, attack_power)
#         self.mana = mana

#     def attack(self, other):
#         if self.mana > 0:
#             print(f"{self.name} произносит заклинание!")
#             self.mana -= 1
#             super().attack(other)
#         else:
#             print(f"{self.name} не может атаковать, потому что у него закончилась мана.")

# warrior = Warrior(name="Воин", health=100, attack_power=15, shield=10)
# mage = Mage(name="Маг", health=80, attack_power=20, mana=5)

# warrior.attack(mage)
# mage.attack(warrior)
# 6
# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def area(self):
#         raise NotImplementedError("Подклассы должны реализовать этот метод")

# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius

#     def area(self):
#         return 3.14159 * (self.radius ** 2)

# class Rectangle(Shape):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Triangle(Shape):
#     def __init__(self, color, base, height):
#         super().__init__(color)
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# circle = Circle(color="red", radius=5)
# rectangle = Rectangle(color="blue", width=4, height=6)
# triangle = Triangle(color="green", base=3, height=4)

# print(f"Площадь круга: {circle.area()}")
# print(f"Площадь прямоугольника: {rectangle.area()}")
# print(f"Площадь треугольника: {triangle.area()}")
# 7
class Task:
    def __init__(self, title, description, status='incomplete'):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Task(title={self.title}, description={self.description}, status={self.status})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Добавлена задача: {task}")

    def change_status(self, title, new_status):
        for task in self.tasks:
            if task.title == title:
                task.status = new_status
                print(f"Статус задачи '{title}' изменен на {new_status}")
                break
        else:
            print(f"Задача с названием '{title}' не найдена")

    def show_tasks(self):
        for task in self.tasks:
            print(task)

task1 = Task(title="Задача 1", description="Описание задачи 1")
task2 = Task(title="Задача 2", description="Описание задачи 2", status="complete")

manager = TaskManager()
manager.add_task(task1)
manager.add_task(task2)

manager.change_status("Задача 1", "complete")
manager.show_tasks()
