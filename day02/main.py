# Playing with Github Copilot, it generated >90% of this file based on my prompts

def read_file_lines():
    file_path = "day02/input"
    lines = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return lines

def main():
    pass
    # Part 1
    # Part 2

if __name__ == "__main__":
    main()