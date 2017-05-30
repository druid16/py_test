# 3. Реализовать класс для работы со списком дел, который предоставляет методы:




# - поставить дело с номером m на позицию n

class Deal:
    def __init__(self, id, text):
        self._id = id
        self._text = text

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self.id = value


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def __str__(self):
        return 'Дело №: {}, Описание: {}.'.format(self.id, self.text)


class OneNote(Deal):
    def __init__(self):
        self.note = []


    def add_deal(self, new_deal):
        return self.note.append(new_deal)


    def get_current_deal(self, id):
        note = list(filter(lambda x: x.id == id, self.note))
        return note[0]

    def remove_deal(self, id):
        deal = list(filter(lambda x: x.id == id, self.note))
        return self.note.remove(deal[id])

    def change_deal(self, id, new):
        deal = list(filter(lambda x: x.id == id, self.note))
        for rep_deal in deal:
            rep_deal.id = new
        return deal[0]

    def __str__(self):
        return '\n'.join(map(str, self.note))


deal1 = Deal('asdf', 'Купить вещи для собаки')
deal2 = Deal(1, 'Купить билеты на Ямайку')

note = OneNote()
note.add_deal(deal1)
note.add_deal(deal2)

print('мое дело', note.get_current_deal(1))

