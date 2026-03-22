class Action:
    pass
# EscapeAction will be used when we hit the Esc key (to exit the game).
class EscapeAction(Action):
    pass

# MovementAction will be used to describe our player moving around.
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy