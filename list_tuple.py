# list = []
# len = int(input("Enter Index Number of List : "))
# n = 0
# while n < len:
#     element = int(input(f"Enter {n+1} Element : "))
#     list.append(element)
#     n += 1

# print("So the List : ",list)

# idx = 0
# while idx < len: # list traverse
#     print(list[idx])
#     idx += 1

# Tuple
# Taking input
a = list(map(int, input("Enter elements separated by spaces: ").split()))

# Converting list to tuple
t = tuple(a)
print("So the tuple is:", t)
print("Length of the tuple:", len(t))

x = 3  # Element to search for
i = 0

while i < len(t):
    if t[i] == x:
        print("Found at index", i)
    else:
        print("Finding...")
    i += 1

