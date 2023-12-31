# a, b, or c for column
# 1, 2, or 3 for row

# ex-  empty board:
#   a   b   c
# 1    |   |   
#   -----------
# 2    |   |
#   -----------
# 3    |   |

row = ["   ", "|", "   ", "|", "   "]
sep = " -----------"
x = " x "
o = " o "
rows = ''.join(row)
print("   a   b   c", "\n", "1"+rows, "\n", sep, "\n", "2"+rows, "\n", sep, "\n", "3"+rows)
spaces = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
open_spaces = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]


# choosing empty square
def choose_box():
    uinput = input('Choose a spot- a, b, or c for the column, and 1, 2, or 3 for the row (e.g., a1 for the top left corner, b3 for the bottom middle square) or type "end" to end the game.: ').lower()
    if uinput in open_spaces:
        open_spaces.remove(uinput)
        return uinput
    elif uinput == "end":
        return uinput
    else: 
        return choose_box()

list_rows = [["   ", "|", "   ", "|", "   "], ["   ", "|", "   ", "|", "   "], ["   ", "|", "   ", "|", "   "]]
def place_markers(spot):
