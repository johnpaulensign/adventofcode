import re

with open("./input.txt", "r") as file:
    # with open("./test.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()


def get_surrounding(pos, current_line):

    pos_start = pos.start() - 3 if pos.start() > 0 else 0
    pos_end = pos.end() + \
        3 if pos.end() < len(lines[current_line]) else pos.end()

    top = ""
    mid = lines[current_line][pos_start:pos_end]
    bot = ""

    if current_line > 0:
        top = lines[current_line - 1][pos_start:pos_end]

    if current_line < len(lines) - 1:
        bot = lines[current_line + 1][pos_start:pos_end]

    return (top, mid, bot)


def get_touching_gears():

    if re.match(r"[0-9]+", ):
        pass
    if re.match(r"[0-9]", mid):
        pass
    if re.match(r"[0-9]", bot):
        pass


total_part_numbers = 0
for i in range(0, len(lines)):

    gears = re.findall(r"\*", lines[i])
    # print(f"{gears}")
    for gear in gears:
        first_number = None
        second_number = None
        pos = re.search(r"\*", lines[i])
        # print(lines[i])
        # print(pos)
        lines[i] = lines[i].replace("*",  "!", 1)
        # print(pos)
        # print("\n".join(get_surrounding(pos, i)))
        (top, mid, bot) = get_surrounding(pos, i)

# .55.12.
# ...*...
# .112...

        for found in re.findall(r"\b[0-9]+\b", top):
            length = len(re.findall(r"[0-9]+", found)[0])
            position = re.search(found, top)
            if position.start() + length >= 3 and position.end() - length <= 3:

                lines[i-1] = lines[i-1].replace(
                    found, "".ljust(len(found), "x"), 1)

                # lines[i-1] = lines[i-1][:pos.start() + position.start() - 3] + \
                #     "".ljust(len(found), "x") + \
                #     lines[i-1][pos.end() - position.end():]
                print(f"found top: {top} at {position}")
                if first_number is None:
                    first_number = int(found)
                elif second_number is None:
                    second_number = int(found)

        for found in re.findall(r"\b[0-9]+\b", mid):
            length = len(re.findall(r"[0-9]+", found)[0])
            position = re.search(found, mid)
            if position.start() <= 3 and position.end() >= 3:
                lines[i] = lines[i].replace(
                    found, "".ljust(len(found), "x"), 1)
                # lines[i] = lines[i][:pos.start() + position.start() - 3] + \
                #     "".ljust(len(found), "x") + \
                #     lines[i][pos.end() - position.end():]
                print(f"found mid: {mid} at {position}")
                if first_number is None:
                    first_number = int(found)
                elif second_number is None:
                    second_number = int(found)

        for found in re.findall(r"\b[0-9]+\b", bot):
            length = len(re.findall(r"[0-9]+", found)[0])
            position = re.search(found, bot)
            if position.start() + length >= 3 and position.end() - length <= 3:
                # lines[i+1] = lines[i+1][:pos.start() + position.start() - 3] + \
                #     "".ljust(len(found), "x") + \
                #     lines[i+1][pos.end() - position.end():]
                lines[i+1] = lines[i+1].replace(
                    found, "".ljust(len(found), "x"), 1)
                print(f"found bot: {bot} at {position}")
                if first_number is None:
                    first_number = int(found)
                elif second_number is None:
                    second_number = int(found)

        if first_number is not None and second_number is not None:
            # print(f"Found a gear: {first_number} and {second_number}")
            # print(lines[i-1])
            # print(lines[i])
            # print(lines[i+1])
            print()
            total_part_numbers += first_number * second_number
            # print(lines[i])

    # if i == 3:
    #     break
        # break
        # pos = re.search(gear, lines[i])

        # pos_start = pos.start() - 1 if pos.start() > 0 else 0
        # pos_end = pos.end() + 1 if pos.end() < len(lines[i]) else pos.end()

        # top = ""
        # mid = lines[i][pos_start:pos_end]
        # bot = ""

        # if i > 0:
        #     top = lines[i - 1][pos_start:pos_end]

        # if i < len(lines) - 1:
        #     bot = lines[i + 1][pos_start:pos_end]

        # symbols_top = re.findall(r"[^0-9\.]", top)
        # symbols_mid = re.findall(r"[^0-9\.]", mid)
        # symbols_bot = re.findall(r"[^0-9\.]", bot)

        # if re.findall(r"[^0-9\.]", top) or re.findall(r"[^0-9\.]", mid) or re.findall(r"[^0-9\.]", bot):
        #     total_part_numbers += int(part)

        # lines[i] = lines[i].replace(part, "".ljust(len(part), 'X'), 1)

print("\n".join(lines))
print(f"Total part numbers: {total_part_numbers}")


# 79909338 too low
# 77783809
# 79862885
# 39571437
# 72572988
# 10609543
# 39571437
