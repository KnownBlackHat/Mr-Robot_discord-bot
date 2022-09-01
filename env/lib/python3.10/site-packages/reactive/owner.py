import asyncio
from typing import Any, Callable

from .property import ReactiveProperty


class ReactiveOwner:
    def __init__(self):
        self.__on_change_handlers = []

    def on_change(self, func: Callable[..., None], *args):
        self.__on_change_handlers.append((func, [object.__getattribute__(self, arg.name) for arg in args]))

    def __getattribute__(self, name: str):
        obj = object.__getattribute__(self, name)
        if hasattr(obj, '__get__'):
            return obj.__get__(self, type(self))
        return obj

    def __set_reactive_attr(self, name: str, value: Any):
        try:
            obj = object.__getattribute__(self, name)
        except AttributeError:
            object.__setattr__(self, name, value)
            if hasattr(value, '__set_name__'):
                value.__set_name__(self, name)
            return None, False
        else:
            if hasattr(obj, '__set__'):
                if isinstance(obj, ReactiveProperty):
                    prev_value = obj.value
                    obj.__set__(self, value)
                    if prev_value != obj.value:
                        return obj, True
                    else:
                        return obj, False
                else:
                    obj.__set__(self, value)
                    return obj, False
            else:
                object.__setattr__(self, name, value)
                return obj, False

    def __set_reactive_attrs(self, **args):
        changed = False
        funccalls = {}

        for arg in args:
            res = self.__set_reactive_attr(arg, args[arg])
            obj, arg_changed = res
            changed = arg_changed or changed

            if not arg_changed:
                continue

            for change_handler in self.__on_change_handlers:
                func = change_handler[0]

                if obj in change_handler[1] or not change_handler[1]:
                    if func in funccalls:
                        funccalls[func] = funccalls[func] + [obj]
                    else:
                        funccalls[func] = [obj]

        return changed, funccalls

    async def _async_bulk_update(self, **args):
        changed, funccalls = self.__set_reactive_attrs(**args)

        for func in funccalls:
            if asyncio.iscoroutinefunction(func):
                await func(*funccalls[func])
            else:
                func(*funccalls[func])

        return changed

    def _bulk_update(self, **args):
        changed, funccalls = self.__set_reactive_attrs(**args)

        for func in funccalls:
            if asyncio.iscoroutine(func):
                continue
            else:
                func(*funccalls[func])

        return changed

    def __setattr__(self, name: str, value: Any):
        changed, funccalls = self.__set_reactive_attrs(**{name: value})

        for func in funccalls:
            if asyncio.iscoroutine(func):
                continue
            else:
                func(*funccalls[func])
