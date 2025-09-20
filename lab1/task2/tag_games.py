import random

FIELD_SIZE = 4
EMPTY_CELL = 0


class TagGame:
    def __init__(self):
        self.playing_field = []
        self.empty_cell_coordinates = (FIELD_SIZE - 1, FIELD_SIZE - 1)
        self.create_field()

    def generate_numbers(self):
        return list(range(1, FIELD_SIZE * FIELD_SIZE)) + [EMPTY_CELL]

    def create_matrix_from_numbers(self, numbers):
        return [numbers[i:i + FIELD_SIZE] for i in range(0, len(numbers), FIELD_SIZE)]

    def create_field(self):
        numbers = self.generate_numbers()
        while True:
            random.shuffle(numbers)
            self.playing_field = self.create_matrix_from_numbers(numbers)
            self.empty_cell_coordinates = self.get_empty_cell_position()
            if self.is_solvable() and not self.is_solved():
                break

    def get_empty_cell_position(self):
        all_cells = self.get_list_from_matrix()
        index = all_cells.index(EMPTY_CELL)
        return divmod(index, FIELD_SIZE)

    def get_list_from_matrix(self):
        return [cell for row in self.playing_field for cell in row]

    def get_tiles_without_empty(self):
        return [tile for tile in self.get_list_from_matrix() if tile != EMPTY_CELL]

    def count_inversions(self):
        tiles = self.get_tiles_without_empty()
        return sum(
            1 for i, current in enumerate(tiles) for other in tiles[i + 1:] if other < current
        )

    def is_solvable(self):
        inversions = self.count_inversions()
        empty_row, _ = self.empty_cell_coordinates
        n = FIELD_SIZE 
        if n % 2 == 1:  
            return inversions % 2 == 0
        empty_row_from_bottom = n - empty_row
        if empty_row_from_bottom % 2 == 0:  
            return inversions % 2 == 1
        else:  
            return inversions % 2 == 0

    def is_solved(self):
        expected = list(range(1, FIELD_SIZE * FIELD_SIZE)) + [EMPTY_CELL]
        return self.get_list_from_matrix() == expected

    def move_cells(self, direction, steps):
        row_shift, col_shift = self.get_direction_by_input(direction)
        if row_shift is None:
            return False
        if not self.is_move_valid(row_shift, col_shift, steps):
            return False
        self.apply_shift(row_shift, col_shift, steps)
        return True

    def get_direction_by_input(self, direction):
        directions = {'w': (1, 0), 's': (-1, 0), 'a': (0, 1), 'd': (0, -1)}
        return directions.get(direction, (None, None))

    def is_move_valid(self, row_shift, col_shift, steps):
        row, col = self.empty_cell_coordinates
        new_row = row + row_shift * steps
        new_col = col + col_shift * steps
        return 0 <= new_row < FIELD_SIZE and 0 <= new_col < FIELD_SIZE
    
    def print_field(self):
        for row in self.playing_field:
            print(self.format_row(row))
        print()

    def apply_shift(self, row_shift, col_shift, steps):
        row, col = self.empty_cell_coordinates
        for _ in range(steps):
            self.playing_field[row][col] = self.playing_field[row + row_shift][col + col_shift]
            row += row_shift
            col += col_shift
        self.playing_field[row][col] = EMPTY_CELL
        self.empty_cell_coordinates = (row, col)

    def format_row(self, row):
        return "".join("   " if c == EMPTY_CELL else f"{c:2d} " for c in row)

