while True:
    def sum(a, b, c):
        return a + b + c


    count = 10


    def printBoard(xState, Ostate, count):
        zero = "X" if xState[0] else ('O' if Ostate[0] else 0)
        one = 'X' if xState[1] else ('O' if Ostate[1] else 1)
        two = 'X' if xState[2] else ('O' if Ostate[2] else 2)
        three = 'X' if xState[3] else ('O' if Ostate[3] else 3)
        four = 'X' if xState[4] else ('O' if Ostate[4] else 4)
        five = 'X' if xState[5] else ('O' if Ostate[5] else 5)
        six = 'X' if xState[6] else ('O' if Ostate[6] else 6)
        seven = 'X' if xState[7] else ('O' if Ostate[7] else 7)
        eight = 'X' if xState[8] else ('O' if Ostate[8] else 8)
        print(f'    {zero} | {one} | {two} ')
        print(f'    --|---|---')
        print(f'    {three} | {four} | {five} ')
        print(f'    --|---|---')
        print(f'    {six} | {seven} | {eight} ')
        return count - 1


    def checkwin(xstate, ostate):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
                print('X won the game')
                return 1
            if sum(ostate[win[0]], ostate[win[1]], ostate[win[2]]) == 3:
                print('O Won the game ')
                return 0
        return -1


    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Ostate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    while True:
        count = printBoard(xState, Ostate, count)
        if count == 0:
            print('Match Tied')
            break
        if turn == 1:
            print("X's Chance")
            value = int(input('Enter The Value from 0 to 8: '))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input('Enter The Value from 0 to 8: '))
            Ostate[value] = 1
        cw = checkwin(xState, Ostate)
        if cw != -1:
            printBoard(xState, Ostate, count)
            print('Game Over')
            break

        turn = 1 - turn

    n = input()
    if n.lower()=='br':
        break