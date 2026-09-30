scores = [85, 72, 90, 45, 68, 77, 55]

total = 0
count_pass = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    if grade != "F":
        count_pass += 1

    total += score
    print(f"Score {score}: {grade}")

average = total / len(scores)
print(f"Average: {average:.1f}")
print(f"Passed: {count_pass} of {len(scores)}")
