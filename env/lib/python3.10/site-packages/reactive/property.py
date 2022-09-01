from typing import Any, Callable, Type


class ReactiveProperty:
    def __init__(self, value: Any, name: str = None, field_type: Type[Any] = None):
        self.value = value
        self.name = name
        self.history = [value]
        self._field_type = field_type
        self._on_change_handlers = []

    def __get__(self, instance: Any, owner: Any):
        if isinstance(self.value, bool):
            class ObservableBool:
                value = self.value
                name = self.name
                history = self.history
                on_change = self.on_change
            return ObservableBool()
        else:
            class ObservableProperty(type(self.value)):
                name = self.name
                history = self.history
                on_change = self.on_change
            return ObservableProperty(self.value)

    def __setattr__(self, name: str, value: Any):
        if name == "value":
            if callable(value):
                raise TypeError("type 'function' is invalid for the value of 'ReactiveProperty'.")
            elif value is None:
                raise TypeError("value of 'ReactiveProperty' cannot be 'None'.")

        return super().__setattr__(name, value)

    def __set__(self, instance: Any, value: Any):
        if self._field_type and not isinstance(value, self._field_type):
            raise TypeError(
                f"expected an instance of type '{self._field_type.__name__}' for attribute '{self.name}', got '{type(value).__name__}' instead")

        prev = self.value
        self.value = value

        if value != prev:
            for change_handler in self._on_change_handlers:
                change_handler(self.value, prev)

    def __delete__(self, instance: Any):
        del self.value

    def __set_name__(self, owner: Any, name: str):
        self.name = name

    def on_change(self, func: Callable[[Any, Any], None]):
        self._on_change_handlers.append(func)
