# ANSI Colors
ORANGE = "\033[38;5;208m"
WHITE = "\033[97m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[1m"

rows = 9

for i in range(rows):
    s = ""

    # S 
    s += ORANGE + BOLD
    for j in range(rows):
        if i == 0 or i == rows//2 or i == rows-1:
            s += "* "
        elif j == 0 and i < rows//2:
            s += "* "
        elif j == rows-1 and i > rows//2:
            s += "* "
        else:
            s += "  "
    s += RESET + "   "

    # H 
    s += ORANGE + BOLD
    for j in range(rows):
        if j == 0 or j == rows-1 or i == rows//2:
            s += "* "
        else:
            s += "  "
    s += RESET + "   "

    # A 
    s += WHITE + BOLD
    for j in range(rows):
        if i == 0 and j > 0 and j < rows-1:
            s += "* "
        elif (j == 0 or j == rows-1) and i != 0:
            s += "* "
        elif i == rows//2:
            s += "* "
        else:
            s += "  "
    s += RESET + "   "

    # N 
    s += BLUE + BOLD
    for j in range(rows):
        if j == 0 or j == rows-1 or j == i:
            s += "* "
        else:
            s += "  "
    s += RESET + "   "

    # N 
    s += GREEN + BOLD
    for j in range(rows):
        if j == 0 or j == rows-1 or j == i:
            s += "* "
        else:
            s += "  "
    s += RESET + "   "

    # U 
    s += GREEN + BOLD
    for j in range(rows):
        if (j == 0 or j == rows-1) and i != rows-1:
            s += "* "
        elif i == rows-1 and 0 < j < rows-1:
            s += "* "
        else:
            s += "  "
    s += RESET

    print(s)
