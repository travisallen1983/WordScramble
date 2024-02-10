def length_one(input_string) -> list:
    output_list = [input_string]
    return output_list


# Iterate over all possible instances of the input string.
# The input_string resets at the end of the loop.
# This makes the last letter first and shifts all other letters one to the right.
def length_two(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        output_string = input_string[0] + input_string[1]
        output_list.append(output_string)
        input_string = input_string[-1] + input_string[0]
        i += 1
    return output_list


# Iterate over all possible instances of the input string.
# Calls lower version of the function to break down the task into smaller pieces
# The input_string resets at the end of the loop.
# This makes the last letter first and shifts all other letters one to the right.
def length_three(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_two(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = input_string[-1] + input_string[0] + input_string[1]
        i += 1
    return output_list


def length_four(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_three(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = (input_string[-1] + input_string[0]
                        + input_string[1] + input_string[2])
        i += 1
    return output_list


def length_five(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_four(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = (input_string[-1] + input_string[0] + input_string[1]
                        + input_string[2] + input_string[3])
        i += 1
    return output_list


def length_six(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_five(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = (input_string[-1] + input_string[0] + input_string[1]
                        + input_string[2] + input_string[3] + input_string[4])
        i += 1
    return output_list


def length_seven(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_six(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = (input_string[-1] + input_string[0] + input_string[1]
                        + input_string[2] + input_string[3] + input_string[4]
                        + input_string[5])
        i += 1
    return output_list


def length_eight(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_seven(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = (input_string[-1] + input_string[0] + input_string[1]
                        + input_string[2] + input_string[3] + input_string[4]
                        + input_string[5] + input_string[6])
        i += 1
    return output_list


def length_nine(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_eight(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = (input_string[-1] + input_string[0] + input_string[1]
                        + input_string[2] + input_string[3] + input_string[4]
                        + input_string[5] + input_string[6] + input_string[7])
        i += 1
    return output_list


def length_ten(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_nine(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = (input_string[-1] + input_string[0] + input_string[1]
                        + input_string[2] + input_string[3] + input_string[4]
                        + input_string[5] + input_string[6] + input_string[7]
                        + input_string[8])
        i += 1
    return output_list


def length_eleven(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_ten(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = (input_string[-1] + input_string[0] + input_string[1]
                        + input_string[2] + input_string[3] + input_string[4]
                        + input_string[5] + input_string[6] + input_string[7]
                        + input_string[8] + input_string[9])
        i += 1
    return output_list


def length_twelve(input_string, input_string_length) -> list:
    output_list = []
    for i in range(0, input_string_length):
        append_strings = length_eleven(input_string[1:], input_string_length - 1)
        j_range = 1
        for k in range(1, input_string_length):
            j_range = j_range * k
        for j in range(0, j_range):
            output_string = input_string[0] + append_strings[j]
            output_list.append(output_string)
        input_string = (input_string[-1] + input_string[0] + input_string[1]
                        + input_string[2] + input_string[3] + input_string[4]
                        + input_string[5] + input_string[6] + input_string[7]
                        + input_string[8] + input_string[9] + input_string[10])
        i += 1
    return output_list


def word_scramble(user_input):
    input_length = len(user_input)

    if input_length == 1:
        output_list = length_one(user_input)
    elif input_length == 2:
        output_list = length_two(user_input, input_length)
    elif input_length == 3:
        output_list = length_three(user_input, input_length)
    elif input_length == 4:
        output_list = length_four(user_input, input_length)
    elif input_length == 5:
        output_list = length_five(user_input, input_length)
    elif input_length == 6:
        output_list = length_six(user_input, input_length)
    elif input_length == 7:
        output_list = length_seven(user_input, input_length)
    elif input_length == 8:
        output_list = length_eight(user_input, input_length)
    elif input_length == 9:
        output_list = length_nine(user_input, input_length)
    elif input_length == 10:
        output_list = length_ten(user_input, input_length)
    elif input_length == 11:
        output_list = length_eleven(user_input, input_length)
    elif input_length == 12:
        output_list = length_twelve(user_input, input_length)
    else:
        output_list = []

    return output_list


def main():
    user_input = 'PYTHONISTA'
    word_output = word_scramble(user_input)
    i = 1
    for word in word_output:
        print(str(i) + ": " + word)
        i += 1


if __name__ == '__main__':
    main()
