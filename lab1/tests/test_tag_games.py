import unittest
from lab1.task2.tag_games import TagGame, EMPTY_CELL, FIELD_SIZE

class TestTagGames(unittest.TestCase):

    def setUp(self):
        self.game=TagGame()

    def test_generate_numbers(self):
        numbers=self.game.generate_numbers()
        self.assertEqual(len(numbers),FIELD_SIZE*FIELD_SIZE)
        self.assertIn(EMPTY_CELL,numbers)

    def test_empty_position(self):
        row,col=self.game.get_empty_cell_position()
        self.assertTrue(0<=row<FIELD_SIZE)
        self.assertTrue(0<=col<FIELD_SIZE)

    def test_create_matrix_from_numbers(self):
        numbers=list(range(FIELD_SIZE*FIELD_SIZE))
        field_matrix=self.game.create_matrix_from_numbers(numbers)
        self.assertEqual(len(field_matrix),FIELD_SIZE)
        self.assertTrue(all(len(row))==FIELD_SIZE for row in field_matrix)

    def test_get_tiles_without_empty(self):
        tiles=self.game.get_tiles_without_empty()
        self.assertEqual(len(tiles),FIELD_SIZE*FIELD_SIZE-1)
        self.assertNotIn(EMPTY_CELL,tiles)

    def test_count_inversions(self):
        inversions=self.game.count_inversions()
        self.assertIsInstance(inversions,int)
        self.assertGreaterEqual(inversions,0)
    
    def test_is_game_solvable(self):
        self.assertIsInstance(self.game.is_solvable(),bool)
        self.assertFalse(self.game.is_solved())

    def test_is_not_solvable(self):
        solved = list(range(1, 16)) + [0]
        solved[0], solved[1] = solved[1], solved[0]  
        self.game.playing_field = [solved[i:i+4] for i in range(0, 16, 4)]
        self.game.empty_cell_coordinates = self.game.get_empty_cell_position()
        self.assertFalse(self.game.is_solvable())

    def test_move_invalid_direction(self):
        result = self.game.move_cells("x", 1)
        self.assertFalse(result)
    
    def test_format_row(self):
        row = [1, 0, 3, 4]
        formatted = self.game.format_row(row)
        self.assertEqual(formatted, " 1     3  4 ")

    def test_move_cells_invalid(self):
        self.game.playing_field = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]  
        ]
        self.game.empty_cell_coordinates = self.game.get_empty_cell_position()
        result = self.game.move_cells("w", 1)
        self.assertFalse(result)

    def test_get_shift_delta(self):
        self.assertEqual(self.game.get_direction_by_input("w"), (1,0))
        self.assertEqual(self.game.get_direction_by_input("s"), (-1,0))
        self.assertEqual(self.game.get_direction_by_input("a"), (0,1))
        self.assertEqual(self.game.get_direction_by_input("d"), (0,-1))
        self.assertEqual(self.game.get_direction_by_input("x"), (None,None))

    def test_apply_shift(self):
        self.game.playing_field = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,0,15]
        ]
        self.game.empty_cell_coordinates = self.game.get_empty_cell_position()
        self.game.apply_shift(0,1,1) 
        self.assertEqual(self.game.empty_cell_coordinates, (3,3))
        self.assertEqual(self.game.playing_field[3][2], 15)

    def test_can_correct_move(self):
        self.game.empty_cell_coordinates = (3,3)
        self.assertTrue(self.game.is_move_valid(-1,0,1)) 
        self.assertFalse(self.game.is_move_valid(1,0,1)) 