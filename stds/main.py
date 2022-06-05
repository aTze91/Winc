# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here
import fileinput
import sys
def main():
    # TODO: read text from stdin

    # TODO: Filter character given as an argument from the text
    filtered_lines = []
    filtered_count = 0
    for line in sys.stdin.readlines():
        for letter in line:
            if letter == sys.argv[1]:
                filtered_count += 1
        filtered_line = line.replace(sys.argv[1],'')
        filtered_lines.append(filtered_line)
    # TODO: Print the result to stdout
    for line in filtered_lines:
        sys.stdout.write(line)
    # TODO: Print the total number of removed characters to stderr
    sys.stderr.write(str(filtered_count))


if __name__ == "__main__":
    main()
