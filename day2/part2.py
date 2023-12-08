import puzzle_input

games = puzzle_input.games

# Return example
#
# {
#   max: {
#     red: 1, blue: 1, green: 1
#   },
#   draws: [
#     {
#       red: 1, blue: 1, green: 1
#     }, {
#       red: 1, blue: 1, green: 1
#     }
#   ]
# }


def parse_game(game):
    new_game = {
        "max": {
            "red": 0, "blue": 0, "green": 0
        },
        "draws": []
    }

    for draw in game:
        new_draw = parse_draw(draw)
        if new_game["max"]["red"] < new_draw["red"]:
            new_game["max"]["red"] = new_draw["red"]

        if new_game["max"]["blue"] < new_draw["blue"]:
            new_game["max"]["blue"] = new_draw["blue"]

        if new_game["max"]["green"] < new_draw["green"]:
            new_game["max"]["green"] = new_draw["green"]
        new_game["draws"].append(new_draw)

    return new_game


# Return example
#
# {
#   red: 1, blue: 1, green: 1
# }
def parse_draw(draw):
    new_draw = draw.split(", ")
    red = 0
    green = 0
    blue = 0
    for color in new_draw:
        if "red" in color:
            red = int(color.replace(" red", ""))
        if "blue" in color:
            blue = int(color.replace(" blue", ""))
        if "green" in color:
            green = int(color.replace(" green", ""))
    return {"red": red, "blue": blue, "green": green}


def get_power(parsed_game):
    return parsed_game["max"]["red"] * parsed_game["max"]["green"] * parsed_game["max"]["blue"]


if __name__ == "__main__":
    total_power = 0
    for game in games:
        parsed_game = parse_game(games[game])
        total_power += get_power(parsed_game)

    print(f"Total power of game IDs: {total_power}")
