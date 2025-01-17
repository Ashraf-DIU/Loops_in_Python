# c = 1
# while c <= 5:
#     print("Hello Loop", c)
#     c += 1
# print(c) 

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# # Multiplication Table
# n =  int(input("Input any Number : "))
# i = 1
# while i <= 10:
#     print(n, " x ", i, " = ",n*i)
#     i += 1

list = []
len = int(input("Enter Index Number of List : "))
n = 0
while n < len:
    element = int(input(f"Enter {n+1} Element : "))
    list.append(element)
    n += 1
print("So the List : ",list)
idx = 0
while idx < len:
    print(list[idx])
    idx +=  1