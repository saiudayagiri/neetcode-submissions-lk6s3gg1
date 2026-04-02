class MyHashSet:

    def __init__(self):
        self.data = [False] * 1000000

    def add(self, key: int) -> None:
        self.data[key-1] = True

    def remove(self, key: int) -> None:
        self.data[key-1] = False

    def contains(self, key: int) -> bool:
        return self.data[key-1]