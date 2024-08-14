import math
# A = int(input("Give me number"))
# if A%3==0 and A%10 == 0:
#     print("Correct")
# else:
#     print("Learn math")
# A = int(input("Give me number "))
# if 999>A<10000 and A!=4999:
#     print("Correct")
# else:
#     print("Learn math")
# A = int(input("Give me number"))
# if A%3==0 and A%4!=0:
#     print("Correct")
# else:
#     print("Learn math")
# y = int(input('y sonini kirgizing:\n>>>'))
# f = int(input('f sonini kirgizing:i\n>>>'))
# A = math.e ** (2 * y) + math.sin(f)
# B = math.log10(3.8 * y + f)
# G = A / B
# print(round(G, 2))
W = int(input('W sonini kirgizing:'))
Y = int(input('Y sonini kirgizing:'))
A = 9.33 * (W ** 3) + math.sqrt(W)
B = math.log10(Y + 3.5) + math.sqrt(Y)
G = A / B
print(G)