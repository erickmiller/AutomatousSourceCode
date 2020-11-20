from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

state = Object()
state.in_game = True
state.current_player = False
state.board = [None] * 9
state.root = None

players = ['X', 'O']
winning_directions = [
        [1, 3, 4],
        [3],
        [3, 2],
        [1],
        [],
        [],
        [1],
        [],
        [],
]

class TicTacToeApp(App):
    def build(self):
        state.root = Builder.load_file('main.kv')
        return state.root

def new_game(self, root):
    board_widget = root.ids.board
    for square_num in range(len(state.board)):
        state.board[square_num] = None
        board_widget.children[square_num].text = ''
        board_widget.children[square_num].background_color = [0.25, 0, 0.25, 1]
    state.in_game = True
    state.current_player = False
    root.ids.status.text = 'Turn: {}'.format(players[state.current_player])

def check_winner(root):
    open_squares = 0
    board_widget = root.ids.board
    for square in range(len(state.board)):
        player = state.board[square]
        if player is None:
            open_squares += 1
            continue
        for direction in winning_directions[square]:
            if (player == state.board[square + direction]
                    and player == state.board[square + 2 * direction]):
                state.in_game = False
                for button_number in (square,
                        square + direction,
                        square + 2 * direction):
                    # The next line is to work around the children being in
                    # reverse order from the .kv file.
                    # This is apparentnly deliberate behavior, optimized for
                    # touch dispatch?
                    kids = list(reversed(board_widget.children))
                    kids[button_number].background_color = [1, 0, 1, 1]
                root.ids.status.text = '{} wins!'.format(players[player])
    if open_squares < 1:
        root.ids.status.text = 'Tie!'
        state.in_game = False

def press(button, root):
    if not state.in_game:
        return
    square = button.square
    if state.board[square] is not None:
        return
    button.text = players[state.current_player]
    state.board[square] = state.current_player
    state.current_player = not state.current_player
    root.ids.status.text = 'Turn: {}'.format(players[state.current_player])
    check_winner(root)

if __name__ == '__main__':
    app = TicTacToeApp()
    app.run()
