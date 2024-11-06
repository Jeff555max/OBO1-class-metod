class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавить товар в ассортимент."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.\n")

    def remove_item(self, item_name):
        """Удалить товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.\n")
        else:
            print(f"Товар '{item_name}' не найден.\n")

    def get_price(self, item_name):
        """Получить цену товара по его названию."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновить цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '{item_name}' обновлена до {new_price}.\n")
        else:
            print(f"Товар '{item_name}' не найден.\n")

def main():
    # Создаем несколько объектов класса Store
    store1 = Store("Магазин Овощи", "ул. Ленина, 10")
    store2 = Store("Магазин Фрукты", "ул. Гагарина, 20")
    store3 = Store("Магазин Напитки", "ул. Победы, 30")

    stores = [store1, store2, store3]

    # Наполняем магазины начальным ассортиментом
    store1.add_item("картофель", 0.5)
    store1.add_item("морковь", 0.4)

    store2.add_item("яблоки", 1.0)
    store2.add_item("бананы", 1.2)

    store3.add_item("вода", 0.8)
    store3.add_item("лимонад", 1.5)

    while True:
        print("Выберите магазин:")
        for i, store in enumerate(stores):
            print(f"{i}: {store.name} ({store.address})")

        choice = input("Введите номер магазина (или 'exit' для выхода): ")
        if choice.lower() == 'exit':
            break

        if choice.isdigit():
            store_index = int(choice)
            if 0 <= store_index < len(stores):
                selected_store = stores[store_index]

                while True:
                    print(f"\nВы выбрали '{selected_store.name}' на {selected_store.address}.")
                    print("Доступные действия:")
                    print("1: Добавить товар")
                    print("2: Удалить товар")
                    print("3: Получить цену товара")
                    print("4: Обновить цену товара")
                    print("5: Вернуться к выбору магазина")

                    action = input("Введите номер действия: ")

                    if action == "1":
                        item_name = input("Введите название товара: ")
                        price = float(input("Введите цену товара: "))
                        selected_store.add_item(item_name, price)

                    elif action == "2":
                        item_name = input("Введите название товара: ")
                        selected_store.remove_item(item_name)

                    elif action == "3":
                        item_name = input("Введите название товара: ")
                        price = selected_store.get_price(item_name)
                        if price is not None:
                            print(f"Цена на '{item_name}' составляет {price}.\n")
                        else:
                            print(f"Товар '{item_name}' не найден.\n")

                    elif action == "4":
                        item_name = input("Введите название товара: ")
                        new_price = float(input("Введите новую цену товара: "))
                        selected_store.update_price(item_name, new_price)

                    elif action == "5":
                        break

                    else:
                        print("Некорректный выбор. Попробуйте еще раз.\n")
            else:
                print("Некорректный номер магазина.\n")
        else:
            print("Некорректный ввод. Пожалуйста, введите номер.\n")

if __name__ == "__main__":
    main()