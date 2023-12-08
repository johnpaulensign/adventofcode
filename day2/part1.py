import puzzle_input

games = puzzle_input.games

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

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


def check_game(parsed_game, max_red, max_green, max_blue):
    if parsed_game["max"]["red"] > max_red or parsed_game["max"]["green"] > max_green or parsed_game["max"]["blue"] > max_blue:
        return False
    return True


if __name__ == "__main__":
    total_value = 0
    valid_count = 0
    for game in games:
        parsed_game = parse_game(games[game])
        if check_game(parsed_game, MAX_RED, MAX_GREEN, MAX_BLUE):
            print(f"Game: {game} - {parsed_game['max']} - Valid")
            total_value += game
            valid_count += 1

    print(f"Number of valid games: {valid_count}")
    print(f"Total value of game IDs: {total_value}")
