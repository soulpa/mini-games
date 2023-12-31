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
sep = "-----------"
x = " x "
o = " o "
rows = ''.join(row)
print(" "+rows,"\n",sep,"\n",rows,"\n",sep, "\n",rows)
spaces = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
open_spaces = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

# choosing empty square
def choose_box():
    uinput = input("choose spot: ").lower()
    if uinput in open_spaces:
        print(uinput)
        open_spaces.remove(uinput)
        print(open_spaces, spaces)
        return uinput
    else: choose_box()

e = choose_box()
print(e)
