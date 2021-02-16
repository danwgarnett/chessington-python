"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):

        current_square = board.find_piece(self)

        possible_moves =[]
        available_moves = []
        route_squares = []

        if self.player == Player.WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # Case 1, normal play
        possible_moves.append(direction * 1)

        # Case 2, pawn hasn't moved yet
        if current_square.row == start_row:
            possible_moves.append(2 * direction)

        # Case 3, If we are next to an opposing piece, move diagonally

        # Assemble all moves not blocked at destination or on route
        for move in possible_moves:

            destination_square = Square(current_square.row + move, current_square.col)
            move_on_board = destination_square.row in range(0,8)

            if not move_on_board:
                continue

            if move > 0:
                route_rows = range(current_square.row + 1, destination_square.row + 1)
            else:
                route_rows = range(destination_square.row, current_square.row)

            pieces_in_squares = []
            for row in route_rows:
                route_square = Square(row,destination_square.col)
                piece_in_square = board.get_piece(route_square)

                if piece_in_square != None:
                    pieces_in_squares.append(piece_in_square)

            if not pieces_in_squares and move_on_board:
                available_moves.append(destination_square)
            
        return available_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []