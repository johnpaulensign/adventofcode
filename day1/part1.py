import input

total_value = 0
for word in input.words:
    first_number = -1
    second_number = -1
    msgs = [word]

    for letter in word:
        try:
            num = int(letter)
            msgs.append(f"{letter}")
            if first_number == -1:
                first_number = num
            second_number = num
        except:
            pass

    if first_number == -1:
        first_number = 0
    if second_number == -1:
        second_number = first_number

    msgs.append(f"Value: {str(first_number) + str(second_number)}")
    print(" - ".join(msgs))
    total_value += int(str(first_number) + str(second_number))

print(f"Total value: {total_value}")
