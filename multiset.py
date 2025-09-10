from collections import Counter
from typing import Union, Iterable


class MultiSet:
    """Класс для работы с неориентированным мультимножеством."""

    def __init__(self, data: Union[str, Iterable, None] = None):
        self.__elements = Counter()
        if data:
            self.add_from(data)

    def add_from(self, data: Union[str, Iterable]) -> None:
        """Добавить элементы из строки или коллекции."""
        if isinstance(data, str):
            for ch in data:
                self.__elements[ch] += 1
        elif isinstance(data, Iterable):
            for item in data:
                self.__elements[item] += 1
        else:
            raise TypeError("Поддерживаются только str и Iterable")

    def add(self, item) -> None:
        """Добавить один элемент."""
        self.__elements[item] += 1

    def remove(self, item) -> None:
        """Удалить один элемент (если он есть)."""
        if self.__elements[item] > 0:
            self.__elements[item] -= 1
            if self.__elements[item] == 0:
                del self.__elements[item]

    def count(self, item) -> int:
        """Количество вхождений элемента."""
        return self.__elements.get(item, 0)

    def is_empty(self) -> bool:
        """Проверка на пустоту."""
        return not self.__elements

    def __str__(self) -> str:
        """Красивое строковое представление."""
        elements_repr = []
        for item, cnt in self.__elements.items():
            elements_repr.extend([str(item)] * cnt)
        return "{" + ", ".join(elements_repr) + "}"

    def __eq__(self, other) -> bool:
        return isinstance(other, MultiSet) and self.__elements == other.__elements

    def __len__(self) -> int:
        return sum(self.__elements.values())


def run_console():
    print("Добро пожаловать в программу работы с мультимножествами!")
    ms = MultiSet()

    while True:
        print("\nМеню:")
        print("1 - Добавить строку")
        print("2 - Добавить элемент")
        print("3 - Удалить элемент")
        print("4 - Показать мультимножество")
        print("5 - Проверить количество элемента")
        print("0 - Выход")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            s = input("Введите строку: ")
            ms.add_from(s)
        elif choice == "2":
            elem = input("Введите элемент: ")
            ms.add(elem)
        elif choice == "3":
            elem = input("Введите элемент для удаления: ")
            ms.remove(elem)
        elif choice == "4":
            print("Мультимножество:", ms)
        elif choice == "5":
            elem = input("Введите элемент для проверки: ")
            print(f"Количество: {ms.count(elem)}")
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    run_console()
