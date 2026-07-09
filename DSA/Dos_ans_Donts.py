
# Variables
n = 0
print('n = ', n) # n = 0

n = 'abc'
print('n = ', n) # n = abc

# Multiple assignments
n, m = 0, 'abc'
n, m, y = 0, 'abc', False

#Incrementing
n = n + 1
n += 1
# n++ -> no

# None is null (absence of value)
n = 4
n = None
print('n = ', n) # n = None

# If statement don't need parentheses() or curly braces{}
n = 1
if n > 2:
    n += 2
elif n == 2:
    n *= 2
else:
    n -= 1

# Parentheses needed for multi line conditions
# and == &&
# or == ||
n , m = 1, 2
if ((n > 2 and 
    n != m) or n == m):
    n+= 2

# while loops are similar
n = 0
while n < 5:
    print(n)
    n+= 1

# looping from i = 0 to i = 4 (for loops)
for i in range(5):
    print(i)

# looping from i = 2 to i = 5 (for loops)
for i in range(2, 6):
    print(i)

# looping from i = 5 to i = 2 (for loops)
for i in range(5, 1, -1):
    print(i)

# Division is decimal by default
print(5 / 2) # 2.5 instead of 2

# Double slash for floor division or integer division or ROUND DOWN
print(5 // 2) # 2

# CAREFUL: most languages round towards 0 by default, so negative numbers will be round down
print(-3 / 2) # -1.5
print(-3 // 2) # -2

# Workaround for rounding towards 0 -> use decimal division then convert to int
print(int(-3 / 2)) # -1

# Modulo is similar
print(10 % 3) #1

# In negative case
print(-10 % 3) #2

# to be consistent with other languages
import math
print(math.fmod(-10, 3)) # -1.0

# More math helpers
print(math.floor(3 / 2)) # 1
print(math.ceil(3 / 2)) # 2
print(math.sqrt(2)) # 1.4142135623730951
print(math.pow(2, 3)) # 8.0

# Max / min int
a = float("inf")
b = float("-inf")

# Py numbers are infinite so they never overflow
import math
print(math.pow(2, 200)) # 1.6069380442589903e + 60

# but still less than infinity
print(math.pow(2, 200) < float("inf")) # True

# Arrays called lists in python
arr = [1, 2, 3]
print(arr) # [1, 2, 3]

# Arrays can be used as stack
arr.append(4)
arr.append(5)
print(arr) # [1, 2, 3, 4, 5]

arr.pop()
print(arr) # [1, 2, 3, 4]

arr.insert(1, 7) # O(n)
print(arr) # [1, 7 , 2 ,3 , 4]

arr[0] = 0 # O(1)
arr[3] = 0
print(arr) # [0, 7, 2, 0, 4]

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr) # [1, 1, 1, 1, 1]
print(len(arr)) # 5

# Careful: -1 is not out of bounds, its the last value
arr = [1, 2, 3]
print(arr[-1]) #3

# Sublists (aka slicing) , last index non-inclusive
arr = [1, 2, 3, 4]
print(arr[1: 3]) # [2, 3]

# Unpacking
a, b, c = [1, 2, 3]
# Be careful though
a, b = [1, 2, 3] # wrong

## Looping through arrays
nums = [1, 2, 3]

# using index -> dont use this
for i in range(len(nums)) :
    print(nums[i])

# Without index
for x in nums:
    print(x)

# With index and value
for i, x in enumerate(nums):
    print(i, x)

# Loop through multiple arrays simultaneously
# Using unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Reverse an array
nums = [1, 2, 3]
nums.reverse()
print(nums) # [3, 2, 1]

# Sorting an array
nums = [5, 4, 7, 3, 8]
nums.sort()
print(nums) # [3, 4, 5, 7, 8]

nums.sort(reverse=True)
print(nums) # [8, 7, 5, 4, 3]

# Sorting list of strings
arr = ["bob", "doe", "candice", "alice"]
arr.sort()
print(arr) # ['alice', 'bob', 'candice', 'doe'] # Alphabetical sort

# Custom string sort (based on string lengths)
arr.sort(key= lambda x : len(x))
print(arr) # ['bob', 'doe', 'alice', 'candice']

# List comprehension
arr = [i for i in range(5)]
print(arr) # [0, 1, 2, 3, 4]

arr = [i+i for i in range(5)]
print(arr) # [0, 2, 4, 6, 8]

# 2D lists
arr = [[0]* 4 for i in range(4)] # will give grid of 4 * 4 of 0

# This won't work
arr = [[0] * 4] * 4
print(arr) # will work but, modifying any col of any row will modify that col of all rows

# Strings are similar to arrays
s = 'abc'
print(s[0:2]) #ab

# But, they re immutable, cannot modify using index
s[0] = 'b' # not work

# can update (result in new string) O(n)
s += 'def'
print(s) #abcdef

# Valid numeric strings can be converted
print(int("123") + int("123")) #246

# Numbers can be converted to strings
print(str(123) + str(123)) #123123

# In rare cases, may need ASCII value of a char
print(ord('a'))
print(ord('b'))

# Combine a list of strings (with an empty delimiter)
strs = ['ab', 'cd', 'ef']
print("".join(strs)) # abcdef

# Split string based on specific delimiter into list
strs = 'ab cd ef gh'
print(strs.split(" ")) # ['ab', 'cd', 'ef', 'gh']


# Queues (double ended queues by default)
from collections import deque

q = deque()
q.append(4)
q.append(5)
q.append(6)
print(q) # deque([4, 5, 6])

q.popleft()
print(q) # deque([5, 6])

q.appendleft(1)
print(q) # deque([1, 5, 6])

q.pop()
print(q) # deque([1, 5])

# Hashset or set - no duplicates
s = set()
s.add(1)
s.add(2)
print(s) # {1, 2}
print(len(s))

print(1 in s) # True
print(2 in s) # True
print(3 in s) # False

s.remove(1)
print(1 is s) # False

# List to set
print(set([1, 2, 3])) # {1, 2, 3}

# Set Comprehension
mySet = {i for i in range(5)}
print(mySet) # {0, 1, 2, 3, 4}

# Hashmap or map or dict
d = dict()
myMap = {}
myMap['alice'] = 88
myMap['bob'] = 77
print(myMap) # {'alice' : 88, 'bob' : 77}
print(len(myMap)) # 2

myMap["alice"] = 80
print(myMap["alice"]) # 80

print("alice" in myMap) # True
myMap.pop("alice")
print("alice" in myMap) # False

myMap = { "alice": 90, "bob": 70 }
print(myMap) # {"alice": 90, "bob": 70}

# Dict comprehension - useful for building adjacency lists
myMap = { i: 2*i for i in range(3) }
print(myMap)

# Looping through maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)

# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# Can't modify
# tup[0] = 0

# Can be used as key for hash map/set
myMap = { (1,2): 3 }
print(myMap[(1,2)])

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)

# Lists can't be keys
# myMap[[3, 4]] = 5

#heaps
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# No max heaps by default, work around is
# to use min heap and multiply by -1 when push & pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

#Functions
def myFunc(n, m):
    return n * m

print(myFunc(3, 4))

# Nested functions have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))

# Can modify objects but not reassign
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        
        # will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)

# Classes
class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)
    
    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()

myObj = MyClass([1, 2, 3])
print(myObj.getLength())
print(myObj.getDoubleLength())