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
spaces = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
open_spaces = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
list_rows = [["   ", "|", "   ", "|", "   "], ["   ", "|", "   ", "|", "   "], ["   ", "|", "   ", "|", "   "]]
three_in_row = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"], ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"], ["a1", "b2", "c3"], ["a3", "b2", "c1"]]
spots_x = []
spots_o = []

# choosing empty square
def choose_box():
    global open_spaces
    uinput = input('Choose a spot- a, b, or c for the column, and 1, 2, or 3 for the row (e.g., a1 for the top left corner, b3 for the bottom middle square), or type "end" to end the game: ').lower()
    print()
    if uinput in open_spaces:
        open_spaces.remove(uinput)
        return uinput
    elif uinput == "end":
        return uinput
    else: 
        return choose_box()

def gameover():
    end = False
    for combo in three_in_row:
        score_x = 0
        score_o = 0
        for spot in combo:
            if spot in spots_x: score_x+=1
            elif spot in spots_o: score_o +=1
        if score_x==3: 
            print("x wins!")
            end = True
        elif score_o ==3:
            print("o wins!")
            end = True
    if len(open_spaces) == 0: 
        print("tie!")
        end = True
    return end
                                                                                                                                                                              
def column(spot):
    if "a" in spot: return 0
    elif "b" in spot: return 2
    else: return 4
    # return when(spot[0]):
        
# prints the board
def print_board():
    print("  a   b   c")
    first = True
    for index, element in enumerate(list_rows, start =0):
        if first:
            first = False
        else: 
            print(sep)
        print(str(index+1)+''.join(element))

def place_marker(spot, mark):
    # replace a b or c index w mark
    row = list_rows[int(spot[1])-1]
    row[column(spot)] = mark
    list_rows[int(spot[1])-1] = row
    return list_rows

def reset():
    global open_spaces
    global list_rows
    global spots_o
    global spots_x
    open_spaces = spaces
    list_rows = [["   ", "|", "   ", "|", "   "], ["   ", "|", "   ", "|", "   "], ["   ", "|", "   ", "|", "   "]]
    spots_x = []
    spots_o = []
def again():  
    again = input("Play again? (Y)es/(N)o: ")
    if again.lower()=="y" or again.lower() == "yes": 
        reset()
        print()
        main()
    elif again.lower()=="n" or again.lower() =="no":
        return "ended"
    else: return again() 
turns = 0
marker = "x"
def main():
    print("   a   b   c", "\n", "1"+rows, "\n", sep, "\n", "2"+rows, "\n", sep, "\n", "3"+rows+"\n")
    def game():
        global turns
        spot = choose_box()
        if turns%2==0:
            marker =" x "
            spots_x.append(spot)
        else:
            marker = " o "
            spots_o.append(spot)
        if spot!= "end":
            place_marker(spot, marker)
            print_board()
            print()
            over = gameover()
            turns+=1
            if over == False: game()
            else: again()
        else: return "ended game"
    game()
main()