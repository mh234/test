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

# W = int(input('W sonini kirgizing:'))
# Y = int(input('Y sonini kirgizing:'))
#  A = 9.33 * (W ** 3) + math.sqrt(W)
# B = math.log10(Y + 3.5) + math.sqrt(Y)
# G = A / B
# print(G)

# a = int(input("Enter number a:"))
# t = int(input("Enter number t:"))
# y = int(input("Enter number y:"))

# A = 7.8 * a ** 2 + 3.52 * t
# B = math.log10(a + 2 * y) + math.e ** y

# D = A / B
# print(D)


# t = int(input("Enter number t:"))
# r = int(input("Enter number r:"))
# y = int(input("Enter number y:"))

# A = 4 * t ** 3 + math.log10(r)
# B = math.e ** (y + r) + 7.2 * math.sin(r)

# W = A / B

# print(W)

# y = int(input("Enter number y:"))
# n =  int(input("Enter number n:"))

# A = y ** 2 - 0.8 *y + math.sqrt(y)
# B = 23.1 * n ** 2 + math.cos * n 

# H = A / B
# print(H)


# y = int(input("Enter number y:"))
# k = int(input("Enter number k:"))


# A = math.sqrt(pow(math.sin(y), 2)+ 6.835)
# B = math.log10(y + k) + 3 * (y ** 2)

# R = A / B
# print(R)

# y = int(input("Enter number y:"))
# q = int(input("Enter number q:"))

# A = math.log10(0.7 * y + 2 * q)
# B = math.sqrt(3 * y ** 2 + 0.5 * y + 4)

# E = A / B 
# print(E)


# y = int(input("Enter number y:"))
# t = int(input("Enter number t:"))
# l = int(input("Enter number l:"))

# A = 2 * t ** 2 + 3 * l + 7.2
# B = math.log10 * y + math.e ** 2 * l
# K = A / B
# print(K)

# # 1. Ikki son kvadratlari summasi va summasining kvadrati
# def problem_1():
#     x = int(input("Birinci sonni kiriting: "))
#     y = int(input("Ikkinchi sonni kiriting: "))
    
#     sum_of_squares = x**2 + y**2
#     square_of_sum = (x + y)**2
    
#     if sum_of_squares > square_of_sum:
#         print("Kvadratlari summasi katta.")
#     elif sum_of_squares < square_of_sum:
#         print("Summaning kvadrati katta.")
#     else:
#         print("Ikkalasi teng.")

# # 2. Staj uchun qo'shimcha haqni hisoblash
# def problem_2():
#     salary = float(input("Oylik maoshni kiriting: "))
#     experience = float(input("Stajni kiriting (yil): "))
    
#     if 2 <= experience < 5:
#         bonus = salary * 0.02
#     elif 5 <= experience < 10:
#         bonus = salary * 0.05
#     else:
#         bonus = 0
    
#     total_salary = salary + bonus
#     print(f"Ustama: {bonus:.2f}")
#     print(f"Umumiy oylik: {total_salary:.2f}")

# 3. Nuqtalarni O(0,0) bilan taqqoslash

# x0 = int(input("A nuqtaning koordinatalarini kiriting (x0): "))
# y0 = int(input("A nuqtaning koordinatalarini kiriting (y0): "))
    
# x1 = int(input("B nuqtaning koordinatalarini kiriting (x1): "))
# y1 = int(input("B nuqtaning koordinatalarini kiriting (y1): "))
# distance_A = math.sqrt(x0**2 + y0**2)
# distance_B = math.sqrt(x1**2 + y1**2)
    
# if distance_A > distance_B:
#      print("A nuqtasi O nuqtasidan uzoqroq.")
# elif distance_A < distance_B:
#     print("B nuqtasi O nuqtasidan uzoqroq.")
# else:
#     print("Ikki nuqta O nuqtasidan teng masofada.")

