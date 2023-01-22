class ScreenFunctions:
    def __init__(self, scrn):
        self.screen = scrn
        self.screen.title("Snake Game")
        self.screen.setup(786, 586)
        self.screen.bgpic("images/background.png")

    def key_listen(self, s):
        screen = self.screen
        screen.listen()
        screen.onkeypress(key="Right", fun=s.move_right)
        screen.onkeypress(key="d", fun=s.move_right)
        screen.onkeypress(key="D", fun=s.move_right)
        screen.onkeypress(key="Left", fun=s.move_left)
        screen.onkeypress(key="a", fun=s.move_left)
        screen.onkeypress(key="A", fun=s.move_left)
        screen.onkeypress(key="Up", fun=s.move_up)
        screen.onkeypress(key="w", fun=s.move_up)
        screen.onkeypress(key="W", fun=s.move_up)
        screen.onkeypress(key="Down", fun=s.move_down)
        screen.onkeypress(key="s", fun=s.move_down)
        screen.onkeypress(key="S", fun=s.move_down)
