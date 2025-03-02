from Enum import Cell

class Board:
    def __init__(self):
        self.__grid = [[Cell.EMPTY for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.__grid:
            row_values = []
            for cell in row:
                row_values.append(cell.value)
            print(" | ".join(row_values))
            print("-" * 9)

    def set_cell(self,row,col,cell:Cell):
        if self.__grid[row][col] == Cell.EMPTY:
            self.__grid[row][col]= cell
            return True
        else:
            return False

    def check_winner(self):
        for row in self.__grid:
            if row[0] == row[1] == row[2] != Cell.EMPTY:
                return row[0]
        for col in range(3):
            if self.__grid[0][col] == self.__grid[1][col] == self.__grid[2][col] != Cell.EMPTY:
                return self.__grid[0][col]
        if self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] != Cell.EMPTY:
            return self.__grid[0][0]
        if self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0] != Cell.EMPTY:
            return self.__grid[0][2]
        return None

    def is_full(self):
        for row in self.__grid:
            for cell in row:
                if cell == Cell.EMPTY:
                    return False
        return True