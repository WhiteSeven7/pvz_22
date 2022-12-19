class AbstractSet:
    def __init__(self):
        self.set_group = set()

    def __iter__(self):
        return iter(self.set_group)

    def __contains__(self, item):
        return item in self.set_group

    def add(self, sprite):
        self.set_group.add(sprite)

    def kill(self, element):
        self.set_group.remove(element)

    def safe_kill(self, element):
        if element in self.set_group:
            self.set_group.remove(element)


class AbstractDoubleSet:
    def __init__(self):
        self.set_group = set()
        self.kill_group = set()

    def __iter__(self):
        return iter(self.set_group)

    def __contains__(self, item):
        return item in self.set_group

    def add(self, sprite):
        self.set_group.add(sprite)

    def kill(self, element):
        self.kill_group.add(element)

    def update(self):
        for sprite in self.set_group:
            sprite.update()
        self.set_group -= self.kill_group
        self.kill_group.clear()
