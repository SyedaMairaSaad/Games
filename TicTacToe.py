def printBoard(xScores,oScores):
    value_0='X' if xScores[0]=='X' else('O' if oScores[0]=='O' else 0)
    value_1='X' if xScores[1]=='X' else('O' if oScores[1]=='O' else 1)
    value_2='X' if xScores[2]=='X' else('O' if oScores[2]=='O' else 2)
    value_3='X' if xScores[3]=='X' else('O' if oScores[3]=='O' else 3)
    value_4='X' if xScores[4]=='X' else('O' if oScores[4]=='O' else 4)
    value_5='X' if xScores[5]=='X' else('O' if oScores[5]=='O' else 5)
    value_6='X' if xScores[6]=='X' else('O' if oScores[6]=='O' else 6)
    value_7='X' if xScores[7]=='X' else('O' if oScores[7]=='O' else 7)
    value_8='X' if xScores[8]=='X' else('O' if oScores[8]=='O' else 8)
    print(f'  {value_0}  |  {value_1}  |  {value_2}')
    print(f'  ___|_____|___')
    print(f'  {value_3}  |  {value_4}  |  {value_5}')
    print(f'  ___|_____|___')
    print(f'  {value_6}  |  {value_7}  |  {value_8}')
    print(f'     |     |   ')

def checkWinner(xScores,oScores):
    winner=[[0,1,2],[3,4,5],[6,7,8],[1,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    x_index=[i for i, e in enumerate(xScores) if e == 'X']
    o_index=[i for i, e in enumerate(oScores) if e == 'O']
    for z in range(0,len(winner)):
        if len(set(winner[z]).intersection(x_index)) ==3:
            return 'X'
        if len(set(winner[z]).intersection(o_index)) ==3:
            return 'O'     
                
        
xScores=[0,0,0,0,0,0,0,0,0]
oScores=[0,0,0,0,0,0,0,0,0]
turn=0
while(True):
    printBoard(xScores,oScores)
    if turn==0:
        print('Its x turn')
        inp=int(input('Input Position: '))
        xScores[inp]='X'
    else:
        print('Its o turn')
        inp=int(input('Input Position: '))
        oScores[inp]='O'
    turn=1-turn
    winner=checkWinner(xScores,oScores)
    if winner is not None:
        print('winner',winner)
        break
    
        
    