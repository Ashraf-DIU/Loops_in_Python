# veg = ["potato", "korolla", "chili", "onion"]
# for val in veg:
#     print(val)

# t = tuple(map(int, input("Enter Tuples : ").split()))
# for i in t:
#     print(i)

#  prime number or not
num = int(input("Enter an  integer Number : "))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number. It is divisible by {i}.")
        break
else:
    print(f"{num} is a prime number.")
