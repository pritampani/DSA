#chaning in hashing in python
# class myhash:
#     def __init__(self,b) -> None:
#         self.bucket = b
#         self.table = [[] for x in range(b)]
        
#     def insert(self,x):
#         i = x%self.bucket
#         self.table[i].append(x)
#     def remove(self,x):
#         i = x%self.bucket
#         if x in self.table[i]:
            
#             self.table[i].remove(x)
#     def search(self,x):
#         i = x%self.bucket
#         return x in self.table[i]
# h = myhash(7)
# h.insert(70)
# h.insert(71)
# h.insert(9)
# h.insert(56)
# h.insert(72)
# print(h.search(56))
# h.remove(56)
# print(h.search(56))
# h.remove(56)







#open Aderessing in python
#liner probing














# frequency of all array item
def frequency(arr):
    freq_dict = {}
    for i in range(len(arr)):
        if arr[i] in freq_dict:
            freq_dict[arr[i]] += 1
        else:
            freq_dict[arr[i]] = 1
    return freq_dict

print(frequency([1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]))





#open Addressing in hashing


# class MyHash:
#     def __init__(self, c):
#         self.cap = c
#         self.table = [-1] * c
#         self.size = 0

#     def hash(self, x):
#         return x % self.cap

#     def search(self, x):
#         h = self.hash(x)
#         t = self.table
#         i = h
#         while t[i] != -1:
#             if t[i] == x:
#                 return True
#             i = (i + 1) % self.cap
#             if i == h:
#                 return False
#         return False

#     def insert(self, x):
#         if self.size == self.cap:
#             return False

#         if self.search(x) == True:
#             return False
#         i = self.hash(x)
#         t = self.table
#         while t[i] not in (-1, -2):
#             i = (i + 1) % self.cap

#         t[i] = x
#         self.size = self.size + 1
#         return True

#     def remove(self, x):
#         h = self.hash(x)
#         t = self.table
#         i = h
#         while t[i] != -1:
#             if t[i] == x:
#                 t[i] = -2
#                 return True
#             i = (i + 1) % self.cap
#             if i == h:
#                 return False
#         return False


# h = MyHash(7)
# h.insert(70)
# h.insert(71)
# h.insert(9)
# h.insert(56)
# h.insert(72)
# print(h.search(56))
# h.remove(56)
# print(h.search(56))
# h.remove(56)


# class HashNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None

# class HashTable:
#     def __init__(self, table_size=128):
#         self.TABLE_SIZE = table_size
#         self.table = [None] * self.TABLE_SIZE

#     def hash_function(self, key):
#         return sum(ord(char) for char in key) % self.TABLE_SIZE

#     def insert(self, key, value):
#         hash_value = self.hash_function(key)
#         if not self.table[hash_value]:
#             self.table[hash_value] = HashNode(key, value)
#         else:
#             entry = self.table[hash_value]
#             while entry.next:
#                 entry = entry.next
#             entry.next = HashNode(key, value)

#     def search(self, key):
#         hash_value = self.hash_function(key)
#         entry = self.table[hash_value]
#         while entry:
#             if entry.key == key:
#                 return entry.value
#             entry = entry.next
#         return -1

# def main():
#     ht = HashTable()
#     ht.insert("hello", 1)
#     ht.insert("world", 2)
#     print(ht.search("hello"))
#     print(ht.search("world"))

# if __name__ == "__main__":
#     main()







a=[0] * 999
