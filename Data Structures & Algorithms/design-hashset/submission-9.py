class MyHashSet:

    def __init__(self):
        self.key_map = set()
        

    def add(self, key: int) -> None:
        self.key_map.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.key_map:
            self.key_map.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.key_map:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)