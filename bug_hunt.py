count = 1
total = 0

# BUG: The while line had no colon, causing a SyntaxError. I added the colon.
# BUG: count < 5 stopped before adding 5, so the total was 10 with no error. I changed it to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Joining a string and a number with + caused a TypeError. I used str(total).
print("Sum of 1 to 5 is: " + str(total))
