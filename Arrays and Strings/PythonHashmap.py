'''
Python hashmap implementation
Used for hashing strings
'''

class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(0, self.size)]

    @staticmethod
    def _hash(self, s):
        ret = 0
        for c in s:
            ret += ord(c)
        return ret % self.size

    def insert(self, key, value):
        h = self._hash(self, key)
        for e in self.table[h]:
            if (e[0] == key):
                e[1]= value
                break
        else:
            self.table[h].append([key, value])

    def get(self, key):
        h = self._hash(self, key)
        for e in self.table[h]:
            if (e[0] == key):
                return e[1]
        else:
            raise ValueError

# Tester driver function
def main():
   hmap = HashMap(8)
   hmap.insert("a", 5)
   hmap.insert("b", "hello")

   print(hmap.get("a"))

   hmap.insert("a", "why")
   print(hmap.get("a"))

if __name__ == '__main__':
    main()