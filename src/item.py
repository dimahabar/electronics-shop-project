class Item():
    pass
item1 = Item()
item2 = Item()


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = int(self.price * self.quantity)
        return self.total_price


    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return float(self.price * Item.pay_rate)





