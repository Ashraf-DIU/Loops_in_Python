list = []
len = int(input("Enter Index Number of List : "))
n = 0
while n < len:
    element = int(input(f"Enter {n+1} Element : "))
    list.append(element)
    n += 1

print("So the List : ",list)

idx = 0
while idx < len: # list traverse
    print(list[idx])
    idx += 1