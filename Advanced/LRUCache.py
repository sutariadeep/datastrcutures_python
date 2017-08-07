#Other source https://discuss.leetcode.com/topic/3831/very-short-solution-using-python-s-ordereddict
#Original source https://www.kunxi.org/blog/2014/05/lru-cache-in-python/
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1

import collections

class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if not key in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

class LRUCache3:
    # dictionary + doubly linked list
    class Node:
        def __init__(self, key, value):
            self.prev = None
            self.key = key
            self.value = value
            self.next = None

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity, self.dict = capacity, {}
        self.head, self.tail = self.Node('head', 'head'), self.Node('tail', 'tail') # dummy head node and dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    # @return an integer
    def get(self, key):
        if key not in self.dict:
            return -1
        else:
            self.insertNodeAtFirst(self.unlinkNode(self.dict[key]))
            return self.dict[key].value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dict:
            self.insertNodeAtFirst(self.unlinkNode(self.dict[key]))
            self.dict[key].value = value
        else:
            if len(self.dict) >= self.capacity: # remove the least recently used element
                del self.dict[self.unlinkNode(self.tail.prev).key]
            self.dict[key] = self.Node(key, value)
            self.insertNodeAtFirst(self.dict[key])

    def unlinkNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node

    def insertNodeAtFirst(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node        

cache = LRUCache2( 2 );

cache.set(1, 1);
cache.set(2, 2);
print cache.get(1);       # returns 1
cache.set(3, 3);    # evicts key 2
print cache.get(2);       # returns -1 (not found)
cache.set(4, 4);    # evicts key 1
print cache.get(1);       # returns -1 (not found)
print cache.get(3);       # returns 3
print cache.get(4);       # returns 4