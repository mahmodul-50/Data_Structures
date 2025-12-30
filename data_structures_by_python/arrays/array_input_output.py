n = int(input("Enter number of elements: "))
arr = []
print("Enter elements:")


# method 1
for i in range(n):
    arr.append(int(input()))

# method 2
# arr = list(map(int, input().split()))
    
# print("Array elements are:")
# for i in arr:
#     print(i)

print("Array elements are:", end=" ")
for x in arr:
    print(x, end=" ")