# 4. Uchburchakning to'g'ri burchakli bo'lishi
# def problem_4():
#     a = float(input("Birinchi tomonni kiriting: "))
#     b = float(input("Ikkinchi tomonni kiriting: "))
#     c = float(input("Uchinchi tomonni kiriting: "))
    
#     sides = sorted([a, b, c])
    
#     if sides[0]**2 + sides[1]**2 == sides[2]**2:
#         print("Uchburchak to'g'ri burchakli.")
#     else:
#         print("Uchburchak to'g'ri burchakli emas.")

# problem_4()
# 5. Musbat sonlarni kvadratga oshirish, manfiylarini o'zgarishsiz qoldirish
# def problem_5():
#     numbers = list((int, input("Uchta sonni kiriting: ").split(' ')))
    
#     results = [x**2 if x > 0 else x for x in numbers]
#     print("Natijalar:", results)
# problem_5()
# # 6. Nuqtaning chorakda yotishini aniqlash
# def problem_6():
#     x = float(input("X koordinatani kiriting: "))
#     y = float(input("Y koordinatani kiriting: "))
    
#     if x > 0 and y > 0:
#         print("Birinci chorak.")
#     elif x < 0 and y > 0:
#         print("Ikkinchi chorak.")
#     elif x < 0 and y < 0:
#         print("Uchinchi chorak.")
#     elif x > 0 and y < 0:
#         print("To'rtinchi chorak.")
#     elif x == 0 and y != 0:
#         print("Y-o'qi.")
#     elif y == 0 and x != 0:
#         print("X-o'qi.")
#     else:
#         print("Koordinatalar o'qning kesishgan joyida.")

# # 7. Uchburchaklarning yuzasini taqqoslash
# def problem_7():
#     a1, b1, c1 = map(float, input("Birinchi uchburchakning tomonlarini kiriting (a1 b1 c1): ").split())
#     a2, b2, c2 = map(float, input("Ikkinchi uchburchakning tomonlarini kiriting (a2 b2 c2): ").split())
    
#     def triangle_area(a, b, c):
#         s = (a + b + c) / 2
#         return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
#     area1 = triangle_area(a1, b1, c1)
#     area2 = triangle_area(a2, b2, c2)
    
#     if area1 > area2:
#         print("Birinchi uchburchakning yuzasi katta.")
#     elif area1 < area2:
#         print("Ikkinchi uchburchakning yuzasi katta.")
#     else:
#         print("Ikki uchburchakning yuzasi teng.")

# # 8. Musbat sonlarni kubga oshirish, manfiylarini 0 bilan almashtirish
# def problem_8():
#     numbers = list(map(int, input("Uchta sonni kiriting: ").split()))
    
#     results = [x**3 if x > 0 else 0 for x in numbers]
#     print("Natijalar:", results)

# # 9. Son juft va 5 ga qoldiqsiz bo'linadimi
# def problem_9():
#     number = int(input("Natural sonni kiriting: "))
    
#     if number % 2 == 0 and number % 5 == 0:
#         print("Son juft va 5 ga qoldiqsiz bo'linadi.")
#     else:
#         print("Son juft emas yoki 5 ga qoldiqsiz bo'linmaydi.")

# ., [19.08.2024 16:12]
# # 10. Nuqtaning birinchi chorakda yotishini aniqlash
# def problem_10():
#     x = float(input("X koordinatani kiriting: "))
#     y = float(input("Y koordinatani kiriting: "))
    
#     if x > 0 and y > 0:
#         print("Birinchi chorak.")
#     else:
#         print("Birinchi chorakda emas.")

# # 11. Depozit bo'yicha protsentdan har oylik to'lov summasini hisoblash
# def problem_11():
#     deposit = float(input("Qo'yilgan jamg'arma summasini kiriting: "))
#     period = float(input("Shartnoma muddatini kiriting (oy): "))
    
#     if period <= 6:
#         annual_rate = 0.06
#     else:
#         annual_rate = 0.08
    
