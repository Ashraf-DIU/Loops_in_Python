# break

# Taking input
t = tuple(map(int, input("Enter elements separated by spaces: ").split()))
print("So the tuple is:", t)
print("Length of the tuple:", len(t))
x = 3  # Element to search for
i = 0
while i < len(t):
    if t[i] == x:
        print("Found at index", i)
        break
    else:
        print("Finding...")
    i += 1
# If the loop completes without finding the element
if i == len(t):
    print(f"{x} not found in the tuple.")


#  continue

# Print numbers from 1 to 10, skipping multiples of 3
num = 1
while num <= 10:
    if num % 3 == 0:  # Check if the number is a multiple of 3
        num += 1  # Increment before skipping to avoid an infinite loop
        continue  # Skip the rest of the loop for multiples of 3
    print(num)
    num += 1
