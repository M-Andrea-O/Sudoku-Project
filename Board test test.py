from Board_Class import *
pygame.init()
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption('Board Class Testing')
clock = pygame.time.Clock()
board = Board(720, 720, screen, "easy")
print(f"Board width: {board.width}")
print(f"Board height: {board.height}")
print(f"Cell size: {board.cell_size}")
print(f"Number of rows: {len(board.cells)}")
print(f"Number of cols in first row: {len(board.cells[0])}")
print(f"Selected cell: ({board.selected_x}, {board.selected_y})")
empty = board.find_empty()
print(f"   : {empty}")
board.select(2, 3)
print(f"   Selected: ({board.selected_x}, {board.selected_y})")
result = board.is_full()


print(f"   Is board full? {result}")

board.select(4, 5)
print(f"selected: ({board.selected_x}, {board.selected_y})")
board.select(2, 3)
print("select",{board.selected_x}, {board.selected_y})
board.sketch(7)
print(f"Sketched value at (2,3): {board.cells[2][3].sketched_value}")


