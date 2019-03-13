"""
Koc University, Turkey
KOLT Python Certificate Program
Spring 2019 - Assignment 1
Created by @ahmetuysal
"""
try:
    print('Welcome to two player Connect Four game!')
    print('This a two player game played on a seven-column, six-row board.')

    # empty squares are denoted with *
    board = [
        ['*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*']]

    players = []
    player_pieces = []

    # Take player names
    players.append(input('Please enter first player\'s name:'))
    players.append(input('Please enter second player\'s name:'))

    # Take player piece symbols
    # Symbols need be unique and have length 1 
    # They should also be different than '*'
    print('\'*\' symbol is reserved to denote empty squares.')
    for player in players:
        piece = input('Please enter the symbol you want to use as your piece {}:'.format(player))
        while piece == '*' or len(piece) != 1 or piece in player_pieces:
            piece = input('Please enter an unused symbol with length 1 {}:'.format(player))
        player_pieces.append(piece)

    # Print the initial board
    for row in board[::-1]:
        print(' '.join(row))
    print(' '.join([str(num) for num in range(7)]))

    # Loop for game
    for move_counter in range(42):
        # Take user input for column_no   
        print('Turn is on {}'.format(players[move_counter%len(players)]))

        column_no = input('Enter the column number (0-6):')
        # Check whether input is a number
        while not str.isnumeric(column_no):
            column_no = input('Please enter a valid number')
        # Cast column_no to int
        column_no = int(column_no)

        # Check whether this is a valid move
        # It needs to be an integer, hint: use str.isnumeric()
        # It needs to be in range [0, 6] inclusive
        # And the selected column cannot be full
        # You need to ask for new column_no until user enters a valid one
        valid = False
        while not valid:
            # Check the range
            while column_no < 0 or column_no > 6:
                column_no = input('Please enter a number (0-6):')
                # Check whether input is a number
                while not str.isnumeric(column_no):
                    column_no = input('Please enter a valid number')
                # Cast column_no to int
                column_no = int(column_no)

            # Check whether the column is full
            row_no = 0
            while row_no < 6:
                if board[row_no][column_no] != '*':
                    row_no += 1
                else:
                    valid = True
                    break
            # this else block only runs if condition on while loop becomes false
            # it is not executed if loop is terminated by a break statement
            else:
                column_no = input('Please select a column that is not full:')
                # Check whether input is a number
                while not str.isnumeric(column_no):
                    column_no = input('Please enter a valid number')
                # Cast column_no to int
                column_no = int(column_no)

        # Play the move
        player_piece = player_pieces[move_counter%len(players)]
        board[row_no][column_no] = player_piece

        # Print the current board
        for row in board[::-1]:
            print(' '.join(row))
        print(' '.join([str(num) for num in range(7)]))

        # Check whether the game is finished
        # We know that piece is added to row:row_no, column:column_no
        game_ended = False
        # Checking the row
        piece_in_a_row = 0
        for loc in board[row_no]:
            if loc == player_piece:
                piece_in_a_row += 1
            else:
                piece_in_a_row = 0
            
            if piece_in_a_row == 4:
                game_ended = True
                break  

        # Checking the column
        piece_in_a_row = 0
        for loc_row in range(6):
            if board[loc_row][column_no] == player_piece:
                piece_in_a_row += 1
            else:
                piece_in_a_row = 0
            
            if piece_in_a_row == 4:
                game_ended = True
                break  

        # Checking the cross \ (assuming top-left corner is 0,0)
        piece_in_a_row = 0
        # checking just 7 squares around newly added piece is enough
        for i in range(-3, 4):
            loc_row = row_no + i
            loc_col = column_no + i
            # if square we are checking is out of bounds
            if  loc_row < 0 or loc_row > 5 or loc_col < 0 or loc_col > 6:
                piece_in_a_row = 0
                continue
            elif board[loc_row][loc_col] == player_piece:
                piece_in_a_row += 1
            else:
                piece_in_a_row = 0

            if piece_in_a_row == 4:
                game_ended = True
                break  
        
        # Checking the cross / (assuming top-left corner is 0,0)
        piece_in_a_row = 0
        # checking just 7 squares around newly added piece is enough
        for i in range(-3, 4):
            loc_row = row_no + i
            loc_col = column_no - i
            # if square we are checking is out of bounds
            if  loc_row < 0 or loc_row > 5 or loc_col < 0 or loc_col > 6:
                piece_in_a_row = 0
                continue
            elif board[loc_row][loc_col] == player_piece:
                piece_in_a_row += 1
            else:
                piece_in_a_row = 0

            if piece_in_a_row == 4:
                game_ended = True
                break  

        # Print the winner and number of moves if game is finished
        # The game should stop at this point if game is finished
        if game_ended:
            print('Congratulations {} you won the game in {} moves.'.format(players[move_counter%len(players)], move_counter + 1))
            break
    # this else block only runs if condition on while loop becomes false
    # it is not executed if loop is terminated by a break statement
    # i.e when all 42 moves are played without a break statement
    else:
        print('There no other legal moves, game is ended in a draw.')
except EOFError:
    print('\n\nUnexpected End Of File error. Program is terminating.')
input('Game is over. Press enter to exit...')