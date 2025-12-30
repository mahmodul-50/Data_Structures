n = int(input("Enter number of elements: "))
arr = []
print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

pos = int(input("Enter element to search: "))

if pos in arr:
    print("Element found at index", arr.index(pos))
else:
    print("Element not found")
