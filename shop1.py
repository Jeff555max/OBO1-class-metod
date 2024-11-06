class Store:
    def __init__(self, name, address):
        """Инициализирует название магазина, адрес и пустой словарь для товаров."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию или None, если товар отсутствует."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")

# Пример создания объекта класса Store и использования методов
store = Store("Магазин Продукты", "ул. Пушкина, д. 12")

store.add_item("яблоки", 0.5)
store.add_item("бананы", 0.75)

print(f"Цена на яблоки: {store.get_price('яблоки')}")
store.update_price("яблоки", 0.6)
print(f"Цена на яблоки после обновления: {store.get_price('яблоки')}")

store.remove_item("бананы")
print(f"Цена на бананы: {store.get_price('бананы')}")