#### HASH USAGE ####

names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}
for name in names:
    # If countMap does not contain name
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1
        
print(countMap)

#### HASH IMPLEMENTATION ####

class Pair:
    def __init__(self, key, val):
        """
        Storing pairs within the Hashmap
        """
        self.key = key
        self.val = val

class HashMap:
    def __init__(self):
        """
        Initialsie the hashmap, initial size of keys (0) and capacity of 2
        Map is maintained as an array, initialised with None
        """
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key):
        """
        hashing function - Given a key return an integer 
        """
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity
    
    def get(self, key):
        """
        Given a key, return the value of the key if it exists 
        Will loop - open addressing to find the index, if index is occupied, increment index
        """
        index = self.hash(key)
        
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None
    
    def put(self, key, val):
        """
        Insert into the hashmap. Conver the key to some index, and loop through the map until an empty slot is found
        """
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            
            index += 1
            index = index % self.capacity
            
    def rehash(self):
        """
        When we perform re-hashing, we double the capacity, copy our previous map's values into our new map and set the size to be zero.
        """
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)
                
    def print(self):
        """
        Print all pairs in the hashmap
        """
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)





