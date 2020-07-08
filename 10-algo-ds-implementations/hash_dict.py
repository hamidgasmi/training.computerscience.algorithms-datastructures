import random

class HashMap:

    def __init__(self, initial_size = 100, universe_size = 10000):
        
        self.capacity = initial_size
        self.universe_size = universe_size
        self.size = 0

        self.hash_map = [[] for _ in range(self.capacity)]

        self.prime = 10007 
        assert(self.prime > self.universe_size)

        self.a = random.randint(1, self.prime - 1)
        self.b = random.randint(1, self.prime - 1)
    
    def _rehash(self) -> None:
        
        old_hash_map = self.hash_map

        self.capacity = min(self.universe_size, 2 * self.capacity)
        self.hash_map = [[] for _ in range(self.capacity)]

        for chain in old_hash_map:
            for (key, val) in chain:
                self.hash_map[self._hash(key)].append((key, val))

        old_hash_map.clear()

    def _hash(self, key:int) -> int:
        
        return ((self.a * key + self.b) % self.prime) % self.capacity

    def _load_factor(self):

        return self.size / self.capacity
    
    def _pos_in_chain(self, key:int, hash_pos: int) -> int:
        
        for i in range(len(self.hash_map[hash_pos])):
            
            if self.hash_map[hash_pos][i][0] == key:
                return i
        
        return -1
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        pos_key = self._hash(key)
        pos_in_chain = self._pos_in_chain(key, pos_key)
        
        if pos_in_chain == -1:
            self.hash_map[pos_key].append((key, value))
            self.size += 1

            if self._load_factor() > 0.5:
                self.rehash()

        else:
            self.hash_map[pos_key][pos_in_chain] = (key, value)
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        pos_key = self._hash(key)
        pos_in_chain = self._pos_in_chain(key, pos_key)
        
        return -1 if pos_in_chain == -1 else self.hash_map[pos_key][pos_in_chain][1]
    
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        pos_key = self._hash(key)
        pos_in_chain = self._pos_in_chain(key, pos_key)
        
        if pos_in_chain != -1:
            self.size -= 1
            self.hash_map[pos_key].pop(pos_in_chain)
        