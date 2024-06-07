def square_or_fourth_power(a, b, c):
    def process_number(n):
        if n >= 0:
            return n ** 2
        else:
            return n ** 4

    a, b, c = map(process_number, [a, b, c])
    print("Результати обчислень: ", a, b, c)

def closer_to_origin(x1, y1, x2, y2):
    distance_A = (x1**2 + y1**2) ** 0.5
    distance_B = (x2**2 + y2**2) ** 0.5

    if distance_A < distance_B:
        print("Точка A ближче до початку координат.")
    else:
        print("Точка B ближче до початку координат.")

def triangle_angles(angle1, angle2):
    angle3 = 180 - (angle1 + angle2)

    if angle1 > 0 and angle2 > 0 and angle3 > 0:
        print("Такий трикутник існує.")
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("Трикутник є прямокутним.")
        else:
            print("Трикутник не є прямокутним.")
    else:
        print("Такий трикутник не існує.")

def modify_numbers(x, y):
    if x < y:
        x = (x + y) / 2
        y = x * y * 2
    else:
        y = (x + y) / 2
        x = x * y * 2

    print("Змінені значення: x =", x, ", y =", y)

def point_location(x, y):
    if x == 0 and y == 0:
        print("Точка знаходиться в початку координат.")
    elif x == 0:
        print("Точка знаходиться на осі Y.")
    elif y == 0:
        print("Точка знаходиться на осі X.")
    elif x > 0 and y > 0:
        print("Точка знаходиться в першому координатному куті.")
    elif x < 0 and y > 0:
        print("Точка знаходиться в другому координатному куті.")
    elif x < 0 and y < 0:
        print("Точка знаходиться в третьому координатному куті.")
    else:
        print("Точка знаходиться в четвертому координатному куті.")

def replace_numbers(a, b):
    if a != b:
        max_val = max(a, b)
        a = max_val
        b = max_val
    else:
        a = 0
        b = 0

    print("Змінені значення: a =", a, ", b =", b)

def count_negative(a, b, c):
    negative_count = sum(1 for x in [a, b, c] if x < 0)
    print("Кількість негативних чисел:", negative_count)

def count_positive(a, b, c):
    positive_count = sum(1 for x in [a, b, c] if x > 0)
    print("Кількість додатних чисел:", positive_count)

def count_integers(a, b, c):
    integer_count = sum(1 for x in [a, b, c] if x.is_integer())
    print("Кількість цілих чисел:", integer_count)

def divisor_check(a, b, c, k):
    for number in [a, b, c]:
        if number % k == 0:
            print(f"Число {k} є дільником числа {number}")

def main():
    # 1
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))
    square_or_fourth_power(a, b, c)

    # 2
    x1 = float(input("Введіть координату x1 для точки A: "))
    y1 = float(input("Введіть координату y1 для точки A: "))
    x2 = float(input("Введіть координату x2 для точки B: "))
    y2 = float(input("Введіть координату y2 для точки B: "))
    closer_to_origin(x1, y1, x2, y2)

    # 3
    angle1 = float(input("Введіть перший кут (в градусах): "))
    angle2 = float(input("Введіть другий кут (в градусах): "))
    triangle_angles(angle1, angle2)

    # 4
    x = float(input("Введіть перше число: "))
    y = float(input("Введіть друге число: "))
    modify_numbers(x, y)

    # 5
    x = float(input("Введіть координату x точки A: "))
    y = float(input("Введіть координату y точки A: "))
    point_location(x, y)

    # 6
    a = int(input("Введіть перше ціле число: "))
    b = int(input("Введіть друге ціле число: "))
    replace_numbers(a, b)

    # 7
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))
    count_negative(a, b, c)

    # 8
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))
    count_positive(a, b, c)

    # 9
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))
    count_integers(a, b, c)

    # 10
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))
    k = float(input("Введіть число k: "))
    divisor_check(a, b, c, k)

if __name__ == "__main__":
    main()
