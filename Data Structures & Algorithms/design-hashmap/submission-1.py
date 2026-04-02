class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000000

    def put(self, key: int, value: int) -> None:
        self.map[key-1] = value

    def get(self, key: int) -> int:
        return self.map[key-1]

    def remove(self, key: int) -> None:
        self.map[key-1] = -1