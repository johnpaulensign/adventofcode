import re

with open("./input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

def get_surrounding_numbers(lines, current_line, pos):
    numbers = []

    numbers += trace_numbers(lines[current_line], pos)

    if current_line > 0:
        numbers += trace_numbers(lines[current_line - 1], pos)

    if current_line < len(lines) - 1:
        numbers += trace_numbers(lines[current_line + 1], pos)

    return numbers

def trace_left(line, pos):
    new_pos = pos
    number = ""
    while new_pos >= 0 and line[new_pos-1:new_pos].isnumeric():
        number = line[new_pos-1:new_pos] + "" + number
        new_pos -= 1
    return number

def trace_right(line, pos):
    length = len(line)
    new_pos = pos + 1
    number = ""
    while new_pos < length and line[new_pos:new_pos+1].isnumeric():
        number += "" + line[new_pos:new_pos+1]
        new_pos += 1
    return number

def trace_numbers(line, pos):
    numbers = []
    found_center_number = False

    # found center
    if pos < len(line) and line[pos:pos+1].isnumeric():
        number = line[pos:pos+1]
        number += trace_right(line, pos)
        number = trace_left(line, pos) + number
        found_center_number = True
        numbers.append(int(number))

    # found left
    if not found_center_number and pos > 0 and line[pos-1:pos].isnumeric():
        numbers.append(int(trace_left(line, pos)))

    # found right
    if not found_center_number and pos < len(line) - 1 and line[pos+1:pos+2].isnumeric():
        numbers.append(int(trace_right(line, pos)))

    return numbers


if __name__ == "__main__":

    total_part_numbers = 0
    for i in range(0, len(lines)):

        gears = re.findall(r"\*", lines[i])
        for gear in gears:
            # find position of asterisk on line
            asterisk_pos = re.search(r"\*", lines[i])

            # replace value so it isn't found again
            lines[i] = lines[i].replace("*",  "!", 1)

            numbers = get_surrounding_numbers(lines, i, asterisk_pos.start())

            if len(numbers) == 2:
                total_part_numbers += numbers[0] * numbers[1]

    print(f"Total part numbers: {total_part_numbers}")