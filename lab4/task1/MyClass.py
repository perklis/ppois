from typing import Self


class MyClass:
    def __init__(self, value: int) -> None:
        self._value: int = value

    @property
    def value(self) -> int:
        return self._value

    def __lt__(self, some: Self, /) -> bool:
        return self._value < some.value

    def __eq__(self, some: object, /) -> bool:
        if isinstance(some, MyClass):
            return self._value == some.value
        return False

    def __gt__(self, some: Self, /) -> bool:
        return self._value > some.value

    def __repr__(self) -> str:
        return f"MyClass({self._value})"
