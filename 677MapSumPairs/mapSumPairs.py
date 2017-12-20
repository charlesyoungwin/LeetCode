class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dic[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        count = 0
        for (k, v) in self.dic.items():
            if k.index(prefix) == 0:
                count += v
        return count

obj = MapSum()
obj.insert('apple', 3)
print(obj.sum('ap'))