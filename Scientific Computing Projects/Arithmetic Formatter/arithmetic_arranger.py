import re

# Finds the width of the longest number in a single problem and adds two spaces
def calculate_width(problem):
    max = 0
    for elem in problem.split():
        if len(elem) > max:
            max = len(elem)
    
    return max + 2


def arithmetic_arranger(problems, calculate = False):
    if len(problems) > 5:
        return "Error: Too many problems."

    lines = []

    for i in range(4):
        # Initialising the lines to empty strings
        lines.append("")

    for problem in problems:
        width = calculate_width(problem)

        pieces = problem.split()
        if pieces[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if len(max(problem.split())) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not re.search("^[0-9]{1,4}$", pieces[0]) or not re.search("^[0-9]{1,4}$", pieces[2]):
            return "Error: Numbers must only contain digits."

        lines[0] += pieces[0].rjust(width + 4)

        lines[1] += " " * 4
        lines[1] += pieces[1]
        lines[1] += pieces[2].rjust(width - 1)

        lines[2] += " " * 4
        lines[2] += "-" * width

        if calculate:
            if(pieces[1] == "+"):
                lines[3] += str(int(pieces[0]) + int(pieces[2])).rjust(width + 4)
            else:  # We have already checked for any other operation not being present
                lines[3] += str(int(pieces[0]) - int(pieces[2])).rjust(width + 4)

    # Remove 4 spaces at the beginning of each line before joining
    for i in range(4):
        lines[i] = lines[i][4:]

    # Joins the lines and returns the block of text
    return "\n".join(tuple(lines))
