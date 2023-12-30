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
