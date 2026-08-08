
# Iterable & Iterator because contains both dunder iter and dunder next method
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)

# for num in nums:
#     print(num)

print(next(nums))
print(next(nums))
#print(next(nums)) # Gives StopIteration exception for (1, 3)

while True:
	try:
		item = next(nums)
		print(item)
	except StopIteration:
		break

# Note: it prints 1 and 2 only once, and while loop printed from 3
# No reinitialization, just forward moving