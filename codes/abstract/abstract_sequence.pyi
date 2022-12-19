from .abstract_sprite import AbstractSprite


class AbstractSet:
    set_group: set[AbstractSprite]

    def __init__(self): ...

    def __iter__(self): ...

    def __contains__(self, item): ...

    def add(self, sprite) -> None: ...

    def kill(self, element) -> None: ...

    def safe_kill(self, element) -> None: ...


class AbstractDoubleSet:
    set_group: set[AbstractSprite]
    kill_group: set[AbstractSprite]

    def __init__(self): ...

    def __iter__(self): ...

    def __contains__(self, item): ...

    def add(self, sprite) -> None: ...

    def kill(self, element) -> None: ...

    def update(self) -> None: ...


class AbstractDict:
    dict_group: dict
    def __init__(self):...
    def __contains__(self, item):...
    def __iter__(self):...
    def get(self, item):...