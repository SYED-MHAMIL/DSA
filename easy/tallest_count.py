numbers = [5,4,6,2,6]

tallest = numbers[0]
count = 1

for num in numbers[1:]:
    if num > tallest:
        tallest = num
        count = 1
    elif num == tallest:
        count += 1

print("Tallest number:", tallest)
print("Count:", count)
