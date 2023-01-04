table = ["   " for i in range(9)]
x = 0
status = False
draw = False
def print_table():
    row1 = "|{}|{}|{}|".format(table[0], table[1], table[2])
    row2 = "|{}|{}|{}|".format(table[3], table[4], table[5])
    row3 = "|{}|{}|{}|".format(table[6], table[7], table[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def win(number):
    if number == 0:
        sign = " X "
    elif number == 1:
        sign = " O "
    if(table[0] == sign and table[1] == sign and table[2] == sign or \
       table[3] == sign and table[4] == sign and table[5] == sign or \
       table[6] == sign and table[7] == sign and table[8] == sign or \
       table[0] == sign and table[3] == sign and table[6] == sign or \
       table[1] == sign and table[4] == sign and table[7] == sign or \
       table[2] == sign and table[5] == sign and table[8] == sign or \
       table[0] == sign and table[4] == sign and table[8] == sign or \
       table[2] == sign and table[4] == sign and table[6] == sign):
        return True  
print_table()
while True:
    for i in range(2):
        x += 1
        if status == True:
            break
        choice = int(input("Player {}: Enter your move (1-9): ".format(i + 1)).strip())            
        while table[choice - 1] == " X " or table[choice - 1] == " O " :
            print("Position already occupied.")
            choice = int(input("Player {}: Enter your move (1-9): ".format(i + 1)).strip())
        if i == 0:
            table[choice - 1] = " X "
        elif i == 1:
            table[choice - 1] = " O "
        print_table()
        if win(i):
            print("Player {} wins!".format(i + 1))
            status = True
        elif x == 9 and win(i):
            print("Player {} wins!".format(i + 1))
            status = True
        elif x == 9:                  
            print("The game ended in a draw")
            draw = True
            break
    if draw or status:
        break
    



    
            
            
        
        
    
    
