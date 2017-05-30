from random import choice


# 2. Реализовать класс(ы) для работы с карточной колодой, который предоставляет методы:
# - инициализация заданным числом карт (36 или 52)
# - получение карты (карта должна пропадать из колоды после того, как была получена)
# - сравнение двух карт (при это учесть, что туз > король > дама > валет > числовые карты)
# - получение оставшегося числа карт в колоде
# Не забыть про то, что каждая карта имеет масть.




class Cards:
    def __init__(self, new_deck):
        self.new_deck = []
        self._new_deck = new_deck

    def init_deck(self):
        card_suit = ['\u2665', '\u2666', '\u2663', '\u2660']
        from_row = 0
        if self._new_deck == 32:
            from_row = 6
        elif self._new_deck == 52:
            from_row = 2
        for i in range(len(card_suit)):
            for j in range(from_row, 15):
                self.new_deck.append([j, card_suit[i]])
        return self.new_deck

    def get_card(self):
        get_card = choice(self.new_deck)
        self.new_deck.remove(get_card)
        return get_card

    def __str__(self):
        return '{}'.format(self.new_deck)


deck = Cards(52)
deck.init_deck()

print(deck.get_card())
print(deck)
