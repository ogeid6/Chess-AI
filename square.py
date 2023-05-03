
class Square:

    def __init__(self, row, col, piece=None):

        self.row = row
        self.col = col
        self.piece = piece  

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        return self.piece != None 
    
    def esemty(self):
        return not self.has_piece()
    
    def has_squad_piece(self, color):
        return self.has_piece() and self.piece.color == color

    
    def has_opps_piece(self, color):
        return self.has_piece() and self.piece.color != color
    
    def esemty_or_opps(self, color):
        return self.esemty() or self.has_opps_piece(color)


    @staticmethod
    def within_range(*args): 
        for arg in args:
            if arg<0 or arg > 7:
                return False
            
        return True

     