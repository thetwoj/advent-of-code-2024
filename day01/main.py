# Playing with Github Copilot, it generated >90% of this file based on my prompts

def read_file_lines():
    file_path = "day01/input"
    lines = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return lines

def split_string(string):
    split_result = string.split()
    if len(split_result) >= 2:
        return int(split_result[0]), int(split_result[1])
    else:
        return None

def find_absolute_difference(a, b):
    return abs(a - b)

def main():
    lines = read_file_lines()
    # Add your code here to process the lines or perform other operations
    first_values = []
    second_values = []
    second_counts = {}

    for line in lines:
        result = split_string(line)
        if result is not None:
            first_value, second_value = result
            first_values.append(first_value)
            second_values.append(second_value)

            # Also generate dict of occurrence counts for
            # the part 2 portion of day 1
            if second_value not in second_counts:
                second_counts[second_value] = 1
            else:
                second_counts[second_value] += 1

    first_values.sort()
    second_values.sort()

    # Part 1
    total_difference = 0
    for first, second in zip(first_values, second_values):
        difference = find_absolute_difference(first, second)
        total_difference += difference
    print(f"Part 1: {total_difference}")

    # Part 2
    total_difference = 0
    for index, value in enumerate(first_values):
        if value not in second_counts:
            continue
        difference = value * second_counts[value]
        total_difference += difference
    print(f"Part 2: {total_difference}")

if __name__ == "__main__":
    main()