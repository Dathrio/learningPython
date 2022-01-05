the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}
            
def print_Board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

"""def win_check(board, last_move):
    if (board['top-L'] == 'X' or  board['top-L'] == board['top-M'] and board['top-L'] == board['top-R'] 
    or board['mid-L'] == board['mid-M'] and board['mid-L'] == board['mid-R']
    or board['bot-L'] == board['bot-M'] and board['bot-L'] == board['bot-R']
    or board['top-L'] == board['mid-L'] and board['mid-L'] == board['bot-L']
    or board['top-M'] == board['mid-M'] and board['mid-M'] == board['bot-M']
    or board['top-R'] == board['mid-R'] and board['bot-R'] == board['mid-R']
    or board['top-L'] == board['mid-M'] and board['mid-M'] == board['bot-R']
    or board['bot-L'] == board['mid-M'] and board['mid-M'] == board['top-R']):
        print_Board(the_board)
        print('Player ' + last_move + ' won!')
        return True
   """     

turn = 'X'
for i in range(9):
    print_Board(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_Board(the_board)