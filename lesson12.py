file = "result.txt"
a = int(input("Enter number 1 "))
b = int(input("Enter second number "))
c = 0
d = input("+,-,*,/")

with open(file, "w") as file:
    file.write(f"this first {a} second {b}  result: {c}")

if d == "*":
    c = a * b
    print(c)

elif d == "/":
    c = a / b 
    print(c)

elif d == "+":
    c = a + b
    print(c)

elif d == "-":
    c = a - b
    print(c)

else:
    print("Learn math")