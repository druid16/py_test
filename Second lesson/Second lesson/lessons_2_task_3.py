# 3. Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic():
    print("Введите два числа:")
    a = float(input())
    b = float(input())
    print(
        "Введите знак операции которая должна быть произведена над числами из предоставленных (+ или сложить; — или  "
        "вычесть; * или умножить; / или разделить (первое на второе).)"
        )
    op = str(input())
    if op == str ("+") or op == "сложить":
        return (float(a+b))
    elif op == str('-') or op == "вычесть":
        return (float(a-b))
    elif op == str('*') or op == "умножить":
        return (a*b)
    elif op == str('/') or op == "разделить":
        return (float(a/b))
    else:
        return ("Неизвестная операция")
print(arithmetic())
