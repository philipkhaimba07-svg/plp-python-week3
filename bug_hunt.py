 Goal: add up the numbers 1 to 5. Expected total: 15.
 BUG: range(1, 5) stops at 4, so 5 is never added.
 The program runs with no error but prints 10 instead of 15.
 FIX: use range(1, 6).

total = 0
for n in range(1, 6):
    total += n
print("Total:", total)

 While loop: it stops when count reaches 0,
 because the condition count > 0 becomes False.
count = 3
while count > 0:
    print(count)
    count -= 1
