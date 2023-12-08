import re
import sys
import puzzle_input

with open("./puzzle_input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

total_part_numbers = 0
part_number_counts = {}
for i in range(0, len(lines)):
    parts = re.findall(r"[0-9]+", lines[i])
    for part in parts:
        pos = re.search(part, lines[i])

        pos_start = pos.start() - 1 if pos.start() > 0 else 0
        pos_end = pos.end() + 1 if pos.end() < len(lines[i]) else pos.end()

        top = ""
        mid = lines[i][pos_start:pos_end]
        bot = ""

        if i > 0:
            top = lines[i - 1][pos_start:pos_end]

        if i < len(lines) - 1:
            bot = lines[i + 1][pos_start:pos_end]

        symbols_top = re.findall(r"[^0-9\.]", top)
        symbols_mid = re.findall(r"[^0-9\.]", mid)
        symbols_bot = re.findall(r"[^0-9\.]", bot)

        if re.findall(r"[^0-9\.]", top) or re.findall(r"[^0-9\.]", mid) or re.findall(r"[^0-9\.]", bot):
            total_part_numbers += int(part)

        lines[i] = lines[i].replace(part, "".ljust(len(part), 'X'), 1)


print(f"Total part numbers: {total_part_numbers}")
