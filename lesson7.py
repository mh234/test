# class Parents:
#     def ___init___(self,make,things):
#         self.__make = make
#         self.__things = things

#     def text(self):
#         return f'{self.__make},   {self.__things}'
# Parents = Parents("stul","stol")
# print(Parents.text())

class Person:
    def skin_color(self):
        return "color"
    

class black(Person):
    def skin_color(self):
        return "black"

class White(Person):
    def skin_color(self):
        return "White"
    
class red(Person):
    def skin_color(self):
        return "Red"
    
Human = [black(),White(),red()]
for x in Human:
    print(x.skin_color())