#     monthly_rate = annual_rate / 12
#     monthly_payment = deposit * monthly_rate
#     print(f"Oylik to'lov summasi: {monthly_payment:.2f}")

# # 12. Ikkita son kvadratlari ayirmasi va ayirmasining kvadrati
# def problem_12():
#     x = int(input("Birinci sonni kiriting: "))
#     y = int(input("Ikkinchi sonni kiriting: "))
    
#     difference_of_squares = x**2 - y**2
#     square_of_difference = (x - y)**2
    
#     if abs(difference_of_squares) > square_of_difference:
#         print("Kvadratlari ayirmasi katta.")
#     elif abs(difference_of_squares) < square_of_difference:
#         print("Ayirmasining kvadrati katta.")
#     else:
#         print("Ikkalasi teng.")

# # 13. Nuqtalarning O(0,0) ga yaqinligi
# def problem_13():
#     x0, y0 = map(float, input("A nuqtaning koordinatalarini kiriting (x0 y0): ").split())
#     x1, y1 = map(float, input("B nuqtaning koordinatalarini kiriting (x1 y1): ").split())
    
#     distance_A = math.sqrt(x0**2 + y0**2)
#     distance_B = math.sqrt(x1**2 + y1**2)
    
#     if distance_A < distance_B:
#         print("A nuqtasi O nuqtasidan yaqinroq.")
#     elif distance_A > distance_B:
#         print("B nuqtasi O nuqtasidan yaqinroq.")
#     else:
#         print("Ikki nuqta O nuqtasidan teng masofada.")

# # 14. Uchburchak teng tomonli bo'lishi
# def problem_14():
#     a = float(input("Birinchi tomonni kiriting: "))
#     b = float(input("Ikkinchi tomonni kiriting: "))
#     c = float(input("Uchinchi tomonni kiriting: "))
    
#     if a == b == c:
#         print("Uchburchak teng tomonli.")
#     else:
#         print("Uchburchak teng tomonli emas.")

# # 15. Pifagor uchligini tekshirish
# def problem_15():
#     a, b, c = sorted(map(int, input("Uchta butun sonni kiriting (a b c): ").split()))
    
#     if a**2 + b**2 == c**2:
#         print("Pifagor uchligi.")
#     else:
#         print("Pifagor uchligi emas.")

# # 16. Doira va kvadrat yuzalari
# def problem_16():
#     circle_area = float(input("Doiraning yuzasini kiriting: "))
#     square_area = float(input("Kvadratning yuzasini kiriting: "))
    
#     radius = math.sqrt(circle_area / math.pi)
#     side = math.sqrt(square_area)
    
#     circle_inside_square = radius * math.sqrt(2) <= side
#     square_inside_circle = side / 2 <= radius
    
#     print(f"Doira kvadratga ichki chizilgan bo'la oladimi? {'Ha' if circle_inside_square else 'Yo\'q'}")
#     print(f"Kvadrat aylana ichiga chizilgan bo'la oladimi? {'Ha' if square_inside_circle else 'Yo\'q'}")

# # 17. Vaqtni chorakda aniqlash
# def problem_17():
#     time = float(input("Joriy vaqtni kiriting (0-24): "))
    
#     if 0 <= time < 12:
#         print("Sutkaning birinchi choragi (AM).")
#     elif 12 <= time < 24:
#         print("Sutkaning ikkinchi choragi (PM).")
#     else:
#         print("Noto'g'ri vaqt.")

# # 18. Son juft yoki 7 raqami bilan tugaydi
# def problem_18():
#     number = int(input("Natural sonni kiriting: "))
    
#     if number % 2 == 0:
#         print("Son juft.")
#     elif number % 10 == 7:
#         print("Son 7 raqami bilan tugaydi.")
#     else:
#         print("Son juft emas va 7 raqami bilan tugamaydi.")
# problem_18()


