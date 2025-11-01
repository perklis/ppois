from typing import Any, Generic, TypeVar
from task2.exceptions import ConstContainerEditingError

T = TypeVar("T")


class ConstContainer(Generic[T]):
    __slots__ = ("_wrapped",)
    _wrapped: T

    def __init__(self, wrapped: T) -> None:
        object.__setattr__(self, "_wrapped", wrapped)

    def __getattribute__(self, name: str) -> Any:
        wrapped_obj = object.__getattribute__(self, "_wrapped")
        try:
            attr = getattr(wrapped_obj, name)
        except AttributeError:
            raise ConstContainerEditingError(f"Нет '{name}' в объекте")

        return attr

    def __setattr__(self, name: str, value: Any) -> None:
        raise ConstContainerEditingError("Невозможно менять поле константы")

    def __repr__(self) -> str:
        wrapped_obj = object.__getattribute__(self, "_wrapped")
        return f"ConstContainer({repr(wrapped_obj)})"
