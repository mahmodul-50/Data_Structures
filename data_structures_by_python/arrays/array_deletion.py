# ## with stl
# n = int(input("Enter number of elements: "))
# arr = []
# print("Enter elements: ")
# for i in range(n):
#     arr.append(int(input()))

# pos = int(input("Enter position to delete(0 based index): "))
# arr.pop(pos)
# print("After deleting the element: ", arr)


## without stl
n = int(input("Enter number of elements: "))
arr = []
# print("Enter elements: ")
for i in range(n):
    arr.append(int(input()))
pos = int(input("Enter position to delete(0 based index): "))
i = pos
while i < n - 1:
    arr[i] = arr[i + 1]
    i += 1
    
n -= 1
print("After deleting last element:", end=" ")
for i in range(n):
    print(arr[i], end=" ")