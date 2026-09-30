count = 1
total = 0

BUG: The while line had no colon at the end, which gave a SyntaxError. I added the colon.
BUG: The condition count < 5 stopped the loop before 5 was added, so the total was 10 and there was no error. I changed it to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

BUG: I tried to join a string and a number with +, which gave a TypeError. I wrapped total in str().
print("Sum of 1 to 5 is: " + str(total))
