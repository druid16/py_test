# 4. Написать класс, который бы по всем внешним признакам был бы словарем, но позволял обращаться к ключам как к атрибутам


class Dict:
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def atribute(self, my_atr):
        for i in self.my_dict.keys():
            if i == my_atr:
                return i


b = {'a': 'b', 'c': 'd'}

a = Dict(b)

print(a.atribute('l'))
print(a.atribute('c'))
