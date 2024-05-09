import string

STAR_CHAR = "*"
SPACE_CHAR = " "


def print_start_series(count: int) -> None:
    # count -> line count
    # in each line there are 2 parts
    # count -> count of starts in each part of the line

    for line_number in range(1, count + 1):
        star_text = ""
        space_text = ""

        star_text = STAR_CHAR * line_number
        space_text = SPACE_CHAR * (count - line_number) * 2

        line_text = star_text + space_text + star_text
        print(line_text)


# print_start_series(5)
#
# **      **   n - 2 = 3 -> 6
# ***    ***   n - 3 = 2 -> 4
# ****  ****   n - 4 = 1 -> 2
# **********   n = 5

ALPHABET = list(string.ascii_lowercase)


def build_palydrom(character: str) -> None:
    character_index = -1

    # find character index in ordered alphabet
    for index, char in enumerate(ALPHABET):
        if char == character:
            character_index = index
            break

    # return error message if character doesn't exist
    if character_index == -1:
        return "the character is invalid"

    for line_number in range(character_index + 1):
        palyndrom = ""

        middle_char = ALPHABET[line_number]
        left_side = ""
        right_side = ""

        # build left side
        for index in range(line_number):
            left_side += ALPHABET[index]

        #build right side
        for index, char in enumerate(left_side):
            right_side += left_side[len(left_side) - index - 1]

        palyndrom = left_side + middle_char + right_side
        print(palyndrom)


# build_palydrom("j")

def print_parts_series(lines_count: int, parts_count: int) -> None:
    #n = lines count
    #k = parts count
      # part -> n numbers + @

    for line in range(lines_count):
        line_text = ""

        for part in range(parts_count):
            part_text = ""

            for number in range(line, lines_count + line):
                #line
                if number < lines_count:
                    part_text += str(number)
                else:
                    part_text += str(number - lines_count)


            part_text += "@"
            line_text += part_text

        print(line_text)

# print_parts_series(10, 3)

HASH_TAG_SYMBOL = "#"
DOLLAR_SYMBOL = "$"
def print_symbols_series(lines_count: int, parts_count: int)-> None:

    for line in range(1, lines_count + 1):
        line_text = ""

        for part in range(parts_count):
            part_text = ""

            for symbol in range(1, lines_count + 1):

                if line % 2 == 0:
                    if symbol <= line:
                        part_text += HASH_TAG_SYMBOL
                    else:
                        part_text += DOLLAR_SYMBOL
                else:
                    if symbol <= line:
                        part_text += DOLLAR_SYMBOL
                    else:
                        part_text += HASH_TAG_SYMBOL

            part_text += "@"
            line_text += part_text

        print(line_text)

print_symbols_series(5, 4)