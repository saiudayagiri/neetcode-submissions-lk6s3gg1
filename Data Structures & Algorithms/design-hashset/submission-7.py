class MyHashSet:

    def __init__(self):
        self.key_map = [False] * 100001
        

    def add(self, key: int) -> None:
        self.key_map[key] = True
        

    def remove(self, key: int) -> None:
        self.key_map[key] = False
        

    def contains(self, key: int) -> bool:
        return self.key_map[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)