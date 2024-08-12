
    

# class V():
#     def __init__(self, a, b , h):
#         self.boyi = a
#         self.eni = b
#         self.balandligi = h

#     def volume(self):
#         return self.boyi * self.balandligi * self.eni
    
# shakl = V(7, 9, 12)
# print(shakl.volume())


try:
    a = 100
    b = int(input("Enter second number"))
    result = a / b
    print(f" {a} / {b} = {result}")
except ValueError:
    print("Learn math")
