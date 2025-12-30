# arr = list(map(int, input("Enter elements: ").split()))
# pos = int(input("Enter position: "))
# val = int(input("Enter value: "))

# arr.insert(pos, val)

# print("After insertion: ", arr)

## without stl
n = int(input("Enter number of elements: "))
arr = [0]*100
print("Enter element: ")
for i in range(n):
    arr[i] = int(input())
pos = int(input("Enter position to insert (0 based): "))
val = int(input("Enter value to insert: "))

i = n
while i > pos:
    arr[i] = arr[i - 1]
    i -= 1
    
arr[pos] = val
n += 1
print("After insertion: ", end=" ")
for i in range(n):
    print(arr[i], end=" ")