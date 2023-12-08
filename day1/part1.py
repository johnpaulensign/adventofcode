import input

total_value = 0
print(f"Total value: {total_value}")
print(f"words {input.words}")
for word in input.words:
    print(f"word {word}")
    first_number = -1
    second_number = -1
    for letter in word:
        try:
            num = int(letter)
            if first_number == -1:
                first_number = num
            second_number = num
        except:
            pass

    if first_number == -1:
        first_number = 0
    if second_number == -1:
        second_number = first_number

    print(f"Adding {str(first_number) + str(second_number)}")
    total_value += int(str(first_number) + str(second_number))

print(f"Total value: {total_value}")
