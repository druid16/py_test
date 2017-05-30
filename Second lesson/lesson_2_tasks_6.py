# 6. Написать функцию-фабрику, которая будет возвращать функцию умножения на аргумент





def newfunc(n):
    n = input()
    def myfunc(x):
        return x * n
    return myfunc

r = newfunc(n)

print(r())