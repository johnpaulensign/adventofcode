import input


def get_number_from_word(letter, word):
    if "zero" in word or letter == "0":
        return 0
    if "one" in word or letter == "1":
        return 1
    if "two" in word or letter == "2":
        return 2
    if "three" in word or letter == "3":
        return 3
    if "four" in word or letter == "4":
        return 4
    if "five" in word or letter == "5":
        return 5
    if "six" in word or letter == "6":
        return 6
    if "seven" in word or letter == "7":
        return 7
    if "eight" in word or letter == "8":
        return 8
    if "nine" in word or letter == "9":
        return 9
    raise IOError(f"word '{word}' is not a number")


total_value = 0
for word in input.words:
    first_number = -1
    second_number = -1
    number = -1
    letter_word = ""
    msgs = [word]
    for letter in word:
        try:
            letter_word += letter

            number = get_number_from_word(letter, letter_word)
            msgs.append(f"{letter_word}")

            if first_number == -1:
                first_number = number

            second_number = number
            letter_word = letter
        except IOError as ex:
            pass
        except:
            letter_word += letter

    if first_number == -1:
        first_number = 0
    if second_number == -1:
        second_number = first_number

    msgs.append(f"Value: {str(first_number) + str(second_number)}")
    print(" - ".join(msgs))
    total_value += int(str(first_number) + str(second_number))

print(f"Total value: {total_value}